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
"""
@app.route("/test1")
def test1():
    return render_template('test1.html')

@app.route("/test2")
def test2():
    return render_template('test2.html')
"""
if __name__ == "__main__":
    app.debug = True
    app.run()
