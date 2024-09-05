import os


os.system("rm -rf db.sqlite3")
os.system("find . -path '*/migrations/0*' -delete")