# 백준 18352 특정 거리의 도시 찾기
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	start, end = map(int, input().split())
	graph[start].append(end)
	
dist = [-1] * (N + 1)

def bfs(start):
	queue = deque()
	queue.append(start)
	dist[start] = 0
	while queue:
		cur_node = queue.popleft()
		for next_node in graph[cur_node]:
			if dist[next_node] == -1:
				queue.append(next_node)
				dist[next_node] = dist[cur_node] + 1

	flag = False
	for i in range(N + 1):
		if dist[i] == K:
			print(i)
			flag = True
	
	if flag == False:
		print(-1)

bfs(X)