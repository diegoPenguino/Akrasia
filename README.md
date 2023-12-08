## To-Do app Akrasia
Built with Django, Boootstrap5, jQuery, and SQLite3

Still a lot of work to be done.

## Installation
1. Clone the repo
```
git clone 
```
3. Create a virtual environment
```
python -m venv venv
```
3. Install the requirements
```
pip install -r requirements.txt
```
4. Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
5. Run the server
```
python manage.py runserver
```

## Features (so far)
- [x] User registration
- [x] User login
- [x] Create a task
- [x] Mark a task as completed
- [x] Delete a task
- [ ] Better README.md
- [ ] Make repeating tasks to work
- [ ] Add a calendar
- [ ] Add a timer
- [ ] Add a pomodoro timer