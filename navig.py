from flask import Flask, render_template, request, redirect, url_for
import handleJSON

app = Flask(__name__, template_folder = 'Templates')

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/regist')
def regist():
    return render_template('regist.html')

@app.route('/regist', methods = ['POST'])
def go():
    return handleJSON.create_file()


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def go2():
    return handleJSON.login_check()

if __name__ == '__main__':
    app.run(debug = True)
