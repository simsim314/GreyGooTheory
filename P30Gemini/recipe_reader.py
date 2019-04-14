import golly as g 


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
		
		if len(g.getcells([dx + x, x, 3, 3])) == 0:
			res += "0"
		else:
			res += "1"
			
	return	res.strip("0")
	

path = r'C:\Users\SimSim314\Documents\GitHub\GreyGooTheory\P30Gemini'

file = open(path + r'\shoot.recipe.txt', 'w')
file.write("xy-O-type-O:-1:" + ":" + recipe(0) + "\n")	
file.write("xy-E-type-O:-10:" + ":" + recipe(1 * 100) + "\n")	
file.write("xy-O-type-E:-12:" + ":" + recipe(4 * 100) + "\n")	
file.write("xy-E-type-E:-2:" + ":" + recipe(11 * 100) + "\n")	
file.close()
