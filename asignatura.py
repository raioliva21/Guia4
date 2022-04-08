class Asignatura():
    """docstring for Asignatura."""

    def __init__(self, nombre):
        self._nombre = nombre


    @property
    def nombre(self):
        return self._nombre
