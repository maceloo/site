import os
from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_produtos():
    # (Seu código aqui)
    pass

@app.route('/')
def home():
    produtos = get_produtos()
    return render_template('home.html', produtos=produtos)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
