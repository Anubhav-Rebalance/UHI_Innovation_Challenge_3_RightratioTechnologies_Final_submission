import requests
import json
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

NGROCK_URL = 'http://8150-35-240-177-180.ngrok.io/'


@app.route("/predict")
def medical_triage_prediction():
    text = request.args.get("text")

    URL = NGROCK_URL + 'predict'

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'text':text}
      
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
      
    # extracting data in json format
    data = r.json()

    # print(json.loads(r.content))
    # print(type(json.loads(r.content)))
    print(data)
    # print(type(eval(data)))

    return jsonify(data)

@app.route("/icd10-codes")
def get_icd10_code_list():

    URL = NGROCK_URL + 'icd10-codes'

    # sending get request and saving the response as response object
    r = requests.get(url = URL)
      
    # extracting data in json format
    data = r.json()

    # print(json.loads(r.content))
    # print(type(json.loads(r.content)))
    print(data)
    # print(type(eval(data)))

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/symptoms")
def get_symptoms():

    URL = NGROCK_URL + 'symptoms'
      
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
      
    # extracting data in json format
    data = r.json()

    return jsonify(data)

@app.route("/latest-symptoms")
def get_patients_symptoms():

    URL = NGROCK_URL + 'latest-symptoms'

    # sending get request and saving the response as response object
    r = requests.get(url = URL)
      
    # extracting data in json format
    data = r.json()

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/save-symptoms", methods=['POST'])
def save_patients_symptoms():

    URL = NGROCK_URL + 'save-symptoms'

    # defining a params dict for the parameters to be sent to the API
    # PARAMS = {'text':text}
      
    # sending get request and saving the response as response object
    r = requests.post(url = URL, json=request.get_json(force=True))
      
    return jsonify("Success")


if __name__ == '__main__':
    app.run()  # If address is in use, may need to terminate other sessions:
               # Runtime > Manage Sessions > Terminate Other Sessions