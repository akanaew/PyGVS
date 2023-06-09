# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 792)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(110, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.experement_number_combobox = QtWidgets.QComboBox(self.groupBox)
        self.experement_number_combobox.setObjectName("experement_number_combobox")
        self.experement_number_combobox.addItem("")
        self.experement_number_combobox.addItem("")
        self.experement_number_combobox.addItem("")
        self.verticalLayout_4.addWidget(self.experement_number_combobox)
        self.recording_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.recording_checkbox.setObjectName("recording_checkbox")
        self.verticalLayout_4.addWidget(self.recording_checkbox)
        self.start_experiment_button = QtWidgets.QPushButton(self.groupBox)
        self.start_experiment_button.setObjectName("start_experiment_button")
        self.verticalLayout_4.addWidget(self.start_experiment_button)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(280, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.inverse_magnetometer = QtWidgets.QCheckBox(self.groupBox_2)
        self.inverse_magnetometer.setObjectName("inverse_magnetometer")
        self.horizontalLayout_2.addWidget(self.inverse_magnetometer)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.scale_magnitometer_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.scale_magnitometer_y.setMinimum(-10000.0)
        self.scale_magnitometer_y.setMaximum(10000.0)
        self.scale_magnitometer_y.setSingleStep(0.01)
        self.scale_magnitometer_y.setObjectName("scale_magnitometer_y")
        self.horizontalLayout_3.addWidget(self.scale_magnitometer_y)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_17.addWidget(self.label_29)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.move_magnitometer_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.move_magnitometer_y.setMinimum(-10000.0)
        self.move_magnitometer_y.setMaximum(10000.0)
        self.move_magnitometer_y.setSingleStep(0.01)
        self.move_magnitometer_y.setObjectName("move_magnitometer_y")
        self.horizontalLayout_17.addWidget(self.move_magnitometer_y)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.select_magnitometer_axis = QtWidgets.QComboBox(self.groupBox_2)
        self.select_magnitometer_axis.setObjectName("select_magnitometer_axis")
        self.select_magnitometer_axis.addItem("")
        self.select_magnitometer_axis.addItem("")
        self.select_magnitometer_axis.addItem("")
        self.verticalLayout_5.addWidget(self.select_magnitometer_axis)
        self.verticalLayout_20.addLayout(self.verticalLayout_5)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.inverse_gyroscope = QtWidgets.QCheckBox(self.groupBox_2)
        self.inverse_gyroscope.setObjectName("inverse_gyroscope")
        self.horizontalLayout_4.addWidget(self.inverse_gyroscope)
        self.verticalLayout_18.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.scale_gyroscope_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.scale_gyroscope_y.setMinimum(-10000.0)
        self.scale_gyroscope_y.setMaximum(10000.0)
        self.scale_gyroscope_y.setSingleStep(0.01)
        self.scale_gyroscope_y.setObjectName("scale_gyroscope_y")
        self.horizontalLayout_5.addWidget(self.scale_gyroscope_y)
        self.verticalLayout_18.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_16.addWidget(self.label_28)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.move_gyroscope_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.move_gyroscope_y.setMinimum(-10000.0)
        self.move_gyroscope_y.setMaximum(10000.0)
        self.move_gyroscope_y.setSingleStep(0.01)
        self.move_gyroscope_y.setObjectName("move_gyroscope_y")
        self.horizontalLayout_16.addWidget(self.move_gyroscope_y)
        self.verticalLayout_18.addLayout(self.horizontalLayout_16)
        self.select_gyroscope_axis = QtWidgets.QComboBox(self.groupBox_2)
        self.select_gyroscope_axis.setObjectName("select_gyroscope_axis")
        self.select_gyroscope_axis.addItem("")
        self.select_gyroscope_axis.addItem("")
        self.select_gyroscope_axis.addItem("")
        self.verticalLayout_18.addWidget(self.select_gyroscope_axis)
        self.verticalLayout_20.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.inverse_accelerometer = QtWidgets.QCheckBox(self.groupBox_2)
        self.inverse_accelerometer.setObjectName("inverse_accelerometer")
        self.horizontalLayout_6.addWidget(self.inverse_accelerometer)
        self.verticalLayout_19.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.scale_accelerometer_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.scale_accelerometer_y.setMinimum(-10000.0)
        self.scale_accelerometer_y.setMaximum(10000.0)
        self.scale_accelerometer_y.setSingleStep(0.01)
        self.scale_accelerometer_y.setObjectName("scale_accelerometer_y")
        self.horizontalLayout_7.addWidget(self.scale_accelerometer_y)
        self.verticalLayout_19.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_12.addWidget(self.label_24)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.move_accelerometer_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.move_accelerometer_y.setMinimum(-10000.0)
        self.move_accelerometer_y.setMaximum(10000.0)
        self.move_accelerometer_y.setSingleStep(0.01)
        self.move_accelerometer_y.setObjectName("move_accelerometer_y")
        self.horizontalLayout_12.addWidget(self.move_accelerometer_y)
        self.verticalLayout_19.addLayout(self.horizontalLayout_12)
        self.select_accelerometer_axis = QtWidgets.QComboBox(self.groupBox_2)
        self.select_accelerometer_axis.setObjectName("select_accelerometer_axis")
        self.select_accelerometer_axis.addItem("")
        self.select_accelerometer_axis.addItem("")
        self.select_accelerometer_axis.addItem("")
        self.verticalLayout_19.addWidget(self.select_accelerometer_axis)
        self.verticalLayout_20.addLayout(self.verticalLayout_19)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.inverse_oculograph_x = QtWidgets.QCheckBox(self.groupBox_2)
        self.inverse_oculograph_x.setObjectName("inverse_oculograph_x")
        self.horizontalLayout_8.addWidget(self.inverse_oculograph_x)
        self.inverse_oculograph_y = QtWidgets.QCheckBox(self.groupBox_2)
        self.inverse_oculograph_y.setObjectName("inverse_oculograph_y")
        self.horizontalLayout_8.addWidget(self.inverse_oculograph_y)
        self.verticalLayout_21.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.scale_oculograph_x_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.scale_oculograph_x_y.setMinimum(-10000.0)
        self.scale_oculograph_x_y.setMaximum(10000.0)
        self.scale_oculograph_x_y.setSingleStep(0.01)
        self.scale_oculograph_x_y.setObjectName("scale_oculograph_x_y")
        self.horizontalLayout_9.addWidget(self.scale_oculograph_x_y)
        self.verticalLayout_21.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_10.addWidget(self.label_22)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.scale_oculograph_y_y = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.scale_oculograph_y_y.setMinimum(-10000.0)
        self.scale_oculograph_y_y.setMaximum(10000.0)
        self.scale_oculograph_y_y.setSingleStep(0.01)
        self.scale_oculograph_y_y.setObjectName("scale_oculograph_y_y")
        self.horizontalLayout_10.addWidget(self.scale_oculograph_y_y)
        self.verticalLayout_21.addLayout(self.horizontalLayout_10)
        self.select_oculograph_axis = QtWidgets.QComboBox(self.groupBox_2)
        self.select_oculograph_axis.setObjectName("select_oculograph_axis")
        self.select_oculograph_axis.addItem("")
        self.select_oculograph_axis.addItem("")
        self.select_oculograph_axis.addItem("")
        self.verticalLayout_21.addWidget(self.select_oculograph_axis)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_11.addWidget(self.label_23)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.move_oculograph_x = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.move_oculograph_x.setMinimum(-10000.0)
        self.move_oculograph_x.setMaximum(10000.0)
        self.move_oculograph_x.setSingleStep(1e-06)
        self.move_oculograph_x.setObjectName("move_oculograph_x")
        self.horizontalLayout_11.addWidget(self.move_oculograph_x)
        self.verticalLayout_21.addLayout(self.horizontalLayout_11)
        self.verticalLayout_20.addLayout(self.verticalLayout_21)
        self.hidden_leds = QtWidgets.QCheckBox(self.groupBox_2)
        self.hidden_leds.setObjectName("hidden_leds")
        self.verticalLayout_20.addWidget(self.hidden_leds)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(280, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.delta = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delta.setFont(font)
        self.delta.setObjectName("delta")
        self.verticalLayout.addWidget(self.delta)
        self.delta_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delta_2.setFont(font)
        self.delta_2.setObjectName("delta_2")
        self.verticalLayout.addWidget(self.delta_2)
        self.delta_3 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delta_3.setFont(font)
        self.delta_3.setObjectName("delta_3")
        self.verticalLayout.addWidget(self.delta_3)
        self.delta_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delta_4.setFont(font)
        self.delta_4.setObjectName("delta_4")
        self.verticalLayout.addWidget(self.delta_4)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.oculograph_graph = GraphicsLayoutWidget(self.tab)
        self.oculograph_graph.setObjectName("oculograph_graph")
        self.horizontalLayout_19.addWidget(self.oculograph_graph)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.gvs_graph = GraphicsLayoutWidget(self.tab_2)
        self.gvs_graph.setObjectName("gvs_graph")
        self.horizontalLayout_18.addWidget(self.gvs_graph)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.general_graph = PlotWidget(self.tab_3)
        self.general_graph.setObjectName("general_graph")
        self.gridLayout_2.addWidget(self.general_graph, 0, 0, 1, 1)
        self.general_scale_graph = PlotWidget(self.tab_3)
        self.general_scale_graph.setObjectName("general_scale_graph")
        self.gridLayout_2.addWidget(self.general_scale_graph, 1, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setRowStretch(0, 5)
        self.gridLayout_2.setRowStretch(1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.verticalLayout_23.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_gvs_dump_button = QtWidgets.QAction(MainWindow)
        self.open_gvs_dump_button.setObjectName("open_gvs_dump_button")
        self.open_oculograph_dump_button = QtWidgets.QAction(MainWindow)
        self.open_oculograph_dump_button.setObjectName("open_oculograph_dump_button")
        self.exit_button = QtWidgets.QAction(MainWindow)
        self.exit_button.setObjectName("exit_button")
        self.menu.addAction(self.open_gvs_dump_button)
        self.menu.addAction(self.open_oculograph_dump_button)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_button)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Эксперимент"))
        self.experement_number_combobox.setItemText(0, _translate("MainWindow", "Эксперимент 1"))
        self.experement_number_combobox.setItemText(1, _translate("MainWindow", "Эксперимент 2"))
        self.experement_number_combobox.setItemText(2, _translate("MainWindow", "Эксперимент 3"))
        self.recording_checkbox.setText(_translate("MainWindow", "Записать видео"))
        self.start_experiment_button.setText(_translate("MainWindow", "Начать эксперимент"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Общий график"))
        self.label.setText(_translate("MainWindow", "Магнитометр"))
        self.inverse_magnetometer.setText(_translate("MainWindow", "Инверсия"))
        self.label_15.setText(_translate("MainWindow", "Масштаб по Y"))
        self.label_29.setText(_translate("MainWindow", "Смещение по Y"))
        self.select_magnitometer_axis.setItemText(0, _translate("MainWindow", "Ось X"))
        self.select_magnitometer_axis.setItemText(1, _translate("MainWindow", "Ось Y"))
        self.select_magnitometer_axis.setItemText(2, _translate("MainWindow", "Ось Z"))
        self.label_16.setText(_translate("MainWindow", "Гироскоп"))
        self.inverse_gyroscope.setText(_translate("MainWindow", "Инверсия"))
        self.label_17.setText(_translate("MainWindow", "Масштаб по Y"))
        self.label_28.setText(_translate("MainWindow", "Смещение по Y"))
        self.select_gyroscope_axis.setItemText(0, _translate("MainWindow", "Ось X"))
        self.select_gyroscope_axis.setItemText(1, _translate("MainWindow", "Ось Y"))
        self.select_gyroscope_axis.setItemText(2, _translate("MainWindow", "Ось Z"))
        self.label_18.setText(_translate("MainWindow", "Акселерометр"))
        self.inverse_accelerometer.setText(_translate("MainWindow", "Инверсия"))
        self.label_19.setText(_translate("MainWindow", "Масштаб по Y"))
        self.label_24.setText(_translate("MainWindow", "Смещение по Y"))
        self.select_accelerometer_axis.setItemText(0, _translate("MainWindow", "Ось X"))
        self.select_accelerometer_axis.setItemText(1, _translate("MainWindow", "Ось Y"))
        self.select_accelerometer_axis.setItemText(2, _translate("MainWindow", "Ось Z"))
        self.label_20.setText(_translate("MainWindow", "Окулограф"))
        self.inverse_oculograph_x.setText(_translate("MainWindow", "Инверсия X"))
        self.inverse_oculograph_y.setText(_translate("MainWindow", "Инверсия Y"))
        self.label_21.setText(_translate("MainWindow", "Масштаб X по Y"))
        self.label_22.setText(_translate("MainWindow", "Масштаб Y по Y"))
        self.select_oculograph_axis.setItemText(0, _translate("MainWindow", "Ось X и Y"))
        self.select_oculograph_axis.setItemText(1, _translate("MainWindow", "Ось X"))
        self.select_oculograph_axis.setItemText(2, _translate("MainWindow", "Ось Y"))
        self.label_23.setText(_translate("MainWindow", "Смещение по X"))
        self.hidden_leds.setText(_translate("MainWindow", "Скрыть светодиоды"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Вычесляемые значения"))
        self.delta.setText(_translate("MainWindow", "Дельта:"))
        self.delta_2.setText(_translate("MainWindow", "Визир 1:"))
        self.delta_3.setText(_translate("MainWindow", "Визир 2:"))
        self.delta_4.setText(_translate("MainWindow", "X;Y;:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Окулограф"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ГВС"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Общий"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.open_gvs_dump_button.setText(_translate("MainWindow", "Открыть дамп ГВС"))
        self.open_oculograph_dump_button.setText(_translate("MainWindow", "Открыть дамп окулогрофа"))
        self.exit_button.setText(_translate("MainWindow", "Выход"))
from pyqtgraph import GraphicsLayoutWidget, PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
