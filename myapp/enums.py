# enums.py
# Định nghĩa các enum/choices dùng cho models

ORDER_STATUS_CHOICES = [
    ('pending', 'Chờ xác nhận'),
    ('confirmed', 'Đã xác nhận'),
    ('shipped', 'Đang giao'),
    ('completed', 'Đã giao thành công'),
    ('cancelled', 'Hủy bởi người dùng'),
    ('rejected', 'Bị từ chối bởi admin'),
]
