# Django Feedback Forms

A feedback collection web application built with Django. Users can submit feedback through a validated form, and submissions are stored in a database and manageable via the Django admin panel.

This project is **MP2** of a structured Django learning roadmap, focused on Django's form system and validation lifecycle.

---

## Features

- Submit feedback with name, email, topic, message, and a 1–5 rating
- Server-side form validation with Django ModelForm
- Custom validators for business rules (minimum name and message length)
- POST / Redirect / GET pattern to prevent duplicate submissions
- CSRF protection on all form submissions
- Django admin integration for managing feedback entries
- Clean, minimal UI with no external CSS frameworks

---

## Tech Stack

- **Python 3.13.7**
- **Django 6.0**
- **SQLite** (default development database)
- HTML / CSS (no frameworks)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/django-feedback-forms.git
cd django-feedback-forms
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply migrations

```bash
cd feedback_project
python manage.py migrate
```

### 5. Create a superuser (optional — for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open your browser and navigate to:

| URL | Description |
|---|---|
| `http://127.0.0.1:8000/feedback/` | Feedback form |
| `http://127.0.0.1:8000/feedback/success/` | Success page |
| `http://127.0.0.1:8000/admin/` | Admin panel |

---

## Project Structure

```
feedback_project/
├── manage.py
├── feedback_project/          # Project configuration
│   ├── settings.py
│   └── urls.py
└── feedback/                  # Feedback application
    ├── models.py              # FeedbackEntry model
    ├── forms.py               # ModelForm + custom validators
    ├── views.py               # GET / POST view logic
    ├── urls.py                # App-level URL patterns
    ├── admin.py               # Admin panel configuration
    └── templates/
        └── feedback/
            ├── form.html      # Feedback form page
            └── success.html   # Submission success page
```

---

## Key Concepts Learned

| Concept | Description |
|---|---|
| `ModelForm` | Automatically generates form fields from a Django model |
| `form.is_valid()` | Triggers Django's full validation pipeline |
| `cleaned_data` | Dictionary of validated field values, populated after `is_valid()` |
| `clean_<field>()` | Custom validator methods called automatically during validation |
| POST / Redirect / GET | Redirect after successful form submission to prevent duplicate POST on refresh |
| `{% csrf_token %}` | Django template tag that adds a CSRF security token to forms |
| `auto_now_add=True` | Automatically sets a timestamp field when a record is created |
| `choices` | Restricts a field to a predefined set of values |

---

## How Validation Works

```
User submits form (POST)
        ↓
FeedbackForm(request.POST)
        ↓
form.is_valid()
        ↓
Step 1: Field-level validation (EmailField, max_length, required)
        ↓
Step 2: cleaned_data is populated
        ↓
Step 3: clean_<field>() methods run (custom rules)
        ↓
Pass → form.save() → redirect to success page
Fail → re-render form with error messages
```

---

## License

This project is for educational purposes.
