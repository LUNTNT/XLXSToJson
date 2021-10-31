import pandas as pd
from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
   
    if request.method == 'POST':
        f = request.files['file']
        data_xls = pd.read_json(f, orient=)
        sheetList = data_xls.sheet_names
        isjson=json

        
        
        return data_json
    else:
        pass
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)