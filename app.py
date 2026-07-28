from flask import Flask, render_template, request

app = Flask(__name__)

images = [
    "/static/cat1.jpg",
    "/static/cat2.jpg",
    "/static/cat3.jpg",
    "/static/scat4.jpg"
]

@app.route("/", methods=["GET", "POST"])
def home():
    index = 0

    if request.method == "POST":
        index = int(request.form["index"])
        index = (index + 1) % len(images)

    return render_template(
        "index.html",
        image=images[index],
        index=index
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)