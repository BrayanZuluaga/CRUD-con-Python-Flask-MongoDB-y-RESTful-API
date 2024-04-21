from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from user import Users

db = dbase.dbConnection()

app = Flask(__name__)

#Application Routes
#Home
@app.route('/')
def home():
    users = db['users']
    usersReceived = users.find()
    return render_template('index.html', users = usersReceived)

#Method Get
@app.route('/viewU', methods=['GET'])
def viewU():
    users = db['users']
    usersReceived = users.find()

    if request.headers.get('Accept') == 'application/JSON':
        # Si la solicitud es de tipo JSON, devuelve los datos en formato JSON
        user_data = []
        for user in usersReceived:
            user_data.append({
                'name': user['name'],
                'years': user['years'],
                'cc': user['cc']
            })
        return jsonify(users=user_data)
    else:
        # De lo contrario, renderiza la plantilla views.html con los datos
        return render_template('views.html', users=usersReceived)

#Method Post
@app.route('/users', methods=['POST', 'PUT'])
def addUser():
    users = db['users']
    name = request.form['name']
    cc = request.form['cc']
    years = request.form['years']

    if name and cc and years:
        user = Users(name, cc, years)
        users.insert_one(user.toDBCollection())
        response = jsonify({
            'name' : name,
            'cc' : cc,
            'years' : years
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method Delete
@app.route('/delete/<string:user_name>', methods=['DELETE'])
def delete(user_name):
    users = db['users']
    users.delete_one({'name' : user_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:user_name>', methods=['POST', 'PUT'])
def edit(user_name):
    users = db['users']
    name = request.form['name']
    cc = request.form['cc']
    years = request.form['years']

    if name and cc and years:
        users.update_one({'name' : user_name}, {'$set' : {'name' : name, 'cc' : cc, 'years' : years}})
        response = jsonify({'message' : 'User ' + user_name + ' updated successfully'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(505)
def notFound(error=None):
    message ={
        'message': 'Not Found ' + request.url,
        'status': '505 Not Found'
    }
    response = jsonify(message)
    response.status_code = 505
    return response



if __name__ == '__main__':
    app.run(debug=True, port=9000)