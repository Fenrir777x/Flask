from flask import Flask, render_template
import csv
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_lab.html',titolo="Benvenuto")

@app.route('/musica')
def music():
    with open ('templates/music.csv','r',encoding='utf-8') as f:
        lett=csv.reader(f)
        next(lett)
        music=list(lett)
    return render_template('musica.html',music=music)

@app.route('/film')
def film():
    with open('templates/film.csv','r',encoding='Utf-8') as f:
        lett=csv.reader(f)
        next(lett)
        film=list(lett)
    return render_template('film.html',film=film)

@app.route('/libri')
def libri():
    with open('templates/book.csv','r',encoding='utf-8') as f:
        lett=csv.reader(f)
        next(lett)
        libri=list(lett)
    return render_template('libri.html',libri=libri)

if __name__ == '__main__':
    app.run(debug=True)