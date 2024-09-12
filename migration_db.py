import os


# migrate
os.system('python src/manage.py makemigrations')
os.system('python src/manage.py migrate')