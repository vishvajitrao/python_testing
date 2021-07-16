import threading
import os
from time import time, ctime


def Square(n):
    result = n * n
    print("The result is:- ", result)


def Cube(num):
    result = num * num * num
    print("The result is:- ", result)


if __name__ == '__main__':
    # let's check time to execute a python program with and without threading
    start = time()
    Square(10064576476)
    Cube(20075869686346457)
    end = time()
    print("Total time to executing:- ", (end - start))

    print("----------------------------")

    # creating thread
    start1 = time()
    t1 = threading.Thread(target=Square, args=(10064576476,))
    t2 = threading.Thread(target=Cube, args=(20075869686346457,))

    # starting thread
    t1.start()
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 1 is completely executed
    t2.join()

    end1 = time()
    print("total time to executing:- ", (end1 - start1))
    print("All done!")

print("----------------------------")


# Python program to illustrate the concept
# of threading


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # thread 1 information
    print("----------------------------------")
    print("Thread 1 is live or not: {}".format(t1.is_alive()))
    print("Name of 1st thread: {}".format(t1.getName()))
    print("Name of 1st thread: {}".format(t1.name))
    print("native id of the thread 1 is: {}".format(t1.native_id))

    # thread 2 information
    print("----------------------------------")
    print("Thread 2 is live or not: {}".format(t1.is_alive()))
    print("Name of 2nd thread: {}".format(t1.getName()))
    print("Name of 2nd thread: {}".format(t1.name))
    print("native id of the thread 2 is: {}".format(t1.native_id))
    print("----------------------------------")
    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()
