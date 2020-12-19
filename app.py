from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == "GET":
        return render_template('paginaInicial.html')
    elif request.method == "POST":
        print(request.form)
        firstNumber = int(request.form['firstNumber'])
        lastNumber = int(request.form['lastNumber'])

        randomNumber = random.randrange(firstNumber, lastNumber)
        print(randomNumber)


        return render_template('paginaInicial.html', randomNumber=randomNumber)