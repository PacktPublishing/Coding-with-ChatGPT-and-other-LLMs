# -*-- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:52:02 2024
@author: Vincent Hall, Build Intellect Ltd.

run this code from a simple, short file path like C:/Users/username/code/ (That's the Windows example.)
"""

from flask import Flask, render_template

#app = Flask(__name__, template_folder=os.path.abspath('C:/Users/mutan/code/Python Script/Prompt5/templates/'))
app = Flask(__name__)#, template_folder='/templates/')
print(app.template_folder)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
