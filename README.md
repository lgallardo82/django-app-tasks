Task App

This is a task application with a CRUD. It has integrated user authentication ##Built with🛠️

    Django
    DjangoRestFramework

Instructions📋:

How to get a copy of the project running on your local machine 1.Clone the repository

git clone https://github.com/santiudev/taskAppDjango.git

2.Create a virtual environment From the cloned directory run:

python -m venv env

3.Activate the virtualenv On macOs or Linux:

source venv/bin/activate

On Windows:

env\scripts\activate

3.Install required requirements

pip install -r requirements.txt

4.Run migrations

python manage.py makemigrations

python manage.py migrate

5.Create an admin User

python manage.py createsuperuser

5.Run the application

python manage.py runserver

Feel free to test and modify it. If you want to contribute You can create a pull request to the project