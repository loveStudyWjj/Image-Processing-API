import requests
import json

url = "http://localhost:8000/api/images/process"
file_path = r"D:\Desktop\tmp\下载.jpg"

data = {
    "process_type": "grayscale",
    "parameters": json.dumps({"width": 800, "height": 600})
}
with open(file_path, "rb") as file:
    files = [('files', file)]

    response = requests.post(
        url,
        data=data,
        files=files,
    )

if response.status_code == 200:
    print("Success!")
    print("Response JSON:", response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print("Error message:", response.text)
