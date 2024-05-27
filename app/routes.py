from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/k1')
def ksiega1():
    return render_template('k1.html')

@app.route('/k2')
def ksiega2():
    return render_template('k2.html')

@app.route('/k3')
def ksiega3():
    return render_template('k3.html')

@app.route('/k4')
def ksiega4():
    return render_template('k4.html')

@app.route('/k5')
def ksiega5():
    return render_template('k5.html')

@app.route('/k6')
def ksiega6():
    return render_template('k6.html')

@app.route('/k7')
def ksiega7():
    return render_template('k7.html')

@app.route('/k8')
def ksiega8():
    return render_template('k8.html')

@app.route('/k9')
def ksiega9():
    return render_template('k9.html')

@app.route('/k10')
def ksiega10():
    return render_template('k10.html')

@app.route('/k11')
def ksiega11():
    return render_template('k11.html')

@app.route('/k12')
def ksiega12():
    return render_template('k12.html')