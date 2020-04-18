import serial

class DMM():

    ser = serial.Serial()

    """
    Class construction
    :argument com: com port where dmm is connected
    """
    def __init__(self, com):
        self.com = com

    def initialization(self):
        self.ser.port = self.com
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE

    def test(self):
            self.sel.open()
            is_open = self.ser.is_open()
            self.ser.close()
            return is_open

