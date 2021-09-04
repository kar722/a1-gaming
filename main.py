# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)

@app.route('/aboutmekarthik/')
def kargreet():
    return render_template("aboutmekarthik.html")

@app.route('/aboutmekarthik/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutmekarthik.html", name1=name)
    # starting and empty input default
    return render_template("aboutmekarthik.html", name1="World")

@app.route('/aboutmedaniel/')
def dangreet():
    return render_template("aboutmedaniel.html")

@app.route('/aboutmedaniel/', methods=['GET', 'POST'])
def greet2():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutmedaniel.html", name1=name)
    # starting and empty input default
    return render_template("aboutmedaniel.html", name1="World")

@app.route('/aboutmedylan/')
def dylangreet():
    return render_template("aboutmedylan.html")

@app.route('/aboutmedylan/', methods=['GET', 'POST'])
def greet3():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutmedylan.html", name1=name)
    # starting and empty input default
    return render_template("aboutmedylan.html", name1="World")

@app.route('/aboutmewilliam/')
def wilgreet():
    return render_template("aboutmewilliam.html")

@app.route('/aboutmewilliam/', methods=['GET', 'POST'])
def greet4():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("aboutmewilliam.html", name1=name)
    # starting and empty input default
    return render_template("aboutmewilliam.html", name1="World")

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
