import flask
from datetime import datetime
from math import sqrt

app = flask.Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'])
def Urv():
    if flask.request.method == 'GET':
        return flask.render_template('Squared.html')
    else:
        try:
            a = float(flask.request.form['a'])
            b = float(flask.request.form['b'])
            c = float(flask.request.form['c'])
        except ValueError:
            return flask.render_template('Squared.html', error="Ошибки! Проверьте введёные данные!")
        D = b**2 - 4*a*c
        No_Error = 1
        if D >= 0:
            x1 = (-b + sqrt(D))/(2*a)
            x2 = (-b - sqrt(D))/(2*a)
        else:
            x1 = str(-b/(2*a)) + ' + i*' + str(sqrt(-D)/(2*a))
            x2 = str(-b/(2*a)) + ' - i*' + str(sqrt(-D)/(2*a))
        return flask.render_template('Squared.html', result=No_Error, otvet1=str(x1), otvet2=str(x2))


app.run()