'''
PUNTOS
Desarrollado por alphydev - Alphystica Developement Departament
'''

class Point:
    '''
    # class Point(*coordinates)
    Proporciona la creacion de puntos de cualquier dimension
    >>> P = Point(8,9,-2)
    [8,9,-2]

    '''
    def __init__(self, *coordinates) -> None:
        self.__notation = [] 
        for elem in coordinates:
            self.__notation.append(elem)

    def __str__(self) -> str:
        return str(self.__notation)

    def dimension(self) -> int:
        '''
        metodo que retorna la dimension del punto
        >>> P = Point(6,7,9)
        >>> P.dimension()
        3
        '''
        return len(self.__notation)

    def __repr__(self) ->str :
        return str(self.__notation)

    def __add__ (self, other):
        __suma = Point()
        if (self.dimension() > other.dimension()):
            for j in range(self.dimension()):
                if (j < other.dimension()):
                    __suma.__notation.append(self.__notation[j]+other.__notation[j])
                else:
                    __suma.__notation.append(self.__notation[j])
            return __suma
        elif (self.dimension() <= other.dimension()):
            for j in range(other.dimension()):
                if (j < self.dimension()):
                    __suma.__notation.append(self.__notation[j]+other.__notation[j])
                else:
                    __suma.__notation.append(other.__notation[j])
            return __suma
    
    def __sub__ (self, other):
        __resta = Point()
        if (self.dimension() > other.dimension()):
            for j in range(self.dimension()):
                if (j < other.dimension()):
                    __resta.__notation.append(self.__notation[j] - other.__notation[j])
                else:
                    __resta.__notation.append(self.__notation[j])
            return __resta
        elif (self.dimension() <= other.dimension()):
            for j in range(other.dimension()):
                if (j < self.dimension()):
                    __resta.__notation.append(self.__notation[j] - other.__notation[j])
                else:
                    __resta.__notation.append(-other.__notation[j])
            return __resta
            