from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return render_template('index.html', first_name=first_name, last_name=last_name)

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
    signed_in = True # we are hardcoding this just to demonstrate how we can do conditionals in our template files
    return render_template('contact.html', signed_in=signed_in)

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()