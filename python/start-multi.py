import multiprocessing
import os
from subprocess import run
from multiprocessing import Process


def worker_process_1():
    path = r"C:\Users\10390\Desktop\auto-py\python"
    os.chdir(path)
    s1 = run(r"venv\Scripts\activate && cd ldappro && python manage.py runserver", shell=True)


def worker_process_2():
    path = r"C:\Users\10390\Desktop\auto-py"
    os.chdir(path)
    s1 = run(r"npm run start", shell=True)


def main():
    workers = []
    p1 = Process(target=worker_process_1)
    p1.start()
    p2 = Process(target=worker_process_2)
    p2.start()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
