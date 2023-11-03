import os
import time


# RUNSERVER
def runserver():
    path = r"C:\Users\10390\Desktop\auto-py\python"
    os.chdir(path)
    os.system(r"venv\Scripts\activate && cd ldappro && python manage.py runserver")
    return True

# OPEN BROWSER
# def openproject():
#     webbrowser.open_new_tab("http://127.0.0.1:8000/")

def openproject():
    path = r"C:\Users\10390\Desktop\auto-py"
    os.chdir(path)
    os.system(r"npm run start")


# EXECUTE PROGRAM
def main():
    St = runserver()
    if St:
        openproject()


main()
