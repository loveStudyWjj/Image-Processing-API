from pydantic import BaseModel
from datetime import datetime


class ImageProcessResult(BaseModel):
    id: int
    original_filename: str
    process_type: str
    created_at: datetime
    status: str
