# Website-GearHub

## Cách cài đặt và chạy website
- Cần có python version 3.13+ (Download tại [python.org](http://www.python.org/downloads/))

1. **Tạo môi trường ảo (Virtual Environment):**
```bash
python -m venv venv
```
2. **Kích hoạt môi trường ảo (Activate Virtual Environment):**
- Window: `venv\Scripts\activate`
- GitBash: `source venv/Scripts/activate`
- MacOS/Linux: `source venv/bin/activate`
3. **Cài đặt các thư viện cần thiết:**
```bash
pip install -r requirements.txt
```
4. **Chạy dự án:**
- Chạy lệnh migrate để khởi tạo database:
```bash
python manage.py migrate
```
- Khởi chạy website:
```bash
python manage.py runserver
```
- Sau đó truy cập vào địa chỉ http://127.0.0.1:8000/ hoặc mở trình duyệt và gõ vào thanh tìm kiếm: `localhost:8000`