from flask import Flask, render_template, current_app, redirect, url_for
from forms import PostForm
import secrets, os
from PIL import Image
from compression import compress_image


app = Flask(__name__)
app.config['SECRET_KEY']='257ewy438yhewh276eyu8547hw734hwujjdeh5'


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)  # generate random hexadecimal token to uniquely identify image
    _, file_extension = os.path.splitext(form_picture.filename)  # split path to get extension type
    picture_function = random_hex + file_extension  # renaming image using generated token
    picture_path = os.path.join(current_app.root_path, 'static/uploads', picture_function)  # creates new path to store image in.
    form_picture.save(picture_path)  # saves image from html form in picture_path
    return picture_function


@app.route('/',methods=['GET','POST'])
def home():
	form = PostForm()
	return render_template('home.html',title='Upload',form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    form=PostForm()
    picture = ""  # empty file
    if form.validate_on_submit():
        picture = save_picture(form.picture.data)
        original_path = os.path.join(current_app.root_path, 'static/uploads', picture)  # path to store uploaded file
        compressed_path = os.path.join(current_app.root_path, 'static/compressed_files',picture)  # creates a path to store compressed file in.
        compress_image(form.picture.data, compressed_path)  # uses PIL compressor to compress and save image in compressed_path.

        uploaded_image_size = str("{:.1f}".format(os.stat(original_path).st_size / 1024)) + 'kb'  # calculates size of uploaded image in kilobytes.
        compressed_image_size = str("{:.1f}".format(os.stat(compressed_path).st_size / 1024)) + 'kb'  # calculates size of compressed image in kilobytes.

        return render_template('upload.html',title='result',picture=picture, upload_size=uploaded_image_size, compressed_size=compressed_image_size)


if __name__ == '__main__':
    app.run(debug=True)
