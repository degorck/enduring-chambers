from PySide6 import QtCore

class WheelEventFilter(QtCore.QObject):
    def eventFilter(self, obj, ev):
        if obj.inherits("QComboBox") and ev.type() == QtCore.QEvent.Wheel:
            return True
        if obj.inherits("QDateEdit") and ev.type() == QtCore.QEvent.Wheel:
            return True
        return False
