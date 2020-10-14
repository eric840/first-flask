from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html') # by default looks for index.html inside a templates folder in the same directory as this script.


@app.route("/another")
def show():
    return '<h1>Yo</h1>'

@app.route('/user/<username>')
def show_user(username):
    return f"Hi {username[0:3]}"

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()