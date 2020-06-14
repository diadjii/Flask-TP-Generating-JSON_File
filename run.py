import os

from flask import Flask, request, render_template


app = Flask(__name__)
data = []

def save_data(d):
    import json
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'data.json')

    with open(json_url) as json_file:
        data = json.load(json_file)

    with open(json_url,'w') as json_file:
        # data = json.load(json_file)
        data["people"].append(d)
        # json_file.write(str(data))
        json.dump(data, json_file, indent=2)

        return "ok"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter', methods=['POST',])
def ajouter():
    name = request.form['fullname']
    age = request.form['age']
    country = request.form['country']
    infos = {'name':name,'age':age, 'country':country}

    return save_data(infos)

if __name__ == "__main__":
    app.run(debug=True)
