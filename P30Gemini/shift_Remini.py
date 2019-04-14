import golly as g 

glds = [[],[]]

glds[0] = g.parse("3o$o$bo!")
glds[1] = g.evolve(g.parse("3o$o$bo!"), 2)
#blck = g.parse("2o$2o!", -4, 0)

def place_glider(i, dx, dy):
	if i%2 == 0:
		g.putcells(glds[0], 15 * int(i/2) + dx, 15 * int(i/2) + dy)
	else:
		g.putcells(glds[1], 8 + 15 * int(i/2) + dx, 8 + 15 * int(i/2) + dy)

		
class ArmP30:
	def __init__(self):
		self.recipe = ""
		self.move_recipes = {}
		self.shoot_recipes = {}
		self.arm_ext = -22
		
	def load_recipes(self):
		path = path = r'C:\Users\SimSim314\Documents\GitHub\GreyGooTheory\P30Gemini'

		file = open(path + r'\shoot.recipe.txt', 'r')
		
		for line in file:
			recipe = line.split(":")
			recipe[1] = int(recipe[1].replace("B", ""))
			recipe[2] = int(recipe[2].replace("G", ""))
			recipe[3] += "0"
			
			self.shoot_recipes[recipe[0]] = recipe 
		
		file.close()

		file = open(path + r'\move.recipe.txt', 'r')
		
		for line in file:
			recipe = line.split(":")
			self.move_recipes[-int(recipe[0])] = recipe[1] + "0"
		
		file.close()

	def apply_move(self, d):
		if d <= 100 and d >= -100:
			self.recipe += self.move_recipes[d]
			self.arm_ext += 2 * d
			
		else:
			if d > 100:
				self.recipe += self.move_recipes[100]
				self.arm_ext += 2 * 100
				self.apply_move(d - 100)
			else:
				self.recipe += self.move_recipes[-100]
				self.arm_ext -= 2 * 100
				self.apply_move(d + 100)
		
	def apply_shoot(self, d):
		recipe = self.shoot_recipes[d][3]
		self.recipe += recipe
		self.arm_ext += 2 * self.shoot_recipes[d][1]
		
	def place(self, x, y):
		idx = 0 
		for i in self.recipe:
			if i == "1":
				place_glider(idx, x, y)
			idx += 1
			
	def apply_slmake(self, slm, dR = 0):
		if slm[0] == "E":
			slm = int(slm.replace("E",""))
			slm += dR 
			
			if slm % 2 == 1:
				shoot = self.shoot_recipes["xy-E-type-E"]
			else: 
				shoot = self.shoot_recipes["xy-O-type-E"]
		
		else: 
			slm = int(slm.replace("O",""))
			slm += dR
			
			if slm % 2 == 1:
				shoot = self.shoot_recipes["xy-E-type-O"]
			else: 
				shoot = self.shoot_recipes["xy-O-type-O"]
		
		d = shoot[2]
		slm -= d
		move_d = (slm - self.arm_ext) / 2 
		self.apply_move(move_d)
		self.apply_shoot(shoot[0])

rle_BR_sl = '''
40b2o$40bo$38bobo$38b2o2$29b2o$6b2o20bobo$6b2o9b2o9b2o$17bobo$18b2o$b
2o42b2o$obo41bobo$bo41bobo$44bo5$133b2o$132bo2bo$46bo24bo61bobo$32b2o
11bobo22bobo61bo4bo$32b2o10bobo23b2o66bobo$44b2o93b2o3$66b2o$30bo35b2o
$29bobo$28bo2bo$29b2o3$38b2o$37bobo$26b2o10bo$25bobo$26bo40b2o$67bobo$
68b2o9$66b2o21bo$65bobo20bobo$65b2o20bo2bo$88b2o6$94bo$93bobo$93b2o$
65b2o$65b2o2$72bo$71bobo8b2o$70bobo8bobo$70b2o8bobo$81bo11$81bo$80bobo
$79bo2bo$80b2o3$89b2o$88bobo$89bo43$34b2o$33bobo$34bo41$69b2o$69bobo$
70bo!
'''

rle_TR_sl = '''
83b2o$83bobo$84bo3$86b2o$85bo2bo$86bobo$87bo37$48bo$47bobo$47b2o3$21b
2o33b2o$20bobo32bo2bo$21bo33bobo$56bo4$41b2o$26b2o12bobo$25bo2bo10bobo
$25bobo12bo$26bo2$b2o$obo$bo2$42bo$41bobo41bo$40bobo41bobo$40b2o42b2o$
67b2o$67bobo$57b2o9b2o9b2o$45b2o9bobo20b2o$45b2o9b2o18$85bo$84bobo8b2o
$83bobo8bobo$83b2o8bobo$94bo2$106bo$104b3o$72b2o29bo$71bobo29b2o$72bo
4$84b2o$84b2o$77b2o$76bo2bo20b2o$76bobo20bobo$77bo21b2o$70b2o$69bobo$
70bo6$97b2o$97bobo$98b2o10$99b2o$99b2o4$95b2o$94bobo$95bo144$214b2o$
214bobo$215bo!'''

