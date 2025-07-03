from flask import Flask, render_template, request, redirect, url_for, session
import random
import smtplib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

SENDER_EMAIL = 'gundlapallivarunkoushik05@gmail.com'
SENDER_PASSWORD = 'gexj nmks jerm lezk'  

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        
        if username == 'testuser' and password == 'pass123':
            session['user'] = username
            session['email'] = email
            return redirect(url_for('otp'))
        else:
            return "Invalid username or password ❌"

    return render_template('login.html')

@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        entered_otp = request.form['otp']
        if entered_otp == session.get('otp'):
            return redirect(url_for('pattern'))
        else:
            return "Invalid OTP ❌"

    
    otp_code = str(random.randint(100000, 999999))
    session['otp'] = otp_code

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            subject = 'Your OTP Code'
            body = f'Your OTP is: {otp_code}'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail(SENDER_EMAIL, session['email'], msg)
        print(f"OTP sent to {session['email']} ✅")
    except Exception as e:
        print(f"Failed to send OTP: {e}")

    return render_template('otp.html')

@app.route('/pattern', methods=['GET', 'POST'])
def pattern():
    if 'user' not in session:
        return redirect(url_for('login'))

    correct_pattern = "14789"  

    if request.method == 'POST':
        user_pattern = request.form['pattern']
        if user_pattern == correct_pattern:
            return render_template('success.html')
        else:
            return "Invalid pattern ❌ Access Denied!"

    return render_template('pattern.html')

if __name__ == '__main__':
    app.run(debug=True)
