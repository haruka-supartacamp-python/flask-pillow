from flask import Flask
from flask import render_template
from flask import request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


# @app.route("/upload", methods=["POST"])
# def upload():
#     file = request.files["uploadFile"]
#     file.save("images/upload.png")
#     uploadFile = file.open("images/upload.png")
#     img = Image.open(file)
#     resized_img = img.resize((uploadFile.width, uploadFile.height))
#     uploadFile.paste(resized_img, (0, 0), resized_img)
#     uploadFile.save("images/out2.png")
#     return uploadFile.show()


if __name__ == "__main__":
    app.run(debug=True)
