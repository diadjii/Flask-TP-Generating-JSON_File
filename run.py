import os
import json

from flask import Flask, request, render_template, redirect,url_for


app = Flask(__name__)
data = []

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, 'static', 'data.json')

def get_user_list():
    with open(json_url) as json_file:
        return json.load(json_file)

def save_data(d):
    data = get_user_list()

    with open(json_url,'w') as json_file:
        data["people"].append(d)

        json.dump(data, json_file, indent=2)

        return "Success !!!"

def find_people_by_name(name):
    peoples = get_user_list()

    for people in peoples['people']:
        if people['name'].strip() == name.strip():
            return people

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def users():
    people = get_user_list()

    return render_template('users_list.html.j2',peoples=people['people'])

@app.route('/user/<name>/edit', methods=['GET', 'POST'])
def edit(name):
    selected_people = {}
    people = find_people_by_name(name)

    if request.method == 'GET':
        return render_template('user_edit.html.j2',people=people)
    else:
        new_name = request.form['name']
        new_age = request.form['age']
        new_country = request.form['country']

        peoples = get_user_list()

        for p in peoples['people']:
            if p['name'].strip() == people['name'].strip():
                p['name'] = new_name
                p['age'] = new_age
                p['country'] = new_country

        with open(json_url,'w') as json_file:
            json.dump(peoples, json_file, indent=2)

            return redirect(url_for('users'))

@app.route('/ajouter', methods=['POST',])
def ajouter():
    name = request.form['fullname']
    age = request.form['age']
    country = request.form['country']

    infos = {'name':name,'age':age, 'country':country}

    return save_data(infos)

if __name__ == "__main__":
    app.run(debug=True)
