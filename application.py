from flask_socketio import SocketIO
from flask import Flask, render_template,request
from threading import Thread, Event

import json
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from CheckReader import checkReader
from configuration import Configuration

__author__ = 'Gio_Manu'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = False

socketio = SocketIO(app)

thread = Thread()

thread_stop_event = Event()


class ServerThread(Thread):
    def __init__(self):
        # define checkReader
        self.reader = checkReader.CheckReader(Configuration)

        self.delay = Configuration.SCANNER_DELAY

        # define eventHandler
        self.event_handler = PatternMatchingEventHandler("*.txt", ignore_patterns="", ignore_directories=True,
                                                         case_sensitive=False)
        # set events
        self.event_handler.on_modified = self.on_modified

        #define Observer
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path="./", recursive=False)

        super(ServerThread, self).__init__()

    def on_modified(self,event):
        self.sendChecks()

    def sendChecks(self):
        res = self.reader.readChecks()
        socketio.emit('Result', {'objects': res}, namespace="/QueueMonitor")

    def run(self):
        self.observer.start()

def registerCheck(num,mode):
    with open(Configuration.CHECKS_PATH,'a') as f:
        f.write("\n")
        f.write("{}|{}".format(num,mode))

@app.route('/')
@app.route('/<terminalID>')
def index(terminalID = None):
    if terminalID is None:
        return render_template('QueueDisplay.html')
    return render_template('Index.html',value=terminalID)

@app.route('/distr')
def distr():
    return render_template('DistDisplay.html')

@app.route('/registerNum/<mode>',methods=['POST'])
def registerNum(mode=None):
    data = request.get_json()
    if not len(data) == 0:
        for el in data:
            registerCheck(num=int(el),mode=int(mode))

    return json.dumps({"status":200})

@socketio.on('connect', namespace='/QueueMonitor')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    # Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = ServerThread()
        thread.start()
    # first broadcast on connect
    thread.sendChecks()


@socketio.on('disconnect', namespace='/QueueMonitor')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=int(80))
