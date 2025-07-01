# Joke API - MCP Server cho Claude

Đây là một project nhỏ xây dựng một máy chủ API cục bộ (local) sử dụng Python. Project được thiết kế để kết nối với ứng dụng Claude Desktop thông qua **Giao thức Ngữ cảnh Mô hình (Model Context Protocol - MCP)**, cho phép Claude tương tác với các "công cụ" (tools) do bạn tự định nghĩa.

Trong ví dụ này, chúng ta tạo ra các công cụ để lấy những câu chuyện cười vui nhộn từ nhiều "nhà cung cấp" khác nhau (ví dụ: truyện cười của Anh Hoàng, Anh Tín).

## ✨ Tính Năng

* **Tích hợp trực tiếp với Claude:** Sử dụng thư viện `mcp.server` để giao tiếp hiệu quả với Claude Desktop App qua `stdio`.
* **Kiến trúc Module hóa:** Dễ dàng thêm các nguồn cung cấp truyện cười mới mà không cần thay đổi logic cốt lõi.
* **API đơn giản:** Cung cấp các "tool" rõ ràng để liệt kê các loại truyện cười và lấy một truyện cười cụ thể.

## 🚀 Công Nghệ Sử Dụng

* **Ngôn ngữ:** Python 3
* **Thư viện chính:**
  * `mcp.server`: Để tạo máy chủ MCP tương thích với Claude.
  * `python-dotenv`: Để quản lý các biến môi trường (tùy chọn).

## 📂 Cấu Trúc Project

```
MCPMINI/
├── .venv/                  # Thư mục môi trường ảo
├── src/
│   ├── joke/
│   │   ├── providers/
│   │   │   ├── base_provider.py    # Lớp cơ sở cho các provider
│   │   │   ├── hoang_jokes.py      # Provider truyện cười của Anh Hoàng
│   │   │   └── tin_jokes.py        # Provider truyện cười của Anh Tín
│   │   ├── __init__.py
│   │   └── joke_factory.py         # Factory để chọn provider
│   ├── __init__.py
│   ├── main.py                     # Điểm khởi chạy của ứng dụng
│   └── server.py                   # Nơi định nghĩa và đăng ký các tool MCP
├── .gitignore
└── README.md
```

## 🛠️ Cài Đặt và Cấu Hình

### 1. Chuẩn bị môi trường

Đầu tiên, hãy đảm bảo bạn đã cài đặt Python 3. Sau đó, tạo và kích hoạt môi trường ảo:

```bash
# Di chuyển đến thư mục gốc của project
cd /path/to/your/MCPMINI

# Tạo môi trường ảo
python -m venv .venv

# Kích hoạt môi trường ảo
# Trên Windows:
.\.venv\Scripts\activate
# Trên macOS/Linux:
# source .venv/bin/activate
```

### 2. Cài đặt thư viện

Tạo một file tên là `requirements.txt` trong thư mục gốc với nội dung sau:

**`requirements.txt`**
```
mcp.server
python-dotenv
```

Sau đó, chạy lệnh sau để cài đặt:
```bash
pip install -r requirements.txt
```

### 3. Cấu hình Claude Desktop App

Để Claude có thể "thấy" và chạy server của bạn, bạn cần cấu hình file `mcp_servers.json`:

1. Trong ứng dụng Claude, vào **Settings -> Developer**.
2. Nhấn nút **"Edit Config"**.
3. Dán đoạn JSON sau vào, **nhớ thay thế các đường dẫn cho đúng với máy của bạn**:
   ```json
   {
       "mcpServers": {
           "my-joke-api": {
               "command": "C:\\path\\to\\your\\MCPMINI\\.venv\\Scripts\\python.exe",
               "args": [
                   "C:\\path\\to\\your\\MCPMINI\\src\\main.py"
               ]
           }
       }
   }
   ```
4. Lưu file lại và **khởi động lại hoàn toàn** Claude (tắt hẳn từ khay hệ thống).

## ▶️ Cách Sử Dụng

Bạn **không cần** chạy server bằng tay. Claude sẽ tự động làm việc đó khi bạn gọi đến tool.

Sau khi đã hoàn tất các bước cài đặt và cấu hình:

1. Mở ứng dụng Claude.
2. Trong ô chat, gõ `@`. Bạn sẽ thấy server của mình xuất hiện (ví dụ: `@Joke API Server`).
3. Thử các câu lệnh sau:
   * `@Joke API Server list available joke types`
   * `@Joke API Server get joke by type with joke_type 'hoang'`
   * Hoặc đơn giản là: `@Joke API Server kể chuyện cười của anh Tín`

Claude sẽ tự động khởi chạy file `main.py` của bạn, gửi yêu cầu đến tool tương ứng và hiển thị kết quả.

## 🧩 Mở Rộng

Để thêm một nguồn truyện cười mới (ví dụ: của Anh Sơn):

1. Tạo file `src/joke/providers/son_jokes.py` theo mẫu của các file provider khác.
2. Trong file `src/joke/joke_factory.py`, import `SonJokeProvider` và thêm nó vào từ điển `AVAILABLE_JOKE_PROVIDERS`:
   ```python
   AVAILABLE_JOKE_PROVIDERS = {
       "hoang": HoangJokeProvider,
       "tin": TinJokeProvider,
       "son": SonJokeProvider, # Thêm dòng mới
   }
   ```

Vậy là xong! Tool của bạn sẽ tự động nhận diện được nguồn truyện cười mới.
