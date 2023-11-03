import os
import subprocess

path = r"C:\Users\10390\Desktop\auto-py\python"
os.chdir(path)

s1 = subprocess.run(r"venv\Scripts\activate && cd ldappro && python manage.py runserver", shell=True)
# path = r"C:\Users\10390\Desktop\auto-py"
# os.chdir(path)
#
# s2 = subprocess.Popen(r"npm run start", shell=True)


