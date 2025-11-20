# naitei14_python_nhom3

npx sunlint --all --input=. 


## Hướng dẫn migrate database và chạy server

### 1. Cài đặt các package cần thiết
```bash
pip install -r requirements.txt
```

### 2. Tạo file .env
Copy file `.env.example` thành `.env` và điền thông tin kết nối database của bạn.

### 3. Thực hiện migrate database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Chạy server
```bash
python manage.py runserver
```

### 5. (Tùy chọn) Tạo superuser để truy cập admin
```bash
python manage.py createsuperuser
```