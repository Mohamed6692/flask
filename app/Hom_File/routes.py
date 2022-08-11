from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory

from app.Hom_File import Hom_File
from app.Hom_File.models import File
from app import db
from app import create_app
from app.Hom_File.forms import Upload
import urllib.request
from flask_login import current_user
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
appl = create_app()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@Hom_File.route('/')
def home():
    return render_template('gest.html')


@Hom_File.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    description = request.form.get('description')
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(appl.config['UPLOAD_FOLDER'], filename))
        file = File(
            description=description,
            filename=filename,
            file=file,
            user_id=current_user.id
        )
        db.session.add(file)
        db.session.commit()
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('gest.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@Hom_File.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='' + filename), code=301)


@Hom_File.route('/files')
def files():
    files = File.query.all()
    return render_template('files.html', files=files)
