from flask import Flask, json, render_template, request, jsonify
from summaryService import summarize

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_companies():
    return render_template('summary.html')

@api.route('/summary', methods=["POST"])
def generate():
    paragraph = request.get_json()
    summary = summarize(paragraph['para'])
    data = {"summary": summary}
    response = api.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')