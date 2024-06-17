# -*-- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:52:02 2024
@author: Vincent Hall, Build Intellect Ltd.
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='G:\.shortcut-targets-by-id\0B9NZZ3j6kD37Uy1NVFhfcmJpemc\Business GD build\Packt\The Book Coding with ChatGPT and other LLMs\code\Chapter 3\Prompt5\templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
