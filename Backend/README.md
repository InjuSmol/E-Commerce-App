STEP's:


1. intall python (3.11)
2. install and activate virtual environment (source /env/bin/activate)
3. install django
4. django-admin startproject e_shop --> create project
5. python3 manage.py startapp main
6. python3 manage.py runserver
 http://127.0.0.1:8000/admin
7. python3 manage.py createsuperuser
Models: 
8. go to main.py/models.py

\* vim usage: 
This will open the vi or vim text editor. You can enter insert mode by pressing i, type your code, then save and exit by pressing Esc, typing :wq, and pressing Enter.

9. Created model Category with a title and image
10. python3 manage.py makemigrations (check if in yourApp/settings.py:Intalled_Apps there is the name of your 'main' app included')
11. ... manage.py migrate
12. ... admin.py in main
13. add brand, size and color
14. images: https://www.pexels.com/ru-ru/@the-glorious-studio-3584518/


