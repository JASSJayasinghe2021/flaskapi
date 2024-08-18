from flask import Flask, render_template, jsonify

app = Flask(__name__)
COUNTRIES = [
        {"id":1, "title":"Sri Lank"},
        {"id":2, "title":"India"},
        {"id":3, "title":"Pakistan"}
        ]

@app.route("/")
def hello_world():
    return render_template('index.html', countries=COUNTRIES)

@app.route("/countries")
def get_countries():
    return jsonify(COUNTRIES)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)