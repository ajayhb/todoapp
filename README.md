An App wherein you can create a project and tasks within that Project to assign it to someone.

Suggestions:
1) Create a Project before creating a Task.
2) Project Duration Must be of the form ```HH:MM:SS```
3) In a newly created Project, the Image won't be shown earlier unless you update it by uploading a new one. 

Setup: 
1) Clone the project into your new directory at any location on your computer.
2) Create a virtualenv with python (Preferred version 3.6 or 3.7) and activate it.
   eg.: for python version 3.6
```
apt-get install python3-pip
sudo pip3 install virtualenv
virtualenv -p python3.6 <venv_name>
source <venv_name>/bin/activate
```
3) Go to that directory path on your terminal where you cloned the project and run the command: ```pip install -r requirements.txt```
4) Create a superuser and a few users for this app to view the Projects and Tasks in Django Admin:
   Superuser:
```
python manage.py createsuperuser
```
  Other Users example:
```
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user(username='userone',email='userone@gmail.com', password='userone')
user = User.objects.create_user(username='usertwo',email='usertwo@gmail.com', password='usertwo')
user = User.objects.create_user(username='userthree',email='userthree@gmail.com', password='userthree')
...
exit()
```
5) Make migrations and run the server
```
python manage.py makemigrations todoapp
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
Further Scope:
  a) User Authentication.
  b) Only the Selected Users can Create, Update and Delete the Tasks.
  c) Drastic Changes in the UI.
