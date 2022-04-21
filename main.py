from flask import Flask, render_template, current_app, redirect, url_for
from forms import PostForm
import secrets, os
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY']='257ewy438yhewh276eyu8547hw734hwujjdeh5'


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/uploads', picture_fn)

    output_size = (256,256)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

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
	p=""
	colors=30
	if form.validate_on_submit():
		p=save_picture(form.picture.data)
		original= os.path.join(current_app.root_path, 'static/uploads',p)
		compressed= os.path.join(current_app.root_path, 'static/compressed_files',p)
	return render_template('upload.html',title='result',p=p,colors=colors)




if __name__ == '__main__':
    app.run(debug=True)
