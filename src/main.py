import uvicorn

# Dòng này cần thiết để Python có thể tìm thấy module trong thư mục src
# Thường thì các công cụ build sẽ xử lý việc này, nhưng để chạy trực tiếp thì cần
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.server import app

if __name__ == "__main__":
    # --reload: server tự khởi động lại khi có thay đổi code
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)