from flask import Flask, send_file, render_template, abort
from jinja2 import TemplateNotFound
app = Flask(__name__)

@app.route("/")
@app.route("/<static>")
def index(static = None):
    if static : 
        try:
            return render_template(static + '.html')
        except:
            abort(404)
    else :
        return render_template('index.html')

@app.route("/table")
def table():
    return render_template('table.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
