"""
Problema
Todos los a ̃nos al iniciar el a ̃no acad ́emico se realiza una ceremonia de bienvenida para los estudiantes
de Ingenier ́ıa Civil en Bioinform ́atica, donde se premia a los estudiantes sobresalientes del a ̃no anterior. Este
a ̃no se realiz ́o en nuestro laboratorio de computaci ́on y estuvo cargada de espect ́aculos art ́ısticos, contando
con una destacada orquesta que acompa ̃n ́o la jornada con la mejor m ́usica y alegr ́ıa.
Durante la ceremonia se entreg ́o un diploma a cada uno de los participantes que obtuvo al menos el tercer
lugar en rendimiento acad ́emico (mejores notas) en las asignaturas de la carrera como lo son: Programaci ́on
Avanzada, Miner ́ıa de datos, Bioinform ́atica estructural, F ́ısica, etc.
Por protocolo COVID, para hacer la entrega de los diplomas se hizo pasar uno a uno a los estudiantes en
una fila. Lamentablemente era muy complicado para los estudiantes situarse en el mismo orden en que los
llamaban y por lo tanto muchas personas recibieron un diploma que no les correspond ́ıa. Naturalmente los
estudiantes quisieron ponerse de acuerdo para intercambi+ar los diplomas y que todos se fueran a casa con el
o los suyo.
Afortunadamente despu ́es de la ceremonia los estudiantes fueron invitados a un cocktel y por lo tanto
ten ́ıan todo el tiempo necesario para intercambiar los diplomas. La tarea no fue sencilla, pues no todos los
estudiantes ten ́ıan la misma cantidad de diplomas ya que algunos estaban en m ́as de una asignatura dentro
del tercer lugar de rendimiento.
Diremos que si el diploma de un participante X est ́a en posesi ́on de un participante Y, entonces X puede
intercambiarlo con Y, ahora si ese Y no le pertenece el diploma debe intercambiarlo con otro estudiante. Esto
repetir ́a hasta que todos los estudiantes tengan el diploma que les pertenece.
"""
import random
from estudiante import Estudiante
from asignatura import Asignatura
from diploma import Diploma
def main():
    #objetos diplomas, estudiantes y cursos
    """
    estudiante = Estudiante("Pablito")
    fisica = Asignatura("Fisica")¿¿
    sebastian = Estudiante("Sebastian")
    sebastian.asignatura = fisica
    estudiante.asignatura = fisica
    for i in estudiante.asignatura:
        print(i)
    for i in sebastian.asignatura:
        print(i)
    """
    programacion = Asignatura("Programacion")
    fisica = Asignatura("Fisica")
    quimica = Asignatura("Quimica")

    lista = [Estudiante("Pablito"), Estudiante("Sebastian"),
            Estudiante("Juan")]
    lista_asignatura = [programacion, fisica, quimica]
    diplomas = []

    for i in lista:
        i.asignatura = random.choice(lista_asignatura)
    for i in lista:
        #print(i.asignatura[0].nombre)
        for x in i.asignatura:
            print(x.nombre)
    
    diplomas = []
    for i in lista:
        for j in i.asignatura:
            diplomas.append(Diploma(i,j))
    print(diplomas)
    

if __name__ == '__main__':
    main()
