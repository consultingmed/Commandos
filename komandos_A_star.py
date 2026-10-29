import random
from collections import deque
import heapq

mapa = []
move_map = {}

def data():
	
	File = open ('zad_input.txt', 'r', encoding = 'utf-8')
	
	start = set()
	finish = set()
	
	for ind, line in enumerate(File):
		line.strip()
		mapa.append(line)

		for i in range(len(line)):
			if line[i] == 'G' or line[i] == 'B':
				finish.add((ind, i))
			if line[i] == 'S' or line[i] == 'B':
				start.add((ind, i))
	
	#print(finish)
	#print(start)		
	#print(mapa)	
	
	return start, finish

def pre_processing():

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for r in range(len(mapa)):
        for c in range(len(mapa[r])):
            if mapa[r][c] != '#':
                for m_idx, (dr, dc) in enumerate(directions):
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < len(mapa) and 0 <= nc < len(mapa[nr]) and mapa[nr][nc] != '#':
                        move_map[((r, c), m_idx)] = (nr, nc)
                    else:
                        move_map[((r, c), m_idx)] = (r, c)
def obraz(s, move_nr):
    return frozenset(move_map[(poz, move_nr)] for poz in s)

def end(start, finish):
    return start.issubset(finish)
    
def heura(finish):

    dists = {}
    q = deque()
    
    for x, y in finish:
        dists[(x, y)] = 0
        q.append((x, y))
        
    while q:
        x, y = q.popleft()
        d = dists[(x, y)]
        
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if mapa[nx][ny] != '#' and (nx, ny) not in dists:
                dists[(nx, ny)] = d + 1
                q.append((nx, ny))
    return dists

def A_star(start, finish):
	
	visited = {}
	q = []
	heapq.heappush(q,(0, (start, "")))
	dist = heura(finish)

	while q:
		price, (s, p) = heapq.heappop(q)
		#print(price)
		
		fs = frozenset(s)
		if fs in visited and visited[fs] <= len(p):
			continue
		visited[fs] = len(p)
				
		if end(s, finish):
			return p
		
		for i in range(4):
			new_s = obraz(s, i)	
			k = 0
			for j in new_s:
				k = max(dist[j], k)
			heapq.heappush(q, (len(p) + k + 1, (new_s, p + str(i))))

	return ""

def convert(path):

	npath = ""
	
	for i in path:
		if i == '1':
			npath = npath + 'R'
		if i == '3':
			npath = npath + 'L'
		if i == '0':
			npath = npath + 'D'
		if i == '2':
			npath = npath + 'U'
	return npath

def start():

	start, finish = data()
	
	pre_processing()

	path = A_star(start, finish)	
	
	#print('\n', '\n', convert(path))
	
	fpath = convert(path)

	#print(fpath)

	f = open('zad_output.txt', 'w', encoding = 'utf-8')
	f.write(fpath)
	#return(fpath)

start()	

