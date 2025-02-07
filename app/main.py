from fastapi import FastAPI
from app.routes import images
from app.database.mysql import init_db
from contextlib import asynccontextmanager

app = FastAPI()

# 使用 lifespan 事件处理器
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 在应用启动时初始化数据库
    init_db()
    yield
    # 这里可以处理应用关闭时的清理工作（如果需要）

app = FastAPI(lifespan=lifespan)

# 包含路由
app.include_router(images.router, prefix="/api/images", tags=["images"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
