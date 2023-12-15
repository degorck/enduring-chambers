"""
Wheel filter for QComboBox and QDateEdit
"""
from PySide6 import QtCore

class WheelEventFilter(QtCore.QObject):
    """
    WheelEventFilter class
    """
    def eventFilter(self, obj, ev):
        """
        Filters QComboBox and QDateEdit wheel event
        """
        if obj.inherits("QComboBox") and ev.type() == QtCore.QEvent.Wheel:
            return True
        if obj.inherits("QDateEdit") and ev.type() == QtCore.QEvent.Wheel:
            return True
        return False
