import golly as g 
import random

glds = [[],[]]

glds[0] = g.parse("3o$o$bo!")
glds[1] = g.evolve(g.parse("3o$o$bo!"), 2)
#blck = g.parse("2o$2o!", -4, 0)

def place_glider(i, dx):
	if i%2 == 0:
		g.putcells(glds[0], 15 * int(i/2) + dx, 15 * int(i/2))
	else:
		g.putcells(glds[1], 8 + 15 * int(i/2) + dx, 8 + 15 * int(i/2))
	
def recipe(dx):
	res = ""
	for i in range(500):
		x = int(i * 7.5)
		
		if len(g.getcells([dx + x + 5, x, 3, 3])) == 0:
			res += "0"
		else:
			res += "1"
			
	return	res.strip("0")

path = r'C:\Users\SimSim314\Documents\GitHub\GreyGooTheory\P30Gemini'

def save(dists):
	file = open(path + r'\move.recipe.txt', 'w')
	
	for i in range(-100, 101):
		if i in dists:
			file.write(str(i) + ":" + dists[i] + "\n")
	
	file.close()

dists = {}

for i in range(100):
	rec = recipe(i * 100)
	if len(rec) > 0:
		dists[i - 20] = rec
	

while True: 

	x1 = random.randint(-100,101)
	x2 = random.randint(-100,101)
	
	if x1 in dists and x2 in dists:
		d = x1 + x2
		if d <= 100 and d >= -100:
			if d in dists:
				if len(dists[d]) > len(dists[x1])+len(dists[x2]) + 4:
					dists[d] = dists[x1] + "0000" + dists[x2]
					save(dists)
				
			else:
				dists[d] = dists[x1]  + "0000" + dists[x2]
				save(dists)
				
				
		
		
		