# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

# create a Flask instance
app = Flask(__name__)


@app.route('/karthikgreet/')
def greet0():
    return render_template("karthikgreet.html")

@app.route('/karthikgreet/', methods=['GET', 'POST'])
def greet1():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("karthikgreet.html", name=name)
    # starting and empty input default
    return render_template("karthikgreet.html", name="World")

@app.route('/danielgreet/')
def greet2():
    return render_template("danielgreet.html")

@app.route('/danielgreet/', methods=['GET', 'POST'])
def greet3():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("danielgreet.html", name1=name)
    # starting and empty input default
    return render_template("danielgreet.html", name1="World")

@app.route('/dylangreet/')
def greet4():
    return render_template("dylangreet.html")

@app.route('/dylangreet/', methods=['GET', 'POST'])
def greet5():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("dylangreet.html", name1=name)
    # starting and empty input default
    return render_template("dylangreet.html", name1="World")

@app.route('/williamgreet/')
def greet6():
    return render_template("williamgreet.html")

@app.route('/williamgreet/', methods=['GET', 'POST'])
def greet7():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("williamgreet.html", name1=name)
    # starting and empty input default
    return render_template("williamgreet.html", name1="World")

@app.route('/greet/')
def greet8():
    return render_template("greet.html")

@app.route('/greet/', methods=['GET', 'POST'])
def greet9():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name1=name)
    # starting and empty input default
    return render_template("greet.html", name1="World")


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/PCs/')
def PCs():
    return render_template("kangaroos.html")


@app.route('/Console/')
def Console():
    return render_template("walruses.html")

@app.route('/PlayStation/')
def PlayStation():
    return render_template("PlayStation.html")

@app.route('/Mobile/')
def Mobile():
    return render_template("hawkers.html")

@app.route('/Video Journals/')
def mini():
    return render_template("Video Journals.html")

@app.route("/binary/", methods = ['GET', 'POST'])
def binary():
    BITS = 4
    imgBulbOn = "/static/assets/bulb_on.gif"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("binary.html", imgBulbOn=imgBulbOn, BITS=BITS)

@app.route('/howitsmade/')
def howitsmade():
    return render_template("howitsmade.html")

@app.route('/Apple/')
def Apple():
    return render_template("Apple.html")

@app.route('/Samsung/')
def Samsung():
    return render_template("Samsung.html")


@app.route('/xbox/')
def xbox():
    return render_template("xbox.html")

@app.route('/Laptops/')
def Laptops():
    return render_template("Laptops.html")

@app.route('/howitsmade/', methods=['GET', 'POST'])
def greet1288():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("howitsmade.html", name1=name)
    # starting and empty input default
    return render_template("howitsmade.html", name1="World")

@app.route('/rgb/', methods=['GET', 'POST'])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    return render_template('rgb.html', images=image_data(path))

@app.route('/ListHackathon/')
def ListHackathon():
    return render_template("ListHackathon.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)