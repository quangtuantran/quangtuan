import cv2
import numpy as np

# Load hình ảnh
image = cv2.imread('pngegg.png')  # Thay 'pngegg.png' bằng đường dẫn của hình ảnh bạn muốn hiển thị

# Tạo một khung màu xanh
frame_color = (0, 255, 0)  # Màu xanh (BGR)
frame_thickness = 10  # Độ dày của khung

# Lấy kích thước của màn hình
screen_width, screen_height = 1500, 1000 # Thay đổi kích thước theo độ phân giải của màn hình của bạn

# Resize hình ảnh để phù hợp với kích thước màn hình
image = cv2.resize(image, (screen_width, screen_height))

# Tính toán tọa độ để hiển thị hình ảnh giữa màn hình
image_height, image_width = image.shape[:2]
start_x = (screen_width - image_width) // 2
start_y = (screen_height - image_height) // 2

# Tạo hình ảnh trống với màu nền trắng
background = np.full((screen_height, screen_width, 3), (255, 255, 255), dtype=np.uint8)

# Chèn hình ảnh vào vị trí được tính toán trước đó
background[start_y:start_y+image_height, start_x:start_x+image_width] = image

# Hiển thị khung màu xanh
cv2.rectangle(background, (start_x - frame_thickness, start_y - frame_thickness),
              (start_x + image_width + frame_thickness, start_y + image_height + frame_thickness),
              frame_color, frame_thickness)

# Hiển thị hình ảnh trên màn hình
cv2.imshow('Image with Green Frame', background)
cv2.waitKey(0)
cv2.destroyAllWindows()
