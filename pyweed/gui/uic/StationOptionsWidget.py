# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/uic/StationOptionsWidget.ui'
#
# Created: Mon Feb 27 16:28:39 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StationOptionsWidget(object):
    def setupUi(self, StationOptionsWidget):
        StationOptionsWidget.setObjectName(_fromUtf8("StationOptionsWidget"))
        StationOptionsWidget.resize(309, 703)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StationOptionsWidget.sizePolicy().hasHeightForWidth())
        StationOptionsWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(StationOptionsWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.SNCLGroupBox = QtGui.QGroupBox(StationOptionsWidget)
        self.SNCLGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SNCLGroupBox.setObjectName(_fromUtf8("SNCLGroupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.SNCLGroupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(4)
        self.formLayout.setVerticalSpacing(1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.networkLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.networkLabel.setObjectName(_fromUtf8("networkLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.networkLabel)
        self.networkLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.networkLineEdit.setObjectName(_fromUtf8("networkLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.networkLineEdit)
        self.stationLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.stationLineEdit.setObjectName(_fromUtf8("stationLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.stationLineEdit)
        self.locationLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.locationLabel.setObjectName(_fromUtf8("locationLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.locationLabel)
        self.locationLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.locationLineEdit.setObjectName(_fromUtf8("locationLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.locationLineEdit)
        self.channelLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.channelLabel.setObjectName(_fromUtf8("channelLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.channelLabel)
        self.channelLineEdit = QtGui.QLineEdit(self.SNCLGroupBox)
        self.channelLineEdit.setObjectName(_fromUtf8("channelLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.channelLineEdit)
        self.stationLabel = QtGui.QLabel(self.SNCLGroupBox)
        self.stationLabel.setObjectName(_fromUtf8("stationLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.stationLabel)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.SNCLGroupBox)
        self.timeGroupBox = QtGui.QGroupBox(StationOptionsWidget)
        self.timeGroupBox.setObjectName(_fromUtf8("timeGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.timeGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.timeBetweenRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeBetweenRadioButton.setEnabled(True)
        self.timeBetweenRadioButton.setChecked(True)
        self.timeBetweenRadioButton.setObjectName(_fromUtf8("timeBetweenRadioButton"))
        self.verticalLayout_2.addWidget(self.timeBetweenRadioButton)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(4)
        self.formLayout_2.setVerticalSpacing(1)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.starttimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.starttimeLabel.setObjectName(_fromUtf8("starttimeLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.starttimeLabel)
        self.starttimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.starttimeDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.starttimeDateTimeEdit.setSizePolicy(sizePolicy)
        self.starttimeDateTimeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.starttimeDateTimeEdit.setCalendarPopup(True)
        self.starttimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.starttimeDateTimeEdit.setObjectName(_fromUtf8("starttimeDateTimeEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.starttimeDateTimeEdit)
        self.endtimeLabel = QtGui.QLabel(self.timeGroupBox)
        self.endtimeLabel.setObjectName(_fromUtf8("endtimeLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.endtimeLabel)
        self.endtimeDateTimeEdit = QtGui.QDateTimeEdit(self.timeGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endtimeDateTimeEdit.sizePolicy().hasHeightForWidth())
        self.endtimeDateTimeEdit.setSizePolicy(sizePolicy)
        self.endtimeDateTimeEdit.setProperty("showGroupSeparator", False)
        self.endtimeDateTimeEdit.setCalendarPopup(True)
        self.endtimeDateTimeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.endtimeDateTimeEdit.setObjectName(_fromUtf8("endtimeDateTimeEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.endtimeDateTimeEdit)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.time30DaysPushButton = QtGui.QPushButton(self.timeGroupBox)
        self.time30DaysPushButton.setObjectName(_fromUtf8("time30DaysPushButton"))
        self.horizontalLayout_7.addWidget(self.time30DaysPushButton)
        self.time1YearPushButton = QtGui.QPushButton(self.timeGroupBox)
        self.time1YearPushButton.setObjectName(_fromUtf8("time1YearPushButton"))
        self.horizontalLayout_7.addWidget(self.time1YearPushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_3 = QtGui.QFrame(self.timeGroupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.timeFromEventsRadioButton = QtGui.QRadioButton(self.timeGroupBox)
        self.timeFromEventsRadioButton.setObjectName(_fromUtf8("timeFromEventsRadioButton"))
        self.verticalLayout_2.addWidget(self.timeFromEventsRadioButton)
        self.verticalLayout.addWidget(self.timeGroupBox)
        self.locationGroupBox = QtGui.QGroupBox(StationOptionsWidget)
        self.locationGroupBox.setObjectName(_fromUtf8("locationGroupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.locationGlobalRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationGlobalRadioButton.setChecked(True)
        self.locationGlobalRadioButton.setObjectName(_fromUtf8("locationGlobalRadioButton"))
        self.verticalLayout_4.addWidget(self.locationGlobalRadioButton)
        self.line_4 = QtGui.QFrame(self.locationGroupBox)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_4.addWidget(self.line_4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.locationRangeRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationRangeRadioButton.setChecked(False)
        self.locationRangeRadioButton.setObjectName(_fromUtf8("locationRangeRadioButton"))
        self.horizontalLayout_8.addWidget(self.locationRangeRadioButton)
        spacerItem1 = QtGui.QSpacerItem(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.drawLocationRangeToolButton = QtGui.QToolButton(self.locationGroupBox)
        self.drawLocationRangeToolButton.setCheckable(True)
        self.drawLocationRangeToolButton.setObjectName(_fromUtf8("drawLocationRangeToolButton"))
        self.horizontalLayout_8.addWidget(self.drawLocationRangeToolButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(1, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.locationRangeNorthDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeNorthDoubleSpinBox.setMinimum(-90.0)
        self.locationRangeNorthDoubleSpinBox.setMaximum(90.0)
        self.locationRangeNorthDoubleSpinBox.setObjectName(_fromUtf8("locationRangeNorthDoubleSpinBox"))
        self.horizontalLayout_4.addWidget(self.locationRangeNorthDoubleSpinBox)
        spacerItem3 = QtGui.QSpacerItem(1, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.locationRangeWestDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeWestDoubleSpinBox.setMinimum(-180.0)
        self.locationRangeWestDoubleSpinBox.setMaximum(180.0)
        self.locationRangeWestDoubleSpinBox.setObjectName(_fromUtf8("locationRangeWestDoubleSpinBox"))
        self.horizontalLayout.addWidget(self.locationRangeWestDoubleSpinBox)
        self.locationRangeEastDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeEastDoubleSpinBox.setMinimum(-180.0)
        self.locationRangeEastDoubleSpinBox.setMaximum(180.0)
        self.locationRangeEastDoubleSpinBox.setObjectName(_fromUtf8("locationRangeEastDoubleSpinBox"))
        self.horizontalLayout.addWidget(self.locationRangeEastDoubleSpinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(1, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.locationRangeSouthDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.locationRangeSouthDoubleSpinBox.setMinimum(-90.0)
        self.locationRangeSouthDoubleSpinBox.setMaximum(90.0)
        self.locationRangeSouthDoubleSpinBox.setObjectName(_fromUtf8("locationRangeSouthDoubleSpinBox"))
        self.horizontalLayout_5.addWidget(self.locationRangeSouthDoubleSpinBox)
        spacerItem5 = QtGui.QSpacerItem(1, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        spacerItem6 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.locationGroupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.locationDistanceFromPointRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationDistanceFromPointRadioButton.setEnabled(True)
        self.locationDistanceFromPointRadioButton.setObjectName(_fromUtf8("locationDistanceFromPointRadioButton"))
        self.horizontalLayout_9.addWidget(self.locationDistanceFromPointRadioButton)
        spacerItem7 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.drawDistanceFromPointToolButton = QtGui.QToolButton(self.locationGroupBox)
        self.drawDistanceFromPointToolButton.setCheckable(True)
        self.drawDistanceFromPointToolButton.setObjectName(_fromUtf8("drawDistanceFromPointToolButton"))
        self.horizontalLayout_9.addWidget(self.drawDistanceFromPointToolButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(24, -1, -1, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.distanceFromPointMinRadiusDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointMinRadiusDoubleSpinBox.setMinimum(0.0)
        self.distanceFromPointMinRadiusDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointMinRadiusDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointMinRadiusDoubleSpinBox"))
        self.horizontalLayout_14.addWidget(self.distanceFromPointMinRadiusDoubleSpinBox)
        self.label_2 = QtGui.QLabel(self.locationGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_14.addWidget(self.label_2)
        self.distanceFromPointMaxRadiusDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setMinimum(0.0)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointMaxRadiusDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointMaxRadiusDoubleSpinBox"))
        self.horizontalLayout_14.addWidget(self.distanceFromPointMaxRadiusDoubleSpinBox)
        self.label_8 = QtGui.QLabel(self.locationGroupBox)
        self.label_8.setEnabled(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_14.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_6 = QtGui.QLabel(self.locationGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_15.addWidget(self.label_6)
        self.distanceFromPointEastDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointEastDoubleSpinBox.setMinimum(-180.0)
        self.distanceFromPointEastDoubleSpinBox.setMaximum(180.0)
        self.distanceFromPointEastDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointEastDoubleSpinBox"))
        self.horizontalLayout_15.addWidget(self.distanceFromPointEastDoubleSpinBox)
        self.label_14 = QtGui.QLabel(self.locationGroupBox)
        self.label_14.setEnabled(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_15.addWidget(self.label_14)
        self.distanceFromPointNorthDoubleSpinBox = QtGui.QDoubleSpinBox(self.locationGroupBox)
        self.distanceFromPointNorthDoubleSpinBox.setMinimum(-90.0)
        self.distanceFromPointNorthDoubleSpinBox.setMaximum(90.0)
        self.distanceFromPointNorthDoubleSpinBox.setObjectName(_fromUtf8("distanceFromPointNorthDoubleSpinBox"))
        self.horizontalLayout_15.addWidget(self.distanceFromPointNorthDoubleSpinBox)
        self.label_7 = QtGui.QLabel(self.locationGroupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_15.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem8 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.line = QtGui.QFrame(self.locationGroupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.locationFromEventsRadioButton = QtGui.QRadioButton(self.locationGroupBox)
        self.locationFromEventsRadioButton.setEnabled(True)
        self.locationFromEventsRadioButton.setObjectName(_fromUtf8("locationFromEventsRadioButton"))
        self.verticalLayout_4.addWidget(self.locationFromEventsRadioButton)
        self.verticalLayout.addWidget(self.locationGroupBox)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)

        self.retranslateUi(StationOptionsWidget)
        QtCore.QMetaObject.connectSlotsByName(StationOptionsWidget)
        StationOptionsWidget.setTabOrder(self.networkLineEdit, self.stationLineEdit)
        StationOptionsWidget.setTabOrder(self.stationLineEdit, self.locationLineEdit)
        StationOptionsWidget.setTabOrder(self.locationLineEdit, self.channelLineEdit)
        StationOptionsWidget.setTabOrder(self.channelLineEdit, self.timeBetweenRadioButton)
        StationOptionsWidget.setTabOrder(self.timeBetweenRadioButton, self.starttimeDateTimeEdit)
        StationOptionsWidget.setTabOrder(self.starttimeDateTimeEdit, self.endtimeDateTimeEdit)
        StationOptionsWidget.setTabOrder(self.endtimeDateTimeEdit, self.timeFromEventsRadioButton)
        StationOptionsWidget.setTabOrder(self.timeFromEventsRadioButton, self.locationFromEventsRadioButton)

    def retranslateUi(self, StationOptionsWidget):
        self.SNCLGroupBox.setTitle(_translate("StationOptionsWidget", "SNCL", None))
        self.networkLabel.setText(_translate("StationOptionsWidget", "Networks", None))
        self.networkLineEdit.setText(_translate("StationOptionsWidget", "_GSN", None))
        self.stationLineEdit.setText(_translate("StationOptionsWidget", "*", None))
        self.locationLabel.setText(_translate("StationOptionsWidget", "Locations", None))
        self.locationLineEdit.setText(_translate("StationOptionsWidget", "*", None))
        self.channelLabel.setText(_translate("StationOptionsWidget", "Channels", None))
        self.channelLineEdit.setText(_translate("StationOptionsWidget", "?HZ", None))
        self.stationLabel.setText(_translate("StationOptionsWidget", "Stations", None))
        self.timeGroupBox.setTitle(_translate("StationOptionsWidget", "Time", None))
        self.timeBetweenRadioButton.setText(_translate("StationOptionsWidget", "Between start and end times", None))
        self.starttimeLabel.setText(_translate("StationOptionsWidget", "Start", None))
        self.starttimeDateTimeEdit.setDisplayFormat(_translate("StationOptionsWidget", "yyyy-MM-dd hh:mm:ss", None))
        self.endtimeLabel.setText(_translate("StationOptionsWidget", "End", None))
        self.endtimeDateTimeEdit.setDisplayFormat(_translate("StationOptionsWidget", "yyyy-MM-dd hh:mm:ss", None))
        self.time30DaysPushButton.setText(_translate("StationOptionsWidget", "Last 30 days", None))
        self.time1YearPushButton.setText(_translate("StationOptionsWidget", "Last year", None))
        self.timeFromEventsRadioButton.setText(_translate("StationOptionsWidget", "Use the event time selection", None))
        self.locationGroupBox.setTitle(_translate("StationOptionsWidget", "Location", None))
        self.locationGlobalRadioButton.setText(_translate("StationOptionsWidget", "Global", None))
        self.locationRangeRadioButton.setText(_translate("StationOptionsWidget", "Within lat/lon box", None))
        self.drawLocationRangeToolButton.setText(_translate("StationOptionsWidget", "Draw on map", None))
        self.locationDistanceFromPointRadioButton.setText(_translate("StationOptionsWidget", "Distance from point", None))
        self.drawDistanceFromPointToolButton.setText(_translate("StationOptionsWidget", "Draw on map", None))
        self.label_2.setText(_translate("StationOptionsWidget", "-", None))
        self.label_8.setText(_translate("StationOptionsWidget", "degrees", None))
        self.label_6.setText(_translate("StationOptionsWidget", "from", None))
        self.label_14.setText(_translate("StationOptionsWidget", "E", None))
        self.label_7.setText(_translate("StationOptionsWidget", "N", None))
        self.locationFromEventsRadioButton.setText(_translate("StationOptionsWidget", "Use the event location bounds", None))

