from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json


app = Flask(__name__)
app.secret_key = 'secret_key'

users = {
    "admin": "123456789",
    "user1": "u12345678"
}

traffic_lights = {
    "light1": "red",
    "light2": "green",
    "light3": "yellow"
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials!")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', traffic_lights=traffic_lights)

@app.route('/update-light/<light_id>/<state>', methods=['POST'])
def update_light(light_id, state):
    if light_id in traffic_lights and state in ['red', 'yellow', 'green']:
        traffic_lights[light_id] = state
        return jsonify({"success": True, "message": "Light updated successfully!"})
    return jsonify({"success": False, "message": "Invalid request!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
