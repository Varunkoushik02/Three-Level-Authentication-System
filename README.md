# Three-Level-Authentication-System

A secure web-based authentication system that verifies a user's identity using **three levels of verification**:
1. **Username & Password**
2. **OTP Verification (Email/SMS)**
3. **Pattern-Based Authentication**


🚀 Features

- 🔑 Traditional login (username & password)
- 📲 OTP verification via email or phone
- 🧩 Custom pattern-based final authentication step
- 🔐 Enhanced multi-layer security
- 🧠 Designed for educational & demo purposes


 🛠️ Technologies Used

 Frontend: HTML, CSS
 Backend: Python (Flask)
 Database: MySQL (via MySQL Workbench)
 Email/OTP: `smtplib` (for email), `random` (for OTP)
 Pattern Auth: Matrix-based logic (custom UI or form logic)



 📁 Folder Structure




Three-level-Auth

* static – Contains static files (CSS, images)
* templates – HTML pages (`login.html`, `otp.html`, etc.)
* app.py – Core Flask logic
* database.sql – MySQL table schema
  







 🧪 How to Run the Project Locally

1. Clone the repo:
```bash
git clone https://github.com/yourusername/Three-Level-Authentication-System.git
````

2. Navigate to the project folder:

```bash
cd Three-Level-Authentication-System
```

3. Install required Python packages:

```bash
pip install flask mysql-connector-python
```

4. Set up your database using `database.sql`

5. Run the app:

```bash
python app.py
```

6. Open `http://localhost:5000` in your browser

---

💡 Future Improvements

* OTP via SMS (Twilio API)
* Add CAPTCHA in login
* Use JWT or session management
* Deployment to cloud (e.g., Vercel, Heroku, etc.)



 🙋‍♂️ Author

Varunkoushik02
GitHub: [@Varunkoushik02](https://github.com/Varunkoushik02)
