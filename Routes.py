import model
import pandas as pd
import requests
from flask import Flask, json, render_template, request, jsonify



app = Flask(__name__)

@app.route('/users', methods=['POST', 'GET'])
def users():
   
    if request.method == 'POST':
        f = request.files['file']
        #data_xls = pd.ExcelFile(f)
        #sheetList = data_xls.sheet_names
        isjson=json
        
        #for x in sheetList:
        #    wb = pd.read_excel(f, sheet_name=x)
        #    isjson= wb.to_json(orient= 'records')
        #    ans = json.loads(isjson)

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)
        
    try:   
        r = requests.post("https://mf-api-user-sj8ek.ondigitalocean.app/mf-2/api/users/addMany", headers=model.post_header, data = json.dumps(ans))
        print(r.status_code)
        print(r.text)
        
        return jsonify(ans)
         
    except:
        return render_template('index.html')
    
@app.route('/customers', methods=['POST', 'GET'])
def customers():
   
    if request.method == 'POST':
        f = request.files['file']
        #data_xls = pd.ExcelFile(f)
        #sheetList = data_xls.sheet_names
        isjson=json
        
        #for x in sheetList:
        #    wb = pd.read_excel(f, sheet_name=x)
        #    isjson= wb.to_json(orient= 'records')
        #    ans[x] = json.loads(isjson)

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)
        
    
    try:                   
        postr = requests.post("https://mf-api-customer-nccrp.ondigitalocean.app/api/customers/addMany", headers=model.post_header, data = json.dumps(ans))
        print(postr)
        print(postr.text)
        getr = requests.get("https://mf-api-customer-nccrp.ondigitalocean.app/api/customers/addMany", headers=model.get_header)
        print(getr)
        print(getr.text)
        return jsonify(ans)
    except:
        return render_template('index.html')

@app.route('/tags', methods=['POST', 'GET'])
def tags():
    if request.method == 'POST':
        f = request.files['file']
        #data_xls = pd.ExcelFile(f)
        #sheetList = data_xls.sheet_names
        isjson=json
        #ans={}
        
        #for x in sheetList:
        #    wb = pd.read_excel(f, sheet_name=x)
        #    isjson= wb.to_json(orient= 'records')
        #    ans[x] = json.loads(isjson)

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)

    try:   
        r = requests.put("https://mf-api-user-sj8ek.ondigitalocean.app/mf-2/api/users/addMany", headers=model.post_header, data = json.dumps(ans))
        print(r)
        print(r.text)
        return jsonify(ans)
         
    except:
        return render_template('index.html')

@app.route('/roles', methods=['POST', 'GET'])
def roles():
    
    if request.method == 'POST':
        f = request.files['file']
        #data_xls = pd.ExcelFile(f)
        #sheetList = data_xls.sheet_names
        isjson=json
        #ans={}
        
        #for x in sheetList:
        #    wb = pd.read_excel(f, sheet_name=x)
        #    isjson= wb.to_json(orient= 'records')
        #    ans[x] = json.loads(isjson)

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)

    try:   
        r = requests.put("https://mf-api-user-sj8ek.ondigitalocean.app/mf-2/api/users/addMany", headers=model.post_header, data = json.dumps(ans))
        print(r)
        print(r.text)
        return jsonify(ans)
         
    except:
        return render_template('index.html')

@app.route('/rules', methods=['POST', 'GET'])
def rules():
    
    if request.method == 'POST':
        f = request.files['file']
        #data_xls = pd.ExcelFile(f)
        #sheetList = data_xls.sheet_names
        isjson=json
        #ans={}
        
        #for x in sheetList:
        #    wb = pd.read_excel(f, sheet_name=x)
        #    isjson= wb.to_json(orient= 'records')
        #    ans[x] = json.loads(isjson)

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)

    try:   
        r = requests.post("https://mf-api-user-sj8ek.ondigitalocean.app/mf-2/api/users/addMany", headers=model.post_header, data = json.dumps(ans))
        print(r)
        print(r.text)
        return jsonify(ans)
         
    except:
        return render_template('index.html')

@app.route('/flows', methods=['POST', 'GET'])
def flows():
    
    if request.method == 'POST':
        f = request.files['file']
        #data_xls = pd.ExcelFile(f)
        #sheetList = data_xls.sheet_names
        isjson=json
        #ans={}
        
        #for x in sheetList:
        #    wb = pd.read_excel(f, sheet_name=x)
        #    isjson= wb.to_json(orient= 'records')
        #    ans[x] = json.loads(isjson)

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)

    try:   
        r = requests.post("https://mf-api-user-sj8ek.ondigitalocean.app/mf-2/api/users/addMany", headers=model.post_header, data = json.dumps(ans))
        print(r)
        print(r.text)
        return jsonify(ans)
         
    except:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)