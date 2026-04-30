from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

# 3-Laboratoriya: Faradey effekti
@app.route('/lab3')
def lab3():
    return render_template('lab3.html')

@app.route('/lab4')
def lab4():
    return render_template('index.html')

@app.route('/lab5')
def lab5():
    return render_template('lab5.html')

@app.route('/lab6')
def lab6():
    return render_template('lab6.html')

if __name__ == '__main__':
    app.run(debug=True)