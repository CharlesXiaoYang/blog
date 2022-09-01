from flask import Flask, render_template
from flask import escape
from flask import url_for


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


# @app.route('/user/<name>')
# def user_page(name):
#     return f'User: {escape(name)}'



if __name__ == '__main__':
    app.run()