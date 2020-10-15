from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    signed_in = True # we are hardcoding this just to demonstrate how we can do conditionals in our template files, in future we won't be hardcoding this.
    return render_template('index.html', signed_in=signed_in)

@app.route("/<name>")
def index_name(name):
    name = name.upper()
    return render_template('index.html', name=name)

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route('/user/<username>')
def show_user(username):
    return f"Hi {username[0:3]}"

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()