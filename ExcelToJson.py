import os
import pandas as pd
from flask import Flask, json, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
   
    if request.method == 'POST':
        f = request.files['file']
        data_xls = pd.ExcelFile(f)
        sheetList = data_xls.sheet_names
        isjson=json
        ans={}
        
        for x in sheetList:
            wb = pd.read_excel(f, sheet_name=x)
            isjson= wb.to_json(orient= 'records')
            ans[x] = json.loads(isjson)
                       
        return ans
    else:
        pass
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)