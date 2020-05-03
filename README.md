# WhasApp survey via Django

Download requirements via pip install -r requirements.txt.

Run:
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

Go to 127.0.0.1:8000/round1 for round 1 questionnaire. Similarly, for round 2 questionnaire. 

Edit forms.py to change form view structure on the webpage, and views.py to change response collection methods. 
(These files are present in respective round1 or round2 folders.)

To change the web page (except the form), go to templates/form.html in respective folders.

To change image, go to templates/form.html (line 101). The images must be added to the media folder first.
(Dynamic image changing not enabled yet.)
