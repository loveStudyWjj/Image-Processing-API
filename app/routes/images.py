import json
import traceback
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.services.image_processing import ImageProcessor
from app.services.storage import StorageService
from app.models.image_model import ImageProcessResult
import time
from app.database.redis import redis_client
from app.database.mysql import get_connection
from typing import List

router = APIRouter()


@router.post("/process", response_model=ImageProcessResult)
async def process_image(
    process_type: str = Form(...),
    parameters: str = Form(...),
    files: List[UploadFile] = File(...),

):
    parameters = json.loads(parameters)
    try:
        file = files[0]
        # 保存处理记录
        process_id = StorageService.save_process_record(
            file.filename,
            process_type
        )

        # 处理图像
        image_data = await file.read()
        processed_image = await ImageProcessor.process_image(
            image_data,
            process_type,
            parameters
        )

        # 更新状态和存储结果
        StorageService.update_process_status(
            process_id,
            'completed',
            processed_image
        )

        return {
            "id": process_id,
            "original_filename": file.filename,
            "process_type": process_type,
            "created_at": time.strftime('%Y-%m-%d %H:%M:%S'),
            "status": 'completed'
        }

    except Exception as e:
        print(traceback.format_exc())
        StorageService.update_process_status(process_id, 'failed')
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/result/{process_id}")
async def get_result(process_id: int):
    # 尝试从Redis获取缓存
    cached = redis_client.get(f"process:{process_id}")
    if cached:
        return {"status": "completed", "result": cached}

    # 查询数据库
    with get_connection() as conn:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM image_process WHERE id = %s"
            cursor.execute(sql, (process_id,))
            result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="Process not found")

    return {
        "status": result['status'],
        "result": result['result_path'] if result['status'] == 'completed' else None
    }
