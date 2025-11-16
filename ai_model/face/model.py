import face_recognition
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def face_register(img):
    image = face_recognition.load_image_file(img)
    face_landmarks_list = face_recognition.face_landmarks(image)
    if not face_landmarks_list:
        print("No faces detected!")
    else:
        print("Detected")


def face_verify(imagev, image):

    known_encoding = face_recognition.face_encodings(image)[0]
    unknown_encoding = face_recognition.face_encodings(imagev)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)