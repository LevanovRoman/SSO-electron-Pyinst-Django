import os
import subprocess

path = r"C:\Users\10390\Desktop\auto-py"
os.chdir(path)

# os.system(r"venv\Scripts\activate && cd ldappro && python manage.py runserver")
# subprocess.run([r"venv\Scripts\activate", "cd ldappro", "python manage.py runserver"])
# result = subprocess.run(["ls"], capture_output=True)
# print(result.stdout)
subprocess.run(r"npm run start", shell=True)

