#from estudiante import Estudiante
from asignatura import Asignatura

class Diploma():
    """docstring for Diploma."""

    def __init__(self, estudiante, asignatura):
        self._estudiante = estudiante
        self._asignatura = asignatura
        pass

    @property
    def estudiante(self):
        return self._estudiante
    
    @estudiante.setter
    def estudiante(self, nombre):
        if isinstance(nombre, Estudiante):
            self._estudiante = nombre
        else:
            print("no pertenece a clase adecuada")
    
    @property
    def asignatura(self):
        return self._asignatura
    
    @asignatura.setter
    def asignatura(self,asignatura):
        if isinstance(asignatura, Asignatura):
            self._asignatura = asignatura
        else:
            print("no pertenece a clase adecuada")
    

