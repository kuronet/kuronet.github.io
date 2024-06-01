const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');

const app = express();
app.use(bodyParser.json());

let users = {};

// Halaman utama
app.get('/', (req, res) => {
    res.send('Welcome to the home page!');
});

// Endpoint login
app.post('/login', (req, res) => {
    const { email, password } = req.body;

    if (users[email] && bcrypt.compareSync(password, users[email].password)) {
        console.log(`User ${email} berhasil login`);
        res.json({ success: true, token: 'dummy-token' }); // Ganti dengan token sebenarnya
    } else {
        res.json({ success: false, message: 'Email atau password salah.' });
    }
});

// Endpoint registrasi
app.post('/register', (req, res) => {
    const { email, password } = req.body;

    if (users[email]) {
        res.json({ success: false, message: 'Email sudah terdaftar.' });
    } else {
        const hashedPassword = bcrypt.hashSync(password, 10);
        users[email] = { password: hashedPassword };

        console.log(`Registrasi baru: ${email}, Password: ${password}, Password (hashed): ${hashedPassword}`);
        res.json({ success: true });
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server berjalan di port ${PORT}`);
});
