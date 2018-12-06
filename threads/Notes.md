# Threads

## Process Vs Threads

#### Process
Any program running on your computer is basically a process or task.<br>
A process is an executing instance of an application.<br>
e.g opening Google Chrome or Microsoft word is a process.<br>
A process can be referred to as a "Main Thread".

#### Threads
Anything executing <b>within</b> a process is a thread.<br>
A thread is the unit of execution within a process.<br>
Each process has at least one thread. It can be made up of multiple threads assigned to specific tasks within a process.
<br>
<b>Multithreading</b> is often used in games.<br>
A thread is a portion of code that may be executed independently of the main program or main thread.

#### Single Thread
If you are not creating any other threads in your program then they are all single threaded programs.<br>
We can make multi threads running in parallel making the best use of the processor.<br>
You can not execute two parallel processes on a uni-processor system.

## Ways of Creating Threads in Python.
1. Using the function.
2. Extending the thread class.
3. Without extending the thread class.

## Thread Communication
In many cases the threads need to communicate with each other to share some kind of information.<br>
We can solve the <b>Producer Consumer Problem</b> in the following ways:
* Using the boolean flag.
* Using wait and notify.

Resolve using Locks and Semaphores.
