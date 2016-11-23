import flask
import sqlite3

app = flask.Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')
    else:
        url1 = str(flask.request.form['Url'])
        if url1 == '':
            return flask.render_template('index.html', error='Пустая сылка!!')
        conn = sqlite3.connect('bd.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        try:
            c.execute('''INSERT INTO urls (link) VALUES (?)''', [url1])
            conn.commit()
        except sqlite3.Error:
            pass
        try:
            ur = c.execute('SELECT id FROM urls WHERE link=:ur', {"ur": url1}).fetchone()[0]
        except sqlite3.Error:
            return flask.render_template('index.html', error='ошибка поиска')
        return flask.render_template('index.html', result='http://127.0.0.1:5000/ss/' + str(ur))


@app.route('/ss/<int:uid>', methods=['GET'])
def redir(uid):
    conn = sqlite3.connect('bd.db')
    c = conn.cursor()
    ur = c.execute('SELECT link FROM urls WHERE id=:id', {"id": uid}).fetchone()[0]
    if ur == '':
        return flask.abort(404)
    return flask.redirect('http://' + ur)


if __name__ == '__main__':
    app.run()
