import flask
import os
import werkzeug

app = flask.Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'])
def Galerey():
    if flask.request.method == 'GET':
        directory = 'static'
        files = os.listdir(directory)
        return flask.render_template('Galerey.html', fileslist=files)
    try:
        fs = flask.request.files['image']
        fs.save('static/' + werkzeug.secure_filename(fs.filename))
    except ValueError:
        return flask.render_template('Galerey.html', error="Ошибки!")
    return flask.redirect('/')


app.run()
