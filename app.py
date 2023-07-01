from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return render_template('home.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
