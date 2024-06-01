from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Simpan pengguna dalam bentuk dictionary untuk contoh ini.
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if email in users and check_password_hash(users[email]['password'], password):
        return jsonify(success=True, token='dummy-token')  # Ganti dengan token sebenarnya
    else:
        return jsonify(success=False, message='Email atau password salah.')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if email in users:
        return jsonify(success=False, message='Email sudah terdaftar.')
    else:
        users[email] = {'password': generate_password_hash(password)}

        from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Simpan pengguna dalam bentuk dictionary untuk contoh ini.
users = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if email in users and check_password_hash(users[email]['password'], password):
        print(f'User {email} berhasil login')  # Cetak log ke terminal
        return jsonify(success=True, token='dummy-token')  # Ganti dengan token sebenarnya
    else:
        return jsonify(success=False, message='Email atau password salah.')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if email in users:
        return jsonify(success=False, message='Email sudah terdaftar.')
    else:
        # Simpan pengguna baru
        hashed_password = generate_password_hash(password)
        users[email] = {'password': hashed_password}

        # Cetak email dan password (hashed) ke terminal
        print(f'Registrasi baru: {email}, Password: {password}, Password (hashed): {hashed_password}')

        return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)

     