rle_BL_sl = '''
25b2o$24bobo$25bo3$22b2o$21bo2bo$21bobo$22bo37$61bo$60bobo$61b2o3$52b
2o33b2o$51bo2bo32bobo$52bobo33bo$53bo4$67b2o$67bobo12b2o$68bobo10bo2bo
$69bo12bobo$83bo6$67bo$24bo41bobo$23bobo41bobo$24b2o42b2o$41b2o$40bobo
$29b2o9b2o9b2o$29b2o20bobo9b2o$52b2o9b2o10$o$3o$3bo$2b2o5$24bo$13b2o8b
obo$13bobo8bobo$14bobo8b2o$15bo2$3bo$3b3o$6bo29b2o$5b2o29bobo$37bo2$
132b2o$132bobo$24b2o107bo$24b2o$31b2o$8b2o20bo2bo$8bobo20bobo$9b2o21bo
$38b2o$38bobo$39bo6$11b2o$10bobo$10b2o10$9b2o$9b2o4$13b2o$13bobo$14bo!'''


rle_TL_sl = '''63bo$62bobo$63b2o14$89bo$88bobo$89b2o3$80b2o$79bo2bo$80bobo$81bo11$81b
o$70b2o8bobo$70bobo8bobo$71bobo8b2o$72bo2$65b2o$65b2o$93b2o$93bobo$94b
o6$88b2o$65b2o20bo2bo$65bobo20bobo$66b2o21bo9$68b2o$67bobo$26bo40b2o$
25bobo$26b2o10bo$37bobo$38b2o3$29b2o$28bo2bo$29bobo$30bo35b2o$66b2o3$
44b2o93b2o$32b2o10bobo23b2o66bobo$32b2o11bobo22bobo61bo4bo$46bo24bo61b
obo$132bo2bo$133b2o5$44bo$bo41bobo$obo41bobo$b2o42b2o$18b2o$17bobo$6b
2o9b2o9b2o$6b2o20bobo$29b2o2$38b2o$38bobo$40bo$40b2o10b2o$52bobo$54bo$
54b2o!
'''

cblocks = '''2o$2o47$29b2o$29b2o53$83b2o$83b2o!'''

glider = g.parse("3o$o$bo!")
boat = g.parse("bo$obo$2o!")

class Duplicator:
	def __init__(self, rle, glider_input, delay_boat):
		self.unit = g.parse(rle)
		gx, gy = glider_input
		self.glider = g.transform(glider, gx, gy)
		gx, gy = delay_boat
		self.dboat = g.transform(boat, gx, gy)
		
	def place(self, x, y, delay = 0, add_glider = False):
		g.putcells(self.unit, x, y)
		g.putcells(self.dboat, x + delay, y-delay)
		
		if add_glider:
			g.putcells(self.glider, x + delay, y-delay)

class Remini:

	def __init__(self, inshift):
	
		self.dup_br = Duplicator(rle_BR_sl, (99, 180), (76, 155))
		self.dup_tr = Duplicator(rle_TR_sl, (243, 303), (215, 273))
		self.dup_bl = Duplicator(rle_BL_sl, (163, 112), (140, 87))
		self.dup_tl = Duplicator(rle_TL_sl, (283,184), (78, -23))
		self.construction = g.parse(cblocks, 139, -204)
		self.shift = inshift
		
	def place_bottom(self, x, y, add_gliders):
		if add_gliders:
			self.dup_bl.place(x, y, 0, add_gliders)
			self.dup_br.place(x + 150, y - 76, 0, add_gliders)
			
		else: 
			self.dup_bl.place(x, y, 9 - self.shift / 2, add_gliders)
			self.dup_br.place(x + 150, y - 76, 5 - self.shift / 2, add_gliders)
			
	def place_top(self, x, y, add_gliders):
	
		if add_gliders:
		
			self.dup_tl.place(x + 58, y + 60, 0, add_gliders)
			self.dup_tr.place(x + 152, y - 109, 0, add_gliders)
			
		else: 
			self.dup_tl.place(x + 58, y + 60, 5, add_gliders)
			self.dup_tr.place(x + 152, y - 109, 10, add_gliders)
			
	def place_blocks(self, x, y):
		g.putcells(self.construction, x, y)
		
	def place(self, x, y, add_gliders = True):
		self.place_top(x-110,y-110, add_gliders)
		self.place_bottom(x,y, add_gliders)
		self.place_blocks(x, y)
		
	def place_unit(self, x, y, d, add_gliders = True):
		rem.place(x,y,add_gliders)
		rem.place(772 + x + d, 505 + self.shift + y + d,add_gliders)

g.new("")


shift = -16

#dup_tl = Duplicator(rle_TL_sl, (231,114), (92, -27))
#dup_tl.place(0,0,0,True)
rem = Remini(shift)


#g.putcells(glider, 400 -52, 400)
dx = 0#i * 100000

d = (568 - shift)
rem.place_unit(dx,0,30 * 300,True)
rem.place_unit(dx,-d,30 * 300,False)
rem.place_unit(dx,-2 * d,30 * 300,False)
rem.place_unit(dx,-3 * d,30 * 300,False)

arm = ArmP30()
arm.load_recipes()

arm.apply_slmake("O" + str(294 - 2 * shift))
arm.apply_slmake("O" + str(332 - shift))
arm.apply_slmake("O" + str(380 - 2 * shift))
arm.apply_slmake("O" + str(446 - shift))

arm.place(dx + 400 -52, 400)