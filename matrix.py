import copy


class Matrix:

	def __init__(self, rows):

		if not rows:
			raise ValueError("Matrix can't be empty")

		row_length = len(rows[0])
		for row in rows:
			if len(row) != row_length:
				raise ValueError('All rows of the matrix must have the same length!')
		self.rows = copy.deepcopy(rows)


	def same_size(self, other):
		if not isinstance(other, Matrix):
			return False
		return len(self.rows) == len(other.rows) and len(self.rows[0]) == len(other.rows[0])

	def __add__(self, other):
			
			if not self.same_size(other):
				raise ValueError('Matrices must have the same dimensions')

			result = []

			for i in range(len(self.rows)):
				row = []
				for j in range(len(self.rows[i])):
					row.append(self.rows[i][j] + other.rows[i][j])
				result.append(row)

			return type(self)(result)
	

	def __sub__(self, other):
			
		if not self.same_size(other):
			raise ValueError('Matrices must have the same dimensions')

		result = []

		for i in range(len(self.rows)):
			row = []
			for j in range(len(self.rows[i])):
				row.append(self.rows[i][j] - other.rows[i][j])
			result.append(row)

		return type(self)(result)
	
	@property
	def transpose(self):

		result = []
		for i in range(len(self.rows[0])):
			row = []
			for j in range(len(self.rows)):
				row.append(self.rows[j][i])
			result.append(row)

		return type(self)(result)
	

	def __str__(self):
		return str(self.rows)
	
	def __eq__(self, other):

		if not isinstance(other, Matrix):
			return False
		return self.rows == other.rows
	
	def is_square(self):
		return len(self.rows) == len(self.rows[0])


	def __mul__(self, other):

		if not isinstance(other, (int, float)):
				raise TypeError('Only number!')
		result = []
		for i in range(len(self.rows)):
			row = []
			for j in range(len(self.rows[i])):
				row.append(self.rows[i][j] * other)
			result.append(row)
		return type(self)(result)
		
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __matmul__(self, other):
       
		if len(self.rows[0]) != len(other.rows):
			raise ValueError("The number of columns of the first matrix must match the number of rows of the second matrix!")

		result = []
		for i in range(len(self.rows)):          
			row = []
			for j in range(len(other.rows[0])):  
				s = 0
				for k in range(len(other.rows)):  
					s += self.rows[i][k] * other.rows[k][j]
				row.append(s)
			result.append(row)

		return type(self)(result)
	
	def __imul__(self, other):
		if not isinstance(other,int):
			raise TypeError('Can multiply only by a number!')
		for i in range(len(self.rows)):
			for j in range(len(self.rows[i])):
				self.rows[i][j] *= other
		return self
	
	

class SquareMatrix(Matrix):
    def __init__(self, rows):
        super().__init__(rows)        
        if not self.is_square():      
            raise ValueError("SquareMatrix must be square")
    
    @property
    def determinant(self):
        if len(self.rows) == 2:
            return self.rows[0][0]*self.rows[1][1] - self.rows[0][1]*self.rows[1][0]
        else:
            raise NotImplementedError("Determinant only implemented for 2x2 for now")


	

A = Matrix([[1,  2,  3], [4,  5, 6],])
B = Matrix([[10, 20, 30], [40, 50, 60],])
V = Matrix([[1, 2], [2, 4], [2, 2]])
C = A + B
D = B - A
print(C.rows)
print(D.rows)
E = A.transpose
print(E)
print(A == B)
print(A * 2)
print(2 * A)
print(A)
print(A @ V)
print(A * 10)

# N = SquareMatrix([[10, 2], [2, 3]])
# print(N.determinant)


