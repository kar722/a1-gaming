# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

@app.route('/karthikgreet/')
def greet():
    return render_template("karthikgreet")

@app.route('/karthikgreet/', methods=['GET', 'POST'])
def greet1():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("karthikgreet.html", name1=name)
    # starting and empty input default
    return render_template("karthikgreet.html", name1="World")

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

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/mini-labs/')
def mini():
    return render_template("mini-labs.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
