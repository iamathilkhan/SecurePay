import cv2

alg = "haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(alg)

img = cv2.imread("./detect.jpg", cv2.IMREAD_GRAYSCALE)

faces = model.detectMultiScale(
    img,
    scaleFactor=1.05,
    minNeighbors=2,
    minSize=(100, 100)
)

for x, y, w, h in faces:
    cropped_image = img[y : y + h, x : x + w]
    target_file_name = 'face.jpg'
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )
