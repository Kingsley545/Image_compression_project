import os
from PIL import Image
import imageio
from flask import Flask,render_template,current_app,redirect,url_for



def compress_image(form_picture, compressed_path):
    foo = Image.open(form_picture)
    foo.save(compressed_path, optimize=True, quality=50)
