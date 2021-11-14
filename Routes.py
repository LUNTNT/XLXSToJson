import model
import pandas as pd
import requests
import jsonschema
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
            jsonschema.validate(instance=ans, schema=model.UserSchema)
        except jsonschema.ValidationError as err:
            return "Input Is invaild"
        
        
    try:   
        r = requests.post(model.UserPost, headers=model.post_header, data = json.dumps(ans))
        print(r.status_code)
        print(r.text)
        
        return jsonify(ans)
        
    except r.status_code > 300:    
        return jsonify({"Status" : str(r.status_code) + r.text, "Data" : ans})
         
    finally:
        return render_template('index.html')
    
@app.route('/customers', methods=['POST', 'GET'])
def customers():
   
    if request.method == 'POST':
        f = request.files['file']
        isjson=json

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)
        
        try: 
            jsonschema.validate(instance=ans, schema=model.CustomerSchema)
        except jsonschema.ValidationError as err:
            return "Input Is invaild"
        
    
    try:                   
        postr = requests.post(model.CustomerPost, headers=model.post_header, data = json.dumps(ans))
        print(postr, postr.text)
        getr = requests.get(model.CustomerGet, headers=model.get_header)
        print(getr, getr.text)
        return jsonify(ans)
    
    except postr.status_code > 300:    
        return jsonify({"Post Status" : str(postr.status_code) + postr.text, "Data" : ans})
    
    except getr.status_code > 300:    
        return jsonify({"Get Status" : str(getr.status_code) + getr.text, "Data" : ans})
    
    finally:
        return render_template('index.html')
    
@app.route('/tags', methods=['POST', 'GET'])
def tags():
    if request.method == 'POST':
        f = request.files['file']
        isjson=json

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)
        
        try: 
            jsonschema.validate(instance=ans, schema=model.TagSchema)
        except jsonschema.ValidationError as err:
            return "Input Is invaild"

    try:   
        r = requests.put(model.TagPut, headers=model.post_header, data = json.dumps(ans))
        print(r.status_code)
        print(r.text)
        
        return jsonify(ans)
        
    except r.status_code > 300:    
        return jsonify({"Status" : str(r.status_code) + r.text, "Data" : ans})
         
    finally:
        return render_template('index.html')

@app.route('/roles', methods=['POST', 'GET'])
def roles():
    
    if request.method == 'POST':
        f = request.files['file']
        isjson=json

        wb = pd.read_excel(f)
        isjson= wb.to_json(orient= 'records')
        ans = json.loads(isjson)
        
        try: 
            jsonschema.validate(instance=ans, schema=model.RoleSchema)
        except jsonschema.ValidationError as err:
            return "Input Is invaild"

    try:   
        r = requests.put(model.RolePut, headers=model.post_header, data = json.dumps(ans))
        print(r.status_code)
        print(r.text)
        
        return jsonify(ans)
        
    except r.status_code > 300:    
        return jsonify({"Status" : str(r.status_code) + r.text, "Data" : ans})
         
    finally:
        return render_template('index.html')

# @app.route('/rules', methods=['POST', 'GET'])
# def rules():
    
#     if request.method == 'POST':
#         f = request.files['file']
#         isjson=json

#         wb = pd.read_excel(f)
#         isjson= wb.to_json(orient= 'records')
#         ans = json.loads(isjson)

#         try: 
#             jsonschema.validate(instance=ans, schema=model.RuleSchema)
#         except jsonschema.ValidationError as err:
#             return "Input Is invaild"

#     try:   
#         r = requests.post(model.RulePost, headers=model.post_header, data = json.dumps(ans))
#         print(r.status_code)
#         print(r.text)
        
#         return jsonify(ans)
        
#     except r.status_code > 300:    
#         return jsonify({"Status" : str(r.status_code) + r.text, "Data" : ans})
         
#     finally:
#         return render_template('index.html')

# @app.route('/flows', methods=['POST', 'GET'])
# def flows():
    
#     if request.method == 'POST':
#         f = request.files['file']
#         isjson=json

#         wb = pd.read_excel(f)
#         isjson= wb.to_json(orient= 'records')
#         ans = json.loads(isjson)

#         try: 
#             jsonschema.validate(instance=ans, schema=model.FlowSchema)
#         except jsonschema.ValidationError as err:
#             return "Input Is invaild"

#     try:   
#         r = requests.post(model.FlowPost, headers=model.post_header, data = json.dumps(ans))
#         print(r.status_code)
#         print(r.text)
        
#         return jsonify(ans)
        
#     except r.status_code > 300:    
#         return jsonify({"Status" : str(r.status_code) + r.text, "Data" : ans})
         
#     finally:
#         return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)