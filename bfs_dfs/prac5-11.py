# 5-10 음료수 얼려먹기
from collections import deque

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력
graph = []
for i in range(n):
	graph.append(list(map(int, input())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	queue = deque()
	queue.append((x, y))

	while queue:
		x, y = queue.popleft()
		graph[x][y] = 1	#visit
		
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			if graph[nx][ny] == 1:
				continue

			queue.append((nx, ny))
			
cnt = 0
for x in range(n):
	for y in range(m):
		if graph[x][y] == 0:
			bfs(x, y)
			cnt += 1

print(cnt)