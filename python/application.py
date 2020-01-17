from flask import Flask, render_template, request
import json
import glob
import re
import numpy as np
import pandas as pd
import time
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('list_of_images.html')

@app.route('/proc', methods=('GET', 'POST'))
def proc():
    if request.method == 'POST':
        req = request.get_json()
        print(req)
        time.sleep(1)
    return ' '.join(['{}: {}'.format(k, v) for k, v in req.items()])

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
