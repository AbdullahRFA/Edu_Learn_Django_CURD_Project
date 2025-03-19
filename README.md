# Edu Learn - Django CRUD Project 🏫📚  

A **course management system** built with **Django** that allows users to manage courses, lessons, and student enrollments. The system includes user authentication, password reset functionality via email (OTP-based), and role-based access control.

---

## 📌 Features  
### 1️⃣ Authentication & Authorization  
- User **registration, login, and logout** functionality.  
- **Password change and reset** using OTP verification via email.  
- **Role-based access control** (Admin & Student).  
- Profile management (Update user information).  

### 2️⃣ Course & Lesson Management  
- **CRUD operations** for courses and lessons.  
- Course descriptions, thumbnails, and durations.  
- Enroll students in courses.  
- View students enrolled in a specific course.  
- View lessons under a course.  

### 3️⃣ Student Management  
- Add new students & manage existing ones.  
- View individual student details.  
- Delete or update student information.  

### 4️⃣ Additional Functionalities  
- **Bootstrap-based responsive UI.**  
- **Django Messages Framework** for alerts.  
- **Custom forms with validation.**  
- **Admin Panel Access** for superusers.  

---

## 🛠️ Technologies Used  
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (can be configured to PostgreSQL/MySQL)  
- **Authentication**: Django Authentication System  
- **Email Service**: SMTP (Google App Password for OTP)  
- **UI Components**: Bootstrap 5, FontAwesome Icons  

---

## 🚀 Installation & Setup  

### 🔹 Step 1: Clone the Repository  
```sh
git clone https://github.com/yourusername/Edu_Learn_Django_CURD_Project.git
cd Edu_Learn_Django_CURD_Project
```

### 🔹 Step 2: Create & Activate Virtual Environment

``` sh python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux

(For Windows, use: venv\Scripts\activate)
```

### 🔹 Step 3: Install Dependencies

    pip install -r requirements.txt

### 🔹 Step 4: Configure Environment Variables

    Create a .env file in the project root directory and add:
```sh
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
SECRET_KEY=your-django-secret-key
```

### 🔹 Step 5: Apply Migrations & Create Superuser

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

(Follow the prompts to create an admin user.)

### 🔹 Step 6: Run the Server

    python manage.py runserver

Then open http://127.0.0.1:8000/ in your browser.

---

### 📂 Project Structure
```sh
Edu_Learn_Django_CURD_Project/
│── Course_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/Course_app/
│   │   ├── base.html
│   │   ├── course_list.html
│   │   ├── course_details.html
│   │   ├── student_list.html
│   │   ├── lesson_list.html
│   │   ├── user_profile.html
│   │   ├── change_password.html
│   │   ├── forgot_password.html
│   │   ├── password_change_complete.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│── EduLearn/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── .env
│── .gitignore
│── manage.py
│── README.md
│── requirements.txt

```
---

<div class="container mt-5">
    <h2 class="text-center text-primary mb-4">📌 API Endpoints & URLs</h2>

<div class="table-responsive">
        <table class="table table-bordered table-hover text-center">
            <thead class="table-dark">
                <tr>
                    <th>Feature</th>
                    <th>URL</th>
                    <th>Method</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>User Registration</td>
                    <td><code>/register_user/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Login</td>
                    <td><code>/login_user/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Logout</td>
                    <td><code>/logout_user/</code></td>
                    <td><span class="badge bg-success">GET</span></td>
                </tr>
                <tr>
                    <td>Change Password</td>
                    <td><code>/change_password/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Forgot Password</td>
                    <td><code>/forgot_password/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Reset Password</td>
                    <td><code>/reset_password/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Courses List</td>
                    <td><code>/course_list/</code></td>
                    <td><span class="badge bg-success">GET</span></td>
                </tr>
                <tr>
                    <td>Create Course</td>
                    <td><code>/create_course/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Edit Course</td>
                    <td><code>/course_edit/&lt;id&gt;/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Delete Course</td>
                    <td><code>/course_delete/&lt;id&gt;/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Create Lesson</td>
                    <td><code>/create_lesson/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Edit Lesson</td>
                    <td><code>/lesson_edit/&lt;id&gt;/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Delete Lesson</td>
                    <td><code>/lesson_delete/&lt;id&gt;/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Enroll Student</td>
                    <td><code>/Enroll_student/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>View Student</td>
                    <td><code>/student_list/</code></td>
                    <td><span class="badge bg-success">GET</span></td>
                </tr>
                <tr>
                    <td>Update Student</td>
                    <td><code>/update_student/&lt;id&gt;/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>Delete Student</td>
                    <td><code>/delete_student/&lt;id&gt;/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
                <tr>
                    <td>User Profile</td>
                    <td><code>/user_profile/</code></td>
                    <td><span class="badge bg-success">GET</span></td>
                </tr>
                <tr>
                    <td>Update Profile</td>
                    <td><code>/update_profile/</code></td>
                    <td><span class="badge bg-primary">POST</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

---

### 📧 Email Setup (SMTP for OTP)

1. Enable 2-Step Verification on your Google Account.
2.	Generate an App Password from Google:
    - Go to 👉 Google App Passwords
	- Select “Mail” and “Other” (Custom name).
	- Copy the generated password.
3.	Add it to your .env file:
```sh
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```


---

### 🔒 Role-Based Access Control
```sh
Role -> Permissions
Admin -> Can add, edit, delete courses, lessons, and students
Student -> Can only view enrolled courses and lessons
```


---

### 📸 Screenshots

🔹 Home Page

🔹 Course Management

🔹 User Registration & Login

🔹 Password Reset

---

### 📝 Contributing
1. Fork the repo.
2. Clone it to your local machine.
3. Create a new branch:

        git checkout -b feature-name


4. Make your changes and commit:

        git commit -m "Added new feature"


5. Push to your branch:

        git push origin feature-name


6. Submit a Pull Request.

---

### 📄 License

This project is licensed under the MIT License.

---

### 💬 Contact

- 👤 Abdullah Nazmus-Sakib
- 📧 Email: your-email@example.com
- 🌐 Website: yourwebsite.com
- 📌 GitHub: AbdullahRFA

---

# 🚀 Happy Coding! 🎉
