from flask import render_template
from . import verify_bp

@verify_bp.route('/')
def verify():
    return render_template('/face.html', title = 'Face Verification')
