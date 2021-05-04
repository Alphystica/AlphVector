'''
VECTORES
Desarrollado por alphydev - Alphystica Developement Departament
'''

from src.Points.points import Point
from math import cos, sin

class Vector(Point):
    '''
    # Class Vector(*coordinates)
    Clase para crear vectores
    >>> V = Vector (5,0,-2)
    >>> V.length()
    5.385164807134504
    '''
    @classmethod
    def byPoints (cls, fistPoint:Point, endPoint:Point):
        '''
        # Vector definido por puntos
        Vector.byPoints(fistPoint:Point, endPoint:Point)
        Vector definido con direccion del vector de "fistPoint" a "endPoint"
        >>> A = Point(1,5,4)
        >>> B = Point(3,5,2)
        >>> V = Point.byPoints(A,B)
        [2,0,-2]
        '''
        __dif = endPoint - fistPoint
        __auxVector = Vector()
        for i in range(__dif.dimension()):
            __auxVector._Point__notation.append(__dif._Point__notation[i])
        return __auxVector
    
    @classmethod
    def byElements(cls, length, *angles):
        '''
        # Vector definido por sus elementos
        Vector.byElements(length, *angles)
        Definiendo la longitud del vector de dos dimensiones y los angulos definidos entre el vector y el eje X.
        Definiendo la longitud del vector de tres dimensiones y los angulos definidos entre el vector,el eje X, el eje Z.
        
        >>> V = Vector.byElements(5, 0.927295218)
        [3,4]
        '''
        __coordinates = []
        __auxVector = Vector()
        if (len(angles) == 1):
            __auxVector._Point__notation.append(length * cos(angles[0]))
            __auxVector._Point__notation.append(length * sin(angles[0]))
            return __auxVector
        elif (len(angles) == 2):
            __auxVector._Point__notation.append(length * sin(angles[0])* cos(angles[1]))
            __auxVector._Point__notation.append(length * sin(angles[0])* sin(angles[1]))
            __auxVector._Point__notation.append(length * cos(angles[0]))
            return __auxVector
        else:
            raise ValueError ("Dimension not correct")
        
    def length(self):
        '''
        # metodo length
        Retorna el modulo o tamaño del vector 
        '''
        __sumSquares = 0
        for x in self._Point__notation:
            __sumSquares += x**2
        return __sumSquares**0.5
    
    def __add__(self, other):
        __aux = super().__add__(other)
        __auxVector = Vector()

        for i in range(__aux.dimension()):
            __auxVector._Point__notation.append(__aux._Point__notation[i])
        
        return __auxVector
    
    def __sub__(self, other):
        __aux = super().__sub__(other)
        __auxVector = Vector()
        for i in range(__aux.dimension()):
            __auxVector._Point__notation.append(__aux._Point__notation[i])
        
        return __auxVector