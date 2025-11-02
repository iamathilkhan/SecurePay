from flask import render_template, request
from .models import face_model
from . import verify_bp

@verify_bp.route('/')
def verify():
    return render_template('/voice.html', title = 'Face Verification')

@verify_bp.route('/face', methods = ['POST'])
def face():
    face = request.files['face']
    name = face.filename
    print(face, name)
    print(face_model())
    return "Face recived"
