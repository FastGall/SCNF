from functools import reduce

class DataError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printError(self):
        print("The element at [{0}][{1}] is NOT binary!".format(self.x, self.y))

class FormatError(Exception):
    def __init__(self, s):
        self.error = "The input is " + s
    def printError(self):
        print(self.error)

class RankError(Exception):
    def __init__(self, r):
        self.r = r
    def printError(self):
        print("The matrix is NOT full rank. (rank = {0})".format(self.r))

class BinMatrix:
    def __init__(self, m = [[1]]):
        self.m = m
        self.r_len = len(self.m) # row number
        self.c_len = len(self.m[0]) # column number

    def __convertMatrixToInt(self):
        return [int(reduce(lambda x , y: x + y, map(str, self.m[i])), 2) for i in range(self.r_len)]

    def __appendUnitMatrix(self):
        m_int = self.__convertMatrixToInt()
        return [(1 << (self.r_len + self.c_len - 1 - i)) ^ m_int[i] for i in range(self.r_len)]

    def __chooseElement(self, r, c, m_int):
        assert r <= c, "The row index can not exceed the column index in row-reduced echelon matrix."

        if c == self.c_len:
            return None
        else:
            mask = (1 << (self.c_len - 1 - c))
            temp = [(m_int[i] & mask) for i in range(r, self.r_len)]
            if mask not in temp:
                return self.__chooseElement(r, c + 1, m_int)
            else:
                return (temp.index(mask) + r, c)

    @staticmethod
    def __switchRows(r1, r2, m_int):
        temp = m_int[r1]
        m_int[r1] = m_int[r2]
        m_int[r2] = temp

    def __addRows(self, r, c, m_int):
        mask = (1 << (self.c_len - 1 - c))
        it = list(range(self.r_len))
        it.remove(r)
        for i in it:
            if m_int[i] & mask != 0:
                m_int[i] ^= m_int[r]

	
    def __isMatrix(self):
        if [len(l) for l in self.m].count(self.c_len) != self.r_len:
            raise FormatError("NOT a matrix!")
        else:
            pass

    def __isSquareMatrix(self):
        if [len(l) for l in self.m].count(self.r_len) != self.r_len:
            raise FormatError("NOT a Square matrix!")
        pass

    def __isBinary(self):
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                if self.m[i][j] not in [0,1]:
                    raise DataError(i, j)
                else:
                    pass

    def rank(self):
        self.__isMatrix()
        self.__isBinary()
        m_int = self.__convertMatrixToInt()
        r = 0
        c = 0
        for i in range(self.r_len):
            arg = self.__chooseElement(r, c, m_int)
            if arg != None:
                r_temp = arg[0]
                c = arg[1]
                self.__switchRows(r, r_temp, m_int)
                self.__addRows(r, c, m_int)
                r += 1
                c += 1
            else:
                return r
        return self.r_len

    def det(self):
        self.__isSquareMatrix()
        self.__isBinary()
        if self.rank() == self.r_len:
            return 1
        else:
            return 0

    def inv(self):
        self.__isSquareMatrix()
        self.__isBinary()
        m_adj = self.__appendUnitMatrix()
        r = 0
        c = 0
        for i in range(self.r_len):
            arg = self.__chooseElement(r, c, m_adj)
            if arg != None:
                r_temp = arg[0]
                c = arg[1]
                self.__switchRows(r, r_temp, m_adj)
                self.__addRows(r, c, m_adj)
                r += 1
                c += 1
            else:
                raise RankError(r)
        return [map(int, list(format((m_adj[i] >> self.c_len), "0" + str(self.r_len) + "b"))) for i in range(self.r_len)]
