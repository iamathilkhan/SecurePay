from flask import render_template, request
from .models import face_model
from . import verify_bp


@verify_bp.route('/')
def verify():
    # template is under app/blueprints/verify/templates/verify/face.html
    return render_template('verify/face.html')


@verify_bp.route('/face', methods=['POST'])
def face():
    face = request.files['face']
    name = face.filename
    print(face, name)
    print(face_model())
    return "Face received"
