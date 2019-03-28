from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/check', methods=['GET'])
def check():
    email = request.args.get("email")
    r = requests.get("https://my-candidate-bonque.jmgapi.com/api/v1/Account/StatusCandidate?email=" + email)
    return(r.text)


if __name__ == '__main__':
    app.run()