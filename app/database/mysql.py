import pymysql
from app.utils.config import settings


def get_connection():
    return pymysql.connect(
        host=settings.mysql_host,
        user=settings.mysql_user,
        password=settings.mysql_password,
        db=settings.mysql_db,
        cursorclass=pymysql.cursors.DictCursor
    )


def init_db():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS image_process (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    original_filename VARCHAR(255),
                    process_type VARCHAR(50),
                    status VARCHAR(20),
                    result_path TEXT,
                    created_at DATETIME
                )
            """)
        conn.commit()


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!")
