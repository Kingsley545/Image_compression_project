from PIL import Image


def compress_image(form_picture, compressed_path):
    foo = Image.open(form_picture)
    foo.save(compressed_path, optimize=True, quality=50)
