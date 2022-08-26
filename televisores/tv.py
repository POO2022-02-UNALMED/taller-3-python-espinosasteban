class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control

    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, volumen):
        self._volumen = volumen

    def getVolumen(self):
        return self._volumen

    def setCanal(self, canal):
        if 0 <= canal <= 120 and self._estado:
            self._canal = canal

    def getCanal(self):
        return self._canal

    def getNumTV(self):
        return self._numTV

    def setNumTV(self, numTV):
        self._numTV = numTV

    def canalUp(self):
        if (canal >= 0 and canal < 120 and self._estado):
            self._canal += 1

    def canalDown(self):
        if (canal > 0 and canal <= 120 and self._estado)
            self._canal -= 1

    def volumenUp(self):
        if (0 <= self._volumen < 7 and self._estado)
            self._volumen += 1

    def volumenDown(self):
        if (0 < self._volumen <= 7 and self._estado)
            self._volumen -= 1






