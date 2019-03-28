from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/check', methods=['GET'])
@cross_origin()
def check():
    email = request.args.get("email")
    r = requests.get("https://my-candidate-bonque.jmgapi.com/api/v1/Account/StatusCandidate?email=" + email)
    return(r.text)


if __name__ == '__main__':
    app.run()