import os
import webbrowser
import asyncio


# RUNSERVER
async def runserver():
    path = r"C:\Users\10390\Desktop\auto-py\python"
    os.chdir(path)
    os.system(r"venv\Scripts\activate && cd ldappro && python manage.py runserver")


# OPEN BROWSER
# def openproject():
#     webbrowser.open_new_tab("http://127.0.0.1:8000/")

def openproject():
    path = r"C:\Users\10390\Desktop\auto-py"
    os.chdir(path)
    os.system(r"npm run start")


# EXECUTE PROGRAM
async def main():
    task1 = asyncio.create_task(runserver())
    openproject()
    await task1


asyncio.run(main())
