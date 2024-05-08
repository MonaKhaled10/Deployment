from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])

        payload = {
            "data": [carat, cut, color, clarity, depth, table, x, y, z]
        }

        response = requests.post("https://mega.us-east-1.modelbit.com/v1/predictedd/latest", json=payload)
        if response.status_code == 200:
            prediction = response.json()['data'][0]
            return render_template('index.html', prediction=prediction)
        else:
            return "Error: Unable to get prediction"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
