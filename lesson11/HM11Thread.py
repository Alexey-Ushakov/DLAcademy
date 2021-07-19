import time
from threading import Thread, Event, get_ident
import threading

event = Event()
variable = ""
mutex = threading.Lock()


def producer1():
    event.set()
    global variable
    for _ in range(3):
        with mutex:
            variable += " Новая глава!"
            print("Bob говорит: Все ждите, пока я работаю!")
            time.sleep(1)


def producer2():
    event.set()
    global variable
    for _ in range(3):
        with mutex:
            variable += " Старая глава"
            print("Lisa говорит: Все ждите, пока я работаю!")
            time.sleep(1)

def consumer(thread_id):
    while True:
        event.wait()
        with mutex:
            print("{} - Я взял! Вот что там было: {}".format(thread_id, variable))


if __name__ == '__main__':
    threads_prod1 = Thread(target=producer1)
    threads_prod2 = Thread(target=producer2)
    threds_prod = [threads_prod1, threads_prod2]

    threads = (Thread(target=consumer, args=(thread_id,))
               for thread_id in range(10))


    for p in threds_prod:
        p.start()
    for p in threds_prod:
        p.join()
    for t in threads:
        t.start()
    event.clear()
    for t in threads:
        t.join()

    print(variable)
