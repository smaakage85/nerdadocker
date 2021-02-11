from flask import Flask, jsonify, request
# from importlib.metadata import version
import os
app = Flask(__name__)

# initialize model.
from NERDA.precooked import DA_ELECTRA_DA
model = DA_ELECTRA_DA()
model.load_network()

@app.route('/')
def home():
    return "NERDA prediction service"

#@app.route('/version/')
#def version():
#    return f'NERDA version: {version("NERDA")}'

@app.route('/predict/', methods=['POST'])
def predict():
    samples = request.get_json()
    text = samples.get('text')
    sentences, tags = model.predict_text(text)
    out = {'sentences': sentences, 'tags': tags}
    return jsonify(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

