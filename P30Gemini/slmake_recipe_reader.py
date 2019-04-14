import golly as g 

def recipe():
	res = ""
	i = 0
	prev = 0 
	
	while True:
		i += 1
		y = int(128 * i) + 1
		cells = g.getcells([-1500+y, y, 2 * 1500, 3])
		
		if len(cells) == 0:
			break 
		
		x = cells[0]
		y = cells[1]
		cur = x - y 
		
		if g.getcell(x + 2, y) == 0:
			res += "O" + str(cur) + " "
		else:
			res += "E" + str(cur - 1) + " "
		
		prev = cur 
		
	return	res
	
g.setclipstr(recipe())
