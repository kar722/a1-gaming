# import "packages" from flask
from flask import Flask, render_template, request

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


@app.route('/Mobile/')
def Mobile():
    return render_template("hawkers.html")

@app.route('/Video Journals/')
def mini():
    return render_template("Video Journals.html")

@app.route('/binary/')
def binary():
    return render_template("binary.html")

@app.route('/howitsmade/')
def howitsmade():
    return render_template("howitsmade.html")



@app.route('/howitsmade/', methods=['GET', 'POST'])
def greet1288():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("howitsmade.html", name1=name)
    # starting and empty input default
    return render_template("howitsmade.html.html", name1="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)