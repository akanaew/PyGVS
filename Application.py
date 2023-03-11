import pyqtgraph
import msgpack
import threading
from PyQt5 import QtWidgets, QtCore

from GVS import GVS
from MainWindow import Ui_MainWindow
from Oculograph import Oculograph

import numpy as np


class Application(QtWidgets.QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.oculograph = Oculograph()
        self.gvs = GVS()

        # Базовые цвета

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.orange = (255, 185, 0)
        self.cyan = (0, 255, 255)
        self.violet = (255, 0, 255)
        self.pink = (255, 0, 200)
        self.light_yellow = (255, 255, 150)

        # Настройки графиков

        self.oculograph_win = self.ui.oculograph_graph
        self.gvs_win = self.ui.gvs_graph
        self.general_plot = self.ui.general_graph
        self.general_scale_plot = self.ui.general_scale_graph
        self.general_plot_vb = self.general_plot.getViewBox()

        self.o_plot_x = self.oculograph_win.addPlot(col=0, row=0, title='Окулограф X')
        self.o_plot_y = self.oculograph_win.addPlot(col=0, row=1, title='Окулограф Y')

        self.m_plot_x = self.gvs_win.addPlot(col=0, row=0, title='Магнитометр X')
        self.m_plot_y = self.gvs_win.addPlot(col=0, row=1, title='Магнитометр Y')
        self.m_plot_z = self.gvs_win.addPlot(col=0, row=2, title='Магнитометр Z')
        self.g_plot_x = self.gvs_win.addPlot(col=0, row=3, title='Гироскоп X')
        self.g_plot_y = self.gvs_win.addPlot(col=0, row=4, title='Гироскоп Y')
        self.g_plot_z = self.gvs_win.addPlot(col=0, row=5, title='Гироскоп Z')
        self.a_plot_x = self.gvs_win.addPlot(col=0, row=6, title='Акселерометр X')
        self.a_plot_y = self.gvs_win.addPlot(col=0, row=7, title='Акселерометр Y')
        self.a_plot_z = self.gvs_win.addPlot(col=0, row=8, title='Акселерометр Z')

        self.general_plot.showGrid(x=True, y=True)
        self.general_scale_plot.showGrid(x=True, y=True)
        self.o_plot_x.showGrid(x=True, y=True)
        self.o_plot_y.showGrid(x=True, y=True)
        self.m_plot_x.showGrid(x=True, y=True)
        self.m_plot_y.showGrid(x=True, y=True)
        self.m_plot_z.showGrid(x=True, y=True)
        self.g_plot_x.showGrid(x=True, y=True)
        self.g_plot_y.showGrid(x=True, y=True)
        self.g_plot_z.showGrid(x=True, y=True)
        self.a_plot_x.showGrid(x=True, y=True)
        self.a_plot_y.showGrid(x=True, y=True)
        self.a_plot_z.showGrid(x=True, y=True)
        self.m_plot_x.setMouseEnabled(x=False, y=True)
        self.m_plot_y.setMouseEnabled(x=False, y=True)
        self.m_plot_z.setMouseEnabled(x=False, y=True)
        self.g_plot_x.setMouseEnabled(x=False, y=True)
        self.g_plot_y.setMouseEnabled(x=False, y=True)
        self.g_plot_z.setMouseEnabled(x=False, y=True)
        self.a_plot_x.setMouseEnabled(x=False, y=True)
        self.a_plot_y.setMouseEnabled(x=False, y=True)
        self.a_plot_z.setMouseEnabled(x=False, y=True)

        self.general_plot.setXRange(0, 5)

        self.o_curve_x = None
        self.o_curve_y = None

        self.general_plot_region = pyqtgraph.LinearRegionItem()
        self.general_plot_region.setZValue(10)
        self.vertical_general_plot_line = pyqtgraph.InfiniteLine(angle=90, movable=False, label='X:{value:0.2f}')
        self.horizontal_general_plot_line = pyqtgraph.InfiniteLine(angle=0, movable=False, label='Y:{value:0.2f}')
        self.vizier_1 = pyqtgraph.InfiniteLine(angle=90, movable=True, label='Визир1: x={value:0.2f}',
                                               pen=pyqtgraph.mkPen('y', width=3, style=QtCore.Qt.DashLine))
        self.vizier_2 = pyqtgraph.InfiniteLine(angle=90, movable=True, label='Визир2: x={value:0.2f}',
                                               pen=pyqtgraph.mkPen('y', width=3, style=QtCore.Qt.DashLine))

        self.general_plot_region.sigRegionChanged.connect(self.UpdateGeneralPlotRegion)
        self.general_plot.sigRangeChanged.connect(self.UpdateGeneralScale)
        self.proxy_1 = pyqtgraph.SignalProxy(self.general_plot.scene().sigMouseMoved, rateLimit=60,
                                             slot=self.MouseMovedGeneralPlot)
        self.proxy_2 = pyqtgraph.SignalProxy(self.general_plot.scene().sigMouseClicked, rateLimit=60,
                                             slot=self.ClickGeneralPlot)
        # Подключение хэндлеров

        self.ui.start_experiment_button.clicked.connect(self.StartRecordingHandler)
        self.ui.open_oculograph_dump_button.triggered.connect(self.OpenOculographFileDumpHandler)
        self.ui.open_gvs_dump_button.triggered.connect(self.OpenGVSFileDumpHandler)
        self.ui.exit_button.triggered.connect(self.ExitApplicationHandler)
        self.ui.select_magnitometer_axis.currentTextChanged.connect(self.SelectMagnetometerHandler)
        self.ui.select_gyroscope_axis.currentTextChanged.connect(self.SelectGyroscopeHandler)
        self.ui.select_accelerometer_axis.currentTextChanged.connect(self.SelectAccelerometerHandler)
        self.ui.scale_magnitometer_y.valueChanged[float].connect(self.ScaleMagnetometerHandler)
        self.ui.scale_gyroscope_y.valueChanged[float].connect(self.ScaleGyroscopeHandler)
        self.ui.scale_accelerometer_y.valueChanged[float].connect(self.ScaleAccelerometerHandler)
        self.ui.scale_oculograph_x_y.valueChanged[float].connect(self.ScaleOculographXHandler)
        self.ui.scale_oculograph_y_y.valueChanged[float].connect(self.ScaleOculographYHandler)
        self.ui.move_magnitometer_y.valueChanged[float].connect(self.MoveMagnetometerHandler)
        self.ui.move_gyroscope_y.valueChanged[float].connect(self.MoveGyroscopeHandler)
        self.ui.move_accelerometer_y.valueChanged[float].connect(self.MoveAccelerometerHandler)
        self.ui.move_oculograph_x.valueChanged[float].connect(self.MoveOculographXHandler)

        # Глобальные свойства

        self.ox = None
        self.oy = None
        self.ot = None
        self.mx = None
        self.my = None
        self.mz = None
        self.gx = None
        self.gy = None
        self.gz = None
        self.ax = None
        self.ay = None
        self.az = None

        self.tmp_ox = None
        self.tmp_oy = None
        self.tmp_ot = None
        self.tmp_mx = None
        self.tmp_my = None
        self.tmp_mz = None
        self.tmp_gx = None
        self.tmp_gy = None
        self.tmp_gz = None
        self.tmp_ax = None
        self.tmp_ay = None
        self.tmp_az = None

        self.time = None
        self.leds = None
        self.am = 'Ось X'
        self.ag = 'Ось X'
        self.aa = 'Ось X'
        self.ao = 'Ось X и Y'

        self.vizier_value_1 = 0
        self.vizier_value_2 = 0
        self.subscriber = None
        self.experiment_start = False

    def StartRecordingHandler(self):
        if self.experiment_start != True:
            self.experiment_start = True
            self.ui.start_experiment_button.setText('Остановаить эксперимент')
            self.subscriber = self.oculograph.StartRecording()
            self.subscriber.subscribe('notify.')
            
            t1 = threading.Thread(target=self.StartExperimentThreading)
            t1.start()
        else:
            self.experiment_start = False
            self.ui.start_experiment_button.setText('Начать эксперимент')

    def StartExperimentThreading(self):
        while self.experiment_start == True:
            if self.experiment_start == False:
                print(f'При выходе из цыкла {self.experiment_start}')
                print(self.experiment_start)
                break;
            self.subscriber.subscribe('.pupil.1.2d')
            topic, payload = self.subscriber.recv_multipart()
            message = msgpack.loads(payload)
            print(f"{topic}: {message}")
        

    def OpenOculographFileDumpHandler(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileNames(caption='Открыть дамп окулогрофа', filter='*.json')
        if len(path) > 0:
            self.ox, self.oy, self.ot = self.oculograph.LoadDumpFile(path[0])
            self.tmp_ox = self.ox
            self.tmp_oy = self.oy
            self.tmp_ot = self.ot
            self.DrawOculographGraphics()
            self.DrawGeneralGraphics()

    def OpenGVSFileDumpHandler(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileNames(caption='Открыть дамп ГВС', filter='*.txt')
        if len(path) > 0:
            self.time, self.leds, self.mx, self.my, self.mz, self.gx, self.gy, self.gz, self.ax, self.ay, self.az = self.gvs.LoadDumpFile(
                path[0])

            self.tmp_mx = self.mx
            self.tmp_my = self.my
            self.tmp_mz = self.mz
            self.tmp_gx = self.gx
            self.tmp_gy = self.gy
            self.tmp_gz = self.gz
            self.tmp_ax = self.ax
            self.tmp_ay = self.ay
            self.tmp_az = self.az

            m_min = np.array([])
            m_min = np.append(m_min, np.min(self.tmp_mx))
            m_min = np.append(m_min, np.min(self.tmp_my))
            m_min = np.append(m_min, np.min(self.tmp_mz))
            m_max = np.array([])
            m_max = np.append(m_max, np.max(self.tmp_mx))
            m_max = np.append(m_max, np.max(self.tmp_my))
            m_max = np.append(m_max, np.max(self.tmp_mz))

            g_min = np.array([])
            g_min = np.append(g_min, np.min(self.tmp_gx))
            g_min = np.append(g_min, np.min(self.tmp_gy))
            g_min = np.append(g_min, np.min(self.tmp_gz))
            g_max = np.array([])
            g_max = np.append(g_max, np.max(self.tmp_gx))
            g_max = np.append(g_max, np.max(self.tmp_gy))
            g_max = np.append(g_max, np.max(self.tmp_gz))
            a_min = np.array([])
            a_min = np.append(a_min, np.min(self.tmp_ax))
            a_min = np.append(a_min, np.min(self.tmp_ay))
            a_min = np.append(a_min, np.min(self.tmp_az))
            a_max = np.array([])
            a_max = np.append(a_max, np.max(self.tmp_ax))
            a_max = np.append(a_max, np.max(self.tmp_ay))
            a_max = np.append(a_max, np.max(self.tmp_az))

            self.m_plot_x.setYRange(np.min(m_min), np.max(m_max))
            self.m_plot_y.setYRange(np.min(m_min), np.max(m_max))
            self.m_plot_z.setYRange(np.min(m_min), np.max(m_max))
            self.g_plot_x.setYRange(np.min(g_min), np.max(g_max))
            self.g_plot_y.setYRange(np.min(g_min), np.max(g_max))
            self.g_plot_z.setYRange(np.min(g_min), np.max(g_max))
            self.a_plot_x.setYRange(np.min(a_min), np.max(a_max))
            self.a_plot_y.setYRange(np.min(a_min), np.max(a_max))
            self.a_plot_z.setYRange(np.min(a_min), np.max(a_max))
            self.DrawGVSGraphics()
            self.DrawGeneralGraphics()

    def SelectMagnetometerHandler(self, value):
        self.am = value
        self.DrawGeneralGraphics()

    def SelectGyroscopeHandler(self, value):
        self.ag = value
        self.DrawGeneralGraphics()

    def SelectAccelerometerHandler(self, value):
        self.aa = value
        self.DrawGeneralGraphics()

    def ScaleMagnetometerHandler(self, value):
        if self.am == 'Ось X':
            self.tmp_mx = [x * value for x in self.mx]
        if self.am == 'Ось Y':
            self.tmp_my = [x * value for x in self.my]
        if self.am == 'Ось Z':
            self.tmp_mz = [x * value for x in self.mz]

        self.DrawGeneralGraphics()

    def ScaleGyroscopeHandler(self, value):
        if self.ag == 'Ось X':
            self.tmp_gx = [x * value for x in self.gx]
        if self.ag == 'Ось Y':
            self.tmp_gy = [x * value for x in self.gy]
        if self.ag == 'Ось Z':
            self.tmp_gz = [x * value for x in self.gz]

        self.DrawGeneralGraphics()

    def ScaleAccelerometerHandler(self, value):
        if self.aa == 'Ось X':
            self.tmp_ax = [x * value for x in self.ax]
        if self.aa == 'Ось Y':
            self.tmp_ay = [x * value for x in self.ay]
        if self.aa == 'Ось Z':
            self.tmp_az = [x * value for x in self.az]

        self.DrawGeneralGraphics()

    def ScaleOculographXHandler(self, value):
        self.tmp_ox = [x * value for x in self.ox]
        self.DrawGeneralGraphics()

    def ScaleOculographYHandler(self, value):
        self.tmp_oy = [x * value for x in self.oy]
        self.DrawGeneralGraphics()

    def MoveMagnetometerHandler(self, value):
        if self.am == 'Ось X':
            self.tmp_mx = [x + value for x in self.tmp_mx]
        if self.am == 'Ось Y':
            self.tmp_my = [x + value for x in self.tmp_my]
        if self.am == 'Ось Z':
            self.tmp_mz = [x + value for x in self.tmp_mz]

        self.DrawGeneralGraphics()

    def MoveGyroscopeHandler(self, value):
        if self.ag == 'Ось X':
            self.tmp_gx = [x + value for x in self.tmp_gx]
        if self.ag == 'Ось Y':
            self.tmp_gy = [x + value for x in self.tmp_gy]
        if self.ag == 'Ось Z':
            self.tmp_gz = [x + value for x in self.tmp_gz]

        self.DrawGeneralGraphics()

    def MoveAccelerometerHandler(self, value):
        if self.aa == 'Ось X':
            self.tmp_ax = [x + value for x in self.tmp_ax]
        if self.aa == 'Ось Y':
            self.tmp_ay = [x + value for x in self.tmp_ay]
        if self.aa == 'Ось Z':
            self.tmp_az = [x + value for x in self.tmp_az]

        self.DrawGeneralGraphics()

    def MoveOculographXHandler(self, value):
        self.tmp_ot = [x + value for x in self.ot]
        self.DrawGeneralGraphics()

    def DrawGeneralGraphics(self):
        self.general_plot.clear()
        self.general_scale_plot.clear()

        self.general_scale_plot.addItem(self.general_plot_region, ignoreBounds=True)
        self.general_plot.addItem(self.vizier_1, ignoreBounds=True)
        self.general_plot.addItem(self.vizier_2, ignoreBounds=True)
        self.vizier_1.setPos(self.vizier_value_1)
        self.vizier_1.setPos(self.vizier_value_2)
        self.general_plot.addItem(self.horizontal_general_plot_line, ignoreBounds=True)
        self.general_plot.addItem(self.vertical_general_plot_line, ignoreBounds=True)

        m = None
        g = None
        a = None

        if self.am == 'Ось X':
            m = self.tmp_mx
        if self.am == 'Ось Y':
            m = self.tmp_my
        if self.am == 'Ось Z':
            m = self.tmp_mz

        if self.ag == 'Ось X':
            g = self.tmp_gx
        if self.ag == 'Ось Y':
            g = self.tmp_gy
        if self.ag == 'Ось Z':
            g = self.tmp_gz

        if self.aa == 'Ось X':
            a = self.tmp_ax
        if self.aa == 'Ось Y':
            a = self.tmp_ay
        if self.aa == 'Ось Z':
            a = self.tmp_az
        if self.time is not None:
            self.general_plot.plot(self.time, m, pen=self.pink, name='Магнитометр')
            self.general_plot.plot(self.time, g, pen=self.green, name='Гироскоп')
            self.general_plot.plot(self.time, a, pen=self.blue, name='Акселерометр')
            self.general_scale_plot.plot(self.time, m, pen=self.pink, name='Магнитометр')
            self.general_scale_plot.plot(self.time, g, pen=self.green, name='Гироскоп')
            self.general_scale_plot.plot(self.time, a, pen=self.blue, name='Акселерометр')
            for led in self.leds:
                self.general_plot.addItem(
                    pyqtgraph.InfiniteLine(movable=False, pos=led[0], angle=90, pen='r', label=f'{led[1]}',
                                           labelOpts={'position': 0.1, 'color': (255, 255, 255),
                                                      'fill': (255, 0, 0, 100), 'movable': True}))
        if self.ot is not None:
            self.general_plot.plot(self.tmp_ot, self.tmp_ox, pen=self.orange, name='Окулограф X')
            self.general_plot.plot(self.tmp_ot, self.tmp_oy, pen=self.cyan, name='Окулограф Y')
            self.general_scale_plot.plot(self.tmp_ot, self.tmp_ox, pen=self.orange, name='Окулограф X')
            self.general_scale_plot.plot(self.tmp_ot, self.tmp_oy, pen=self.cyan, name='Окулограф Y')

    def DrawOculographGraphics(self):
        self.o_plot_x.clear()
        self.o_plot_y.clear()
        self.o_plot_x.plot(x=self.ot, y=self.ox, pen=self.orange, name='Окулограф X')
        self.o_plot_y.plot(x=self.ot, y=self.oy, pen=self.cyan, name='Окулограф y')

    def DrawGVSGraphics(self):
        self.m_plot_x.clear()
        self.m_plot_y.clear()
        self.m_plot_z.clear()
        self.g_plot_x.clear()
        self.g_plot_y.clear()
        self.g_plot_z.clear()
        self.a_plot_x.clear()
        self.a_plot_y.clear()
        self.a_plot_z.clear()
        self.m_plot_x.plot(x=self.time, y=self.mx, pen=self.pink, name='Магнитометр X')
        self.m_plot_y.plot(x=self.time, y=self.my, pen=self.pink, name='Магнитометр Y')
        self.m_plot_z.plot(x=self.time, y=self.mz, pen=self.pink, name='Магнитометр Z')
        self.g_plot_x.plot(x=self.time, y=self.gy, pen=self.green, name='Гироскоп X')
        self.g_plot_y.plot(x=self.time, y=self.gy, pen=self.green, name='Гироскоп Y')
        self.g_plot_z.plot(x=self.time, y=self.gy, pen=self.green, name='Гироскоп Z')
        self.a_plot_x.plot(x=self.time, y=self.ax, pen=self.blue, name='Акселерометр X')
        self.a_plot_y.plot(x=self.time, y=self.ay, pen=self.blue, name='Акселерометр Y')
        self.a_plot_z.plot(x=self.time, y=self.az, pen=self.blue, name='Акселерометр Z')

    def UpdateGeneralPlotRegion(self):
        self.general_plot_region.setZValue(10)
        minX, maxX = self.general_plot_region.getRegion()
        self.general_plot.setXRange(minX, maxX, padding=0)
        self.general_plot.setXRange(minX, maxX, padding=0)

    def UpdateGeneralScale(self, window, viewRange):
        rgn = viewRange[0]
        self.general_plot_region.setRegion(rgn)

    def MouseMovedGeneralPlot(self, evt):
        pos = evt[0]
        if self.general_plot.sceneBoundingRect().contains(pos):
            mousePoint = self.general_plot_vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            if index > 0 and index < len(self.time):
                self.vertical_general_plot_line.setPos(mousePoint.x())
                self.horizontal_general_plot_line .setPos(mousePoint.y())
                self.ui.delta_4.setText(f'X;Y;: {mousePoint.x()};{mousePoint.y()}')

    def ClickGeneralPlot(self, pos):
        clickPoint = self.general_plot_vb.mapSceneToView(pos[0].pos())
        if self.vizier_value_1 == 0:
            self.vizier_value_1 = clickPoint.x()
            self.vizier_1.setPos(self.vizier_value_1)
            self.ui.delta_2.setText(f'Визир 1: {self.vizier_value_1}')
        else:
            if self.vizier_value_2 == 0:
                self.vizier_value_2 = clickPoint.x()
                self.vizier_2.setPos(self.vizier_value_2)
                self.ui.delta_3.setText(f'Визир 2: {self.vizier_value_2}')
                self.ui.delta.setText(f'Дельта: {self.vizier_value_2 - self.vizier_value_1}')
            else:
                self.vizier_value_1 = 0
                self.vizier_value_2 = 0
                self.vizier_1.setPos(self.vizier_value_1)
                self.vizier_2.setPos(self.vizier_value_2)

    def ExitApplicationHandler(self):
        QtWidgets.QApplication.quit()
