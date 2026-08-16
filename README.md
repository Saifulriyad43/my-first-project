# my-first-project


# 🥗 Django Calorie Calculator

A simple Django-based **Calorie & BMR Calculator** that allows users to create a personal calorie profile and calculate their **Basal Metabolic Rate (BMR)** and estimated **daily calorie requirements** based on age, gender, weight, and height.

## 🚀 Features

* 🔐 User-based calorie profiles
* 👤 One-to-one profile relationship with Django's built-in `User` model
* ⚖️ Weight input in kilograms
* 📏 Height input in centimeters
* 🎂 Age-based calculation
* 🚻 Gender-based BMR calculation
* 🔥 BMR calculation
* 🍽️ Daily calorie requirement calculation
* 🗄️ Django ORM database integration
* 🛡️ Built-in Django authentication support

## 🛠️ Technologies Used

* **Python**
* **Django**
* **Django ORM**
* **SQLite** / PostgreSQL
* **HTML, CSS, JavaScript** *(if frontend is added)*

## 📂 Project Structure

```text
calorie-calculator/
│
├── manage.py
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── calorie/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── templates/
│
├── static/
│
├── db.sqlite3
└── README.md
```

## 🧩 Model

The main model is `CalorieProfile`.

```python
class CalorieProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.FloatField(help_text="Weight in kilograms")
    height_cm = models.FloatField(help_text="Height in centimeters")

    bmr = models.FloatField(default=0)
    daily_calories = models.FloatField(default=0)
```

### Field Explanation

| Field            | Description                             |
| ---------------- | --------------------------------------- |
| `user`           | Connects the profile with a Django user |
| `name`           | User's name                             |
| `age`            | User's age                              |
| `gender`         | Male/Female                             |
| `weight`         | Weight in kilograms                     |
| `height_cm`      | Height in centimeters                   |
| `bmr`            | Calculated Basal Metabolic Rate         |
| `daily_calories` | Estimated daily calorie requirement     |

## 🧮 BMR Calculation

The application can use the **Mifflin-St Jeor equation**.

### Male

```text
BMR = (10 × weight) + (6.25 × height) - (5 × age) + 5
```

### Female

```text
BMR = (10 × weight) + (6.25 × height) - (5 × age) - 161
```

Where:

* Weight = kilograms
* Height = centimeters
* Age = years

## 🍽️ Daily Calorie Calculation

Daily calorie requirements can be estimated by multiplying BMR by an activity factor.

```text
Daily Calories = BMR × Activity Factor
```

Example activity factors:

| Activity Level    | Factor |
| ----------------- | -----: |
| Sedentary         |    1.2 |
| Lightly Active    |  1.375 |
| Moderately Active |   1.55 |
| Very Active       |  1.725 |
| Extremely Active  |    1.9 |

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/calorie-calculator.git
```

### 2. Go to the project directory

```bash
cd calorie-calculator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔑 Django Admin

You can manage calorie profiles through the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

## 🔮 Future Improvements

* [ ] User registration and login
* [ ] Activity-level selection
* [ ] BMI calculator
* [ ] Calorie deficit/surplus calculator
* [ ] Meal planning
* [ ] Weight tracking
* [ ] Progress charts
* [ ] REST API using Django REST Framework
* [ ] PostgreSQL database
* [ ] Responsive frontend
* [ ] Docker support
* [ ] API authentication with JWT

## 🎯 Learning Objectives

This project is useful for practicing:

* Django Models
* Django ORM
* Model relationships
* One-to-One relationships
* Django Authentication
* Forms
* Views
* Templates
* CRUD operations
* Database migrations
* Business logic in Django

## 📌 Disclaimer

This calculator provides **general estimates** and should not be considered medical or nutritional advice. Individual calorie requirements can vary depending on many factors.

## 👨‍💻 Author

**Your Name**

* GitHub: `https://github.com/yourusername`
* LinkedIn: `https://linkedin.com/in/yourprofile`

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
