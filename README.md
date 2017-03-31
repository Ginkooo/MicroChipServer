HOW TO USE IT
=============

1. Install python 3.6
2. python -m pip install virtualenv
3. cd ~ (Or any directory)
4. mkdir envs
5. cd envs
6. virtualenv microchip (or python -m virtualenv microchip if does not work)
7. source microchip/bin/activate (Or if on Windows, run activate from Scripts folder)
8. cd to microchipserver folder
9. pip install -r requirements.txt
10. look for manage.py script in project folder
11. ./manage.py runserver
12. Urls you can get are in url.py file
13. views are in views.py file
