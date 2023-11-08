import multiprocessing
import os
import time
from subprocess import run
from multiprocessing import Process
import socket


def check_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', 8000))
    if result == 0:
        sock.close()
        return True
    else:
        sock.close()
        return False


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
    while not check_port():
        time.sleep(1)
    p2 = Process(target=worker_process_2)
    p2.start()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
