import multiprocessing
import os


def task1():
    print("Task 1 assigned to Process: {}".format(multiprocessing.current_process().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to Process: {}".format(multiprocessing.current_process().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main Process
    print("Main process name: {}".format(multiprocessing.current_process().name))

    # creating Process
    p1 = multiprocessing.Process(target=task1, name='t1')
    p2 = multiprocessing.Process(target=task2, name='t2')

    # Process 1 information
    print("----------------------------------")
    print("Process 1 is live or not: {}".format(p1.is_alive()))
    print("Name of 1st Process: {}".format(p1.name))
    print("Native id of the Process 1 is: {}".format(p1.pid))

    # Process 2 information
    print("----------------------------------")
    print("Process 2 is live or not: {}".format(p2.is_alive()))
    print("Name of 2nd Process: {}".format(p2.name))
    print("Native id of the Process 2 is: {}".format(p2.pid))
    print("----------------------------------")
    # starting Process
    p1.start()
    p2.start()

    # wait until all Process finish
    p1.join()
    p2.join()

    # close the process
    p1.close()
    p2.close()

# ------------------------------------------------------------------------

