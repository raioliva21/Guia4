from asignatura import Asignatura
from diploma import Diploma
class Estudiante():
    """docstring for estudiante."""

    def __init__(self, nombre):
        self._nombre = nombre
        self._asignatura = []
        self._diploma = []
        pass
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            print("El tipo de dato no corresponde")
    @property
    def asignatura(self):
        return self._asignatura
    @asignatura.setter
    def asignatura(self, asignatura):
        if isinstance(asignatura, Asignatura):
            self._asignatura.append(asignatura)
        else:
            print("El tipo de dato no corresponde")
    
    @property
    def diploma(self):
        return self._diploma
    @diploma.setter
    def diploma(self, diploma):
        if isinstance(diploma, Diploma):
            self._diploma.append(diploma)
        else:
            print("El tipo de dato no corresponde")
