from json import load
import os
from speechbrain.pretrained import SpeakerRecognition
import face_recognition
import warnings
from keras.models import Sequential, load_model
from keras.layers import Dense, Input

warnings.filterwarnings("ignore", category=UserWarning)

verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec"
)

def face_register(img):
    image = face_recognition.load_image_file(img)
    face_landmarks_list = face_recognition.face_landmarks(image)
    if not face_landmarks_list:
        print("No faces detected!")
    else:
        print("Detected")

    return face_landmarks_list


def face_verify(imagev, image):

    known_encoding = face_recognition.face_encodings(image)[0]
    unknown_encoding = face_recognition.face_encodings(imagev)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
    return results


def verify_voice(v1, v2):
    score, prediction = verification.verify_files(
        v1,
        v2
    )

    return score, prediction

if os.path('./model.h5'):
    model = Sequential()

    model.add(Input(shape=(5, )))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(epochs=30, batch_size=20, validation_batch_size=0.2)

    model.save('model.h5')

def Fraud_detect(inputs):
    model = load_model('model.h5')
    predict = model.predict(inputs)

    return predict