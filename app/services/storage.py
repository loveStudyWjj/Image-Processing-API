from app.database.mysql import get_connection
from app.database.redis import redis_client
import time

class StorageService:
    @staticmethod
    def save_process_record(filename: str, process_type: str):
        with get_connection() as conn:
            with conn.cursor() as cursor:
                sql = """
                INSERT INTO image_process 
                (original_filename, process_type, status, created_at)
                VALUES (%s, %s, %s, %s)
                """
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute(sql, (filename, process_type, 'processing', created_at))
                conn.commit()
                return cursor.lastrowid

    @staticmethod
    def update_process_status(process_id: int, status: str, result: str = None):
        with get_connection() as conn:
            with conn.cursor() as cursor:
                sql = """
                UPDATE image_process 
                SET status = %s, result_path = %s 
                WHERE id = %s
                """
                cursor.execute(sql, (status, result, process_id))
                conn.commit()

        if status == 'completed' and result:
            redis_client.set(f"process:{process_id}", result, ex=3600)