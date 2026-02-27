# Notely App
### Smart Note-Taking System with Markdown Support & REST API

***Notely***  is a robust Django-based application, ***engineered*** for seamless personal information management.
It combines an intuitive user interface with ***powerful organizational tools*** like dynamic tagging, categorical filtering, and real-time search.


## Key Technical Features

- ***Advanced Organization*** :  ***Implemented*** a dual-layered organization system using dynamic Categories (one-to-many) and Tags (many-to-many) for ***maximum flexibility***.
- ***Markdown Integration*** :  Custom-built template filters to render Markdown content, allowing for rich-text notes with code blocks, lists, and formatting.
- ***Search Engine*** :  ***Developed a comprehensive search logic*** that queries across titles, content, and tags simultaneously using ***Django `Q` objects***.
- ***State Management*** :  ***Added "Pinned Notes" functionality*** to keep information at the top of the dashboard using custom ordering logic.
- ***API*** :  Built with ***Django REST Framework (DRF) endpoints***, making the backend ready for future mobile or desktop client integrations.
- ***Responsive UX*** :  ***Utilizes*** Bootstrap 5 with custom CSS animations featuring with a card layout for optimal readability.


## Tech Stack

- ***Backend*** :  Python , Django
- ***Frontend*** :  JavaScript, Bootstrap 5, Markdown-it, CSS
- **Database** :  PostgreSQL ( for Production ) / SQLite ( for Development) 
- ***API*** :  Django REST Framework (DRF)


## What I Learned

- ***Complex Querysets*** :  Use a `select_related` and `prefetch_related` ***to optimize database*** hits when loading notes with categories and tags.
- ***Template Tags*** :  ***Learning how to extend Django’s template engine*** to create custom filters for Markdown processing.
- ***Design*** :  ***Focusing on "CRUD" operations*** from a UX perspective—ensuring that pinning, deleting, and editing are intuitive and fast.
- ***DRF Fundamentals*** :  ***Understanding Serializers and Viewsets*** to expose data via a secure API.


## Instructions to setup

- Clone or download the repository :
- ```bash
- git clone https://github.com/ivailoiliev89-netizen/Simple-Notely-app.git
- ***Create*** a .env file and populate it with your DB credentials (see settings.py for required keys)
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


## Usage

- ***Authentication*** :  Register a new account to keep your notes private and synced.
- ***Organization*** :  Create custom Categories and Tags via the `/admin` panel to structure your data.
- ***Markdown*** :  Write notes using standard Markdown syntax (e.g., `# Header`, `- List`) for rich-text formatting.
- ***Filtering*** :  Use the search bar or click on any Tag badge to instantly filter your collection.


## Future Improvements

- ***Auto-Save Functionality*** :  ***Implementing AJAX or Fetch API*** to save drafts automatically while typing.
- ***Reminders & Notifications*** :  ***Adding a "Reminder" field*** with Celery and Redis to send email notifications for specific notes.
- ***Collaborative Notes*** :  Allowing users to share specific notes or categories with other registered users via unique links.
- ***Dark Mode*** :  ***A native UI toggle*** for better accessibility and night-time use.

