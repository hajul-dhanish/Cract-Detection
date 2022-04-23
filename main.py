import os
from flask import Flask, request

UPLOAD_FOLDER = "./upload"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file1" not in request.files:
            return "there is no file1 in form!"
        file1 = request.files["file1"]
        print(file1.stream.readline)
        path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
        file1.save(path)
        return file1.filename

    return """
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
      <input type="file" name="file2">
      <input type="submit">
    </form>
    """


@app.route("/detect", methods=["GET", "POST"])
def uplodd():
    os.system("python3 CrackDetection.py")

    return "Hi Priya!!!!"




if __name__ == "_main_":
    # app.run()
    app.run(host="0.0.0.0", port=5000)