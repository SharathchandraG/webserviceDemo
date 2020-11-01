from flask import Flask,jsonify, make_response
import os
import json
from flask.globals import request
import pandas as pd

fileDir = os.path.dirname(os.path.realpath(__file__))
employees_df = pd.read_csv(os.path.join(fileDir,'employeesData.csv'))

app = Flask(__name__)


@app.route('/webServiceDemo/checkAlive', methods=['GET'])    
def checkAlive():
    try:
        return make_response(jsonify(message='webServiceDemo is live'), 200)
    except Exception as eor:
        print(eor)

@app.route('/webServiceDemo/refreshData', methods=['PUT'])    
def refreshData():
    try:
        employees_df = pd.read_csv(os.path.join(fileDir,'employeesData_bkp.csv'))
        employees_df = employees_df[['Emp ID', 'First Name','Last Name',
            'Gender', 'E Mail', 'Date of Birth','Age in Yrs.', 'Date of Joining','Salary','City']]

        employees_df.to_csv(os.path.join(fileDir,'employeesData.csv'),index=False)
        employees_df = pd.read_csv(os.path.join(fileDir,'employeesData.csv'))

        return make_response(jsonify(message='Data reloaded from Backup file'), 200)
    except Exception as eor:
        print(eor)


@app.route('/webServiceDemo/getEmpByID', methods=['GET'])    
def getEmployeeByID():
    try:
        ID = request.args.get('ID','')
        return app.response_class(response=employees_df.loc[employees_df['Emp ID'] == int(ID)].to_json(orient='records'),
                                  status=200,
                                  mimetype='application/json')
    except Exception as eor:
        print(eor)
@app.route('/webServiceDemo/employees/', methods=['GET'])
def getEmployeesData():
    try:
        limit = request.args.get('limit',10)
        print('getting employees Data with limit '+str(limit))
        print(employees_df.head(int(limit)).to_json(orient='records'))
        return app.response_class(response=employees_df.head(int(limit)).to_json(orient='records'),
                                  status=200,
                                  mimetype='application/json')
    except Exception as eor:
        print(eor)


@app.route('/webServiceDemo/Employees/<ID>', methods=['PUT'])
def updateEmployeeData(ID):
    try:
        print('updating employee Data')
        
        inputJson = request.json
        
        ID = int(ID)
        
        for key in inputJson:
            if key in employees_df.columns and key != "Emp ID":
                employees_df.loc[employees_df['Emp ID'] == ID, [key]] = inputJson[key]

        employees_df.to_csv(os.path.join(fileDir,'employeesData.csv'),index=False)
        
        return app.response_class(response=employees_df.loc[employees_df['Emp ID'] == ID].to_json(orient='records'),
                                  status=200,
                                  mimetype='application/json')
    except Exception as eor:
        return app.response_class(response=json.dumps({'error':str(eor)}),
                                  status=500,
                                  mimetype='application/json')


@app.route('/webServiceDemo/deleteEmployee/', methods=['DELETE'])
def deleteEmployee():
    try:
        print('Deleting employee Data')
        ID = request.args.get('ID','')
        ID = int(ID)
        print(ID)
        delrecord = employees_df.loc[employees_df['Emp ID'] == ID].to_json(orient='records')
        # Get names of indexes for which column Stock has value No
        indexNames = employees_df[ employees_df["Emp ID"] == ID ].index
        # Delete these row indexes from dataFrame
        employees_df.drop(indexNames , inplace=True)


        employees_df.to_csv(os.path.join(fileDir,'employeesData.csv'),index=False)
        
        return app.response_class(response=delrecord if delrecord != "[]" else json.dumps({"WARNING": "record not found"}),
                                  status=200,
                                  mimetype='application/json')
    except Exception as eor:
        return app.response_class(response=json.dumps({'error':str(eor)}),
                                  status=500,
                                  mimetype='application/json')


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    print(error)
    return make_response(jsonify({'error': 'route Not found'}), 404)

if __name__=='__main__':
    print("Starting webServiceDemo App..................!")
    from flask_cors import CORS
    CORS(app)
    app.run(host="127.0.0.1", port="8001")