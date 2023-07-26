from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('task2_evaluation.html')

@app.route('/hash', methods=["POST"])
def calculate_hash():
    image = request.files['img']

    temp_path = "temp_image"
    image.save(temp_path)

    with open(temp_path, "rb") as f:
        im_bytes = f.read()
    im_hash = hashlib.md5(im_bytes).hexdigest()

    # Remove the temporary image file
    import os
    os.remove(temp_path)

    return im_hash

if __name__ == '__main__':
    app.run(debug=True)
