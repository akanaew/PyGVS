import numpy as np


class GVS:
    def __init__(self):
        super(GVS, self).__init__()
        self.mx = np.array([])
        self.my = np.array([])
        self.mz = np.array([])
        self.gx = np.array([])
        self.gy = np.array([])
        self.gz = np.array([])
        self.ax = np.array([])
        self.ay = np.array([])
        self.az = np.array([])
        self.time = np.array([])
        self.LEDs = []

    def LoadDumpFile(self, path):
        file = open(path, 'r')
        damp = file.read()
        rows = damp.split("\n")
        time = 0
        for index, row in enumerate(rows):
            if row != "":
                cols = row.split(", ")
                oldIndex = index - 1
                if index == 0:
                    oldIndex = 0
                oldCols = rows[oldIndex].split(", ")
                delta = int(cols[1]) - int(oldCols[1])
                if delta < 0:
                    delta = delta + 65535
                if time == 0:
                    time = delta / 32768
                else:
                    time = time + delta / 32768
                self.time = np.append(self.time, time)
                txt = ''
                if index == 0:
                    if int(cols[2]) & (1 << 0):
                        txt = 'Центр'
                    self.LEDs.append([time, txt])
                else:
                    if int(oldCols[2]) != int(cols[2]):
                        if int(cols[2]) & (1 << 0):
                            txt = 'Центр'
                        if int(cols[2]) & (1 << 1):
                            txt = 'Верх'
                        if int(cols[2]) & (1 << 2):
                            txt = 'Лево'
                        if int(cols[2]) & (1 << 3):
                            txt = 'Низ'
                        if int(cols[2]) & (1 << 4):
                            txt = 'Право'
                        if int(cols[2]) & (1 << 5):
                            txt = 'ГВС'
                        self.LEDs.append([time, txt])
                self.mx = np.append(self.mx, int(np.int16(cols[3])))
                self.my = np.append(self.my, int(np.int16(cols[4])))
                self.mz = np.append(self.mz, int(np.int16(cols[5])))
                self.gx = np.append(self.gx, int(np.int16(cols[6])))
                self.gy = np.append(self.gy, int(np.int16(cols[7])))
                self.gz = np.append(self.gz, int(np.int16(cols[8])))
                self.ax = np.append(self.ax, int(np.int16(cols[9])))
                self.ay = np.append(self.ay, int(np.int16(cols[10])))
                self.az = np.append(self.az, int(np.int16(cols[11])))
        return self.time, self.LEDs, self.mx, self.my, self.mz, self.gx, self.gy, self.gz, self.ax, self.ay, self.az
