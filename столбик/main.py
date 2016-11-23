import flask

app = flask.Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'])
def Urv():
    if flask.request.method == 'GET':
        return flask.render_template('Squared.html')
    s = flask.request.form['textt']
    ss = s.split(' ')
    return flask.render_template('Squared.html', urls=zip(ss[::2], ss[1::2]))

app.run()
