# Start with a basic flask app webpage.
from flask_socketio import SocketIO
from flask import Flask, render_template
from threading import Thread, Event

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import  Observer
from CheckReader import checkReader

from configuration import Configuration

__author__ = 'Gio_Manu'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()

thread_stop_event = Event()

class ServerThread(Thread):
    def __init__(self):
        self.reader = checkReader.CheckReader(Configuration)
        self.delay = Configuration.SCANNER_DELAY

        #define eventHandler
        self.event_handler = PatternMatchingEventHandler("*.txt", ignore_patterns="", ignore_directories=True, case_sensitive=False)

        #set events
        self.event_handler.on_modified = self.on_modified

        #define Observer
        self.observer = Observer()
        self.observer.schedule(self.event_handler,path="./",recursive=False)

        super(ServerThread, self).__init__()

    def on_modified(self,event):
        res = self.reader.readChecks()
        socketio.emit('Result',{'objects':res},namespace="/test")

    def run(self):
        self.observer.start()

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
        thread = ServerThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
