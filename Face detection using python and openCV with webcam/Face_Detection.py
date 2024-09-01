# pip install opencv-python (tải terminal trước nhé)
import cv2

# Tải file xml để nhận diện khuôn mặt
a = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Mở camera
b = cv2.VideoCapture(0)

while True:
    # Đọc hình ảnh từ camera
    c_rec, d_image = b.read()
    
    # Chuyển đổi hình ảnh sang màu xám
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    
    # Nhận diện khuôn mặt
    f = a.detectMultiScale(e, 1.3, 6)

    # Vẽ hình chữ nhật quanh khuôn mặt
    for (x1,y1,w1,h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1+w1, y1+h1), (255,0,0), 5)

    # Hiển thị hình ảnh
    cv2.imshow('img', d_image)
    
    # Đợi phím tắt
    h = cv2.waitKey(40) & 0xff
    
    # Thoát nếu nhấn phím 'esc' (mã ASCII là 27)
    if h == 27:
        break

# Giải phóng camera
b.release()
# Đóng tất cả cửa sổ
cv2.destroyAllWindows()