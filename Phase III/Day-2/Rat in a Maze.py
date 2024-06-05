def findAllWays(x, y, matrix, N, path, visited):
	# Border checks
	if x < 0 or x == N or y < 0 or y == N:
		return
 
	# Condition to check whether we can traverse via those coordinates or not
	if matrix[x][y] == 0 or visited[x][y] == True:
		return
 
	# Condition to check whether we've reached our final coordinates or not
	if x == N - 1 and y == N - 1:
		print("".join(path))
		return
 
	visited[x][y] = True 
 
	# Top Direction
	path.append("U")
	findAllWays(x - 1, y, matrix, N, path, visited)
	path.pop()
 
	# Bottom Direction
	path.append("D")
	findAllWays(x + 1, y, matrix, N, path, visited)
	path.pop()
 
	# Left Direction 
	path.append("L")
	findAllWays(x, y - 1, matrix, N, path, visited)
	path.pop()
 
	# Right Direction
	path.append("R")
	findAllWays(x, y + 1, matrix, N, path, visited)
	path.pop()
	visited[x][y]=False
 
 
path = []
visited = []
matrix = [[1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
n = len(matrix)
 
for i in range(n):
	eachRow = []
	for j in range(n):
		eachRow.append(False)
	visited.append(eachRow)
findAllWays(0, 0, matrix, n, path, visited)
