from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)
@app.route('/')

def api_root():
    return "Hello L Devendar Rao"

@app.route('/runo', methods=["POST"])
def api_runo_data():
    if request.headers['content-type'] == 'application/json':
        return json.dumps(request.json)
if __name__ == "__main__":
    app.run(debug=True)
