from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == "GET":
        return render_template('paginaInicial.html')
    elif request.method == "POST":
        print(request.form)
        firstNumber = request.form['firstNumber']
        lastNumber = request.form['lastNumber']

        if firstNumber == '' or lastNumber == '':
            errorMensage = "The inputs must not be empty!"
            return render_template('paginaInicial.html', errorMensage=errorMensage)

        firstNumber = int(firstNumber)
        lastNumber = int(lastNumber)

        if firstNumber > lastNumber:
            errorMensage = "The last number on the Range must be greater than the first number!"
            return render_template('paginaInicial.html', errorMensage=errorMensage)
        elif firstNumber == lastNumber:
            errorMensage = "The first number and the last number must be different!"
            return render_template('paginaInicial.html', errorMensage=errorMensage)

        randomNumber = random.randrange(firstNumber, lastNumber)
        print(randomNumber)


        return render_template('paginaInicial.html', randomNumber=randomNumber)