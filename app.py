from flask import Flask, request, render_template
from model import ans
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def classifierA():
    if request.method == "POST":
        val1 = request.form.get("ans_1")
        val2 = request.form.get("ans_2")
        val3 = request.form.get("ans_3")
        val4 = request.form.get("ans_4")
        out = ans(val1, val2, val3, val4)
        return render_template("index.html",out=  out)

    return render_template("index.html",out=" ")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port = 8080)

if __name__ == "__main__":
    app.run(debug=True)