# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
from configuration import  Configuration
from checkReader import  checkReader

__author__ = 'Gio_Manu'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

class RandomThread(Thread):
    def __init__(self):
        self.reader = checkReader.CheckReader(Configuration)
        self.delay = 2
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            number = round(random()*10, 3)
            print(number)
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            sleep(self.delay)

    def getChecks(self):
        while not thread_stop_event.isSet():
            res = self.reader.readChecks()
            print(res)
            socketio.emit('Result',{'objects':res},namespace="/test")
            sleep(self.delay)

    def run(self):
        self.getChecks()


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index_demo.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
