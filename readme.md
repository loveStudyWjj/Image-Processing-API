

# Image Processing API

这是一个基于 FastAPI 的小型图像处理项目，集成了 OpenCV、scikit-image、PyMySQL 和 Redis 技术。用户可以通过 API 上传图像并对其进行处理，处理结果会存储在 MySQL 数据库中，并使用 Redis 缓存以提高性能。

## 功能特性

- 支持多种图像处理操作（灰度化、Canny 边缘检测、高斯模糊等）。
- 使用 MySQL 持久化存储处理记录。
- 使用 Redis 缓存处理结果，提高查询性能。
- 提供完整的 RESTful API 接口。
- 异步处理，支持高并发。

## 技术栈

- **FastAPI**: 用于构建高性能的 RESTful API。
- **OpenCV**: 用于图像处理。
- **scikit-image**: 提供高级图像处理算法。
- **PyMySQL**: 用于连接和操作 MySQL 数据库。
- **Redis**: 用于缓存处理结果。

---

## 安装与运行

### 1. 克隆项目

```bash
git clone image-processing-api.git
cd image-processing-api
```

### 2. 安装依赖

确保已安装 Python 3.8+，然后运行以下命令安装依赖：

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

在项目根目录下创建 `.env` 文件，并填写以下内容：

```plaintext
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=image_db
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

### 4. 创建数据库

- image_db库


### 5. 启动服务

运行以下命令启动 FastAPI 服务：

```bash
uvicorn app.main:app --reload
```

服务启动后，访问 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 查看 API 文档。

---

## API 文档

### 1. 上传并处理图像

- **URL**: `/api/images/process`
- **Method**: `POST`
- **Request Body**:
  - `file`: 图像文件（支持 JPG、PNG 等格式）。
  - `process_type`: 处理类型（如 `grayscale`、`canny`、`gaussian`）。
  - `parameters`: 处理参数（可选）。
- **Response**:
  - `id`: 处理记录 ID。
  - `original_filename`: 原始文件名。
  - `process_type`: 处理类型。
  - `created_at`: 处理时间。
  - `status`: 处理状态（如 `completed`）。


### 2. 获取处理结果

- **URL**: `/api/images/result/{process_id}`
- **Method**: `GET`
- **Response**:
  - `status`: 处理状态（如 `completed`、`failed`）。
  - `result`: 处理结果的 Base64 编码（如果状态为 `completed`）。



---

## 项目结构

```
image-processing-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── mysql.py
│   │   └── redis.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── image_model.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── images.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── image_processing.py
│   │   └── storage.py
│   └── utils/
│       ├── __init__.py
│       └── config.py
├── requirements.txt
└── README.md
```

---

## 依赖列表

- `fastapi>=0.68.0`
- `uvicorn>=0.15.0`
- `python-multipart`
- `opencv-python-headless`
- `scikit-image`
- `pymysql`
- `redis`
- `python-dotenv`
- `pydantic-settings`


---

## 许可证

本项目基于 MIT 许可证开源。详情请参阅 [LICENSE](LICENSE) 文件。

---


Enjoy your image processing! 🚀