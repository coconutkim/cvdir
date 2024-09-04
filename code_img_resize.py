# 이미지 크기 조정 (화면 크기에 맞게 조절)
def resize_image(img, max_width=800, max_height=600):
    h, w = img.shape[:2]
    aspect_ratio = w / h
    if w > max_width or h > max_height:
        if aspect_ratio > 1:
            new_w = max_width
            new_h = int(max_width / aspect_ratio)
        else:
            new_h = max_height
            new_w = int(max_height * aspect_ratio)
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    return img

img = resize_image(img)