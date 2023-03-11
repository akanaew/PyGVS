import json
import time
import zmq

import numpy as np


class Oculograph:
    def __init__(self):
        super(Oculograph, self).__init__()
        self.x = np.array([])
        self.y = np.array([])
        self.t = np.array([])
        self.pupil_remote = None
        self.subscriber = None

    def LoadDumpFile(self, path):
        if len(path) == 0:
            return "Не задан путь до файла"

        file = open(path, 'r').read()
        json_data = json.loads(file)
        print(len(json_data['x']))
        for x in json_data['x']:
            self.x = np.append(self.x, x)

        for y in json_data['y']:
            self.y = np.append(self.y, y)

        for t in json_data['t']:
            self.t = np.append(self.t, t)

        return self.x, self.y, self.t

    def SaveDumpFile(self, path, x, y, t):
        oculographDump = {'x': x, 'y': y, 't': t}
        file = open(f'{path}experiment_{time.time()}.json', 'w')
        json.dump(oculographDump, file, sort_keys=True, indent=2)

    def StartRecording(self):
        ctx = zmq.Context()
        
        self.pupil_remote = zmq.Socket(ctx, zmq.REQ)
        self.pupil_remote.connect('tcp://127.0.0.1:50020')
        self.pupil_remote.send_string('R')
        print(self.pupil_remote.recv_string())
        self.pupil_remote.send_string('SUB_PORT')
        sub_port = self.pupil_remote.recv_string()
        self.subscriber = ctx.socket(zmq.SUB)
        self.subscriber.connect(f'tcp://localhost:{sub_port}')

        return self.subscriber