from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('paginaInicial.html')