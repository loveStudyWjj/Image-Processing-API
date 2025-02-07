import cv2
import numpy as np
from skimage import filters
import base64

class ImageProcessor:
    @staticmethod
    async def process_image(image_data: bytes, process_type: str, params: dict):
        nparr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if process_type == "grayscale":
            processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif process_type == "canny":
            low = params.get("low_threshold", 100)
            high = params.get("high_threshold", 200)
            processed = cv2.Canny(img, low, high)
        elif process_type == "gaussian":
            sigma = params.get("sigma", 1.0)
            processed = filters.gaussian(img, sigma=sigma, channel_axis=2)
        else:
            raise ValueError("Unsupported processing type")
        
        _, buffer = cv2.imencode('.jpg', processed)
        return base64.b64encode(buffer).decode('utf-8')