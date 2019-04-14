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
		self.arm_ext = -42
		
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

cblocks_top = '''2o$2o57$19b2o$19b2o!'''
cblocks_bottom = '''2o$2o!'''

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

	def __init__(self, shift):
	
		self.dup_br = Duplicator(rle_BR_sl, (99, 180), (76, 155))
		self.dup_tr = Duplicator(rle_TR_sl, (243, 303), (215, 273))
		self.dup_bl = Duplicator(rle_BL_sl, (163, 112), (140, 87))
		self.dup_tl = Duplicator(rle_TL_sl, (283,184), (78, -23))
		self.top_blocks = g.parse(cblocks_top, 139 + 10, -204 - 10)
		self.bottom_blocks = g.parse(cblocks_top, 83 + 139, 102-204)
		self.shift = shift 
		
	def place_bottom(self, x, y, add_gliders):
		if add_gliders:
			self.dup_bl.place(x, y, 0, add_gliders)
			self.dup_br.place(x + 150, y - 76, 0, add_gliders)
			
		else: 
			self.dup_bl.place(x, y, 9, add_gliders)
			self.dup_br.place(x + 150, y - 76, 5, add_gliders)
			
	def place_top(self, x, y, add_gliders):
	
		if add_gliders:
		
			self.dup_tl.place(x + 58, y + 60, 0, add_gliders)
			self.dup_tr.place(x + 152, y - 109, 0, add_gliders)
			
		else: 
			self.dup_tl.place(x + 58, y + 60, 5 - self.shift/2, add_gliders)
			self.dup_tr.place(x + 152, y - 109, 10 - self.shift/2, add_gliders)
			
	def place_blocks(self, x, y):
		g.putcells(self.bottom_blocks, x, y)
		g.putcells(self.top_blocks, x - self.shift, y - self.shift)
		
	def place(self, x, y, add_gliders = True):
		self.place_top(x-110 - self.shift,y-110 - self.shift, add_gliders)
		self.place_bottom(x,y, add_gliders)
		self.place_blocks(x, y)
		
	def place_unit(self, x, y, d, add_gliders = True):
		rem.place(x,y,add_gliders)
		rem.place(772 + x + d + self.shift,505 + y + d + self.shift,add_gliders)

g.new("")

#dup_tl = Duplicator(rle_TL_sl, (231,114), (92, -27))
#dup_tl.place(0,0,0,True)

#for shift in range(0, 60, 2):
shift = 14 

dx = 0#shift * 10000
rem = Remini(shift)
d = 1200000 / 30 

rem.place_unit(dx,0,30 * d,True)
#rem.place_unit(dx,-568,30 * d,False)
#rem.place_unit(dx,-2 * 568,30 * d,False)
#rem.place_unit(dx,-3 * 568,30 * d,False)
#rem.place_unit(dx,-4 * 568,30 * d,False)
#rem.place_unit(dx,-5 * 568,30 * d,False)
#rem.place_unit(dx,-6 * 568,30 * d,False)

arm = ArmP30()
arm.load_recipes()
Gemini_recipe = '''E-7 E-14 E-6 O4 O10 E6 O18 E35 E37 E39 E38 E41 E49 E52 E56 O65 O82 O80 E97 E90 E94 O103 O120 O118 E135 E128 E132 O141 O158 O156 E173 E166 E170 O179 O196 O194 E211 E213 E215 E217 E216 E219 E227 E230 E234 O243 O260 O258 E275 E268 E272 O281 O298 O296 E313 E306 E310 O319 O336 O334 E351 E353 E355 E357 E356 E359 E367 E379 E381 E383 E382 E385 E393 E405 E407 E409 E408 E411 E419 E431 E433 E435 E434 E437 E445 E457 E459 E461 E460 E463 E471 E483 E485 E487 E486 E489 E497 E509 E511 E513 E512 E515 E523 E535 E537 E539 E538 E541 E549 E561 E565 E579 E545 E534 E529 E537 E529 E536 E535 E538 E531 E532 E529 E521 E509 E512 E505 E506 E503 E495 E483 E486 E479 E480 E477 E469 O468 O468 E465 O463 E450 E450 E457 O470 O463 O460 E450 O455 O455 E457 O444 E474 E467 E473 E475 E442 O455 O453 O461 O454 O438 E438 E439 E456 O463 E468 E461 E464 E466 E465 E468 E476 E479 E470 E470 E477 O442 E449 O457 O465 E451 E442 E460 E464 O473 O490 O488 E505 E498 E502 O512 E516 E496 O493 E507 E535 E524 E552 E549 E539 E534 E549 O554 O562 O554 E573 E576 O578 O588 O587 E588 E576 E576 O576 E570 E572 E572 E567 E562 O531 E529 E529 E535 E533 E528 E528 E519 E528 E522 E523 O518 O521 E536 O529 O519 E516 O524 E525 E505 E495 O497 O494 E485 E477 O460 O457 E448 E440 E457 E494 O490 O494 O485 E477 O470 O462 E452 E452 O445 O442 E446 O470 O473 E443 O457 O460 O463 E450 E454 E470 E480 E483 E480 E467 E466 O468 O465 O465 E462 O414 O411 E402 E411 E415 E418 E411 E412 E409 E394 E401 E375 E375 E389 E387 O384 O366 O363 E354 E346 E363 E401 O401 O408 O407 O421 O419 E412 E438 O444 E446 O450 E451 O460 E458 E456 E464 O468 E472 O477 O497 E498 O481 O482 E459 O453 O453 E453 O457 E442 E439 O451 E458 E467 E460 O467 E463 E450 E469 E463 E460 O469 O472 O472 E465 E488 E481 O456 E460 E459 E449 E448 E457 E460 E469 E472 E499 O492 O489 O491 O485 E483 E482 E484 O460 O445 E455 E443 E450 E441 E434 E448 E455 E436 E443 O448 O445 O452 E454 E441 O435 O417 O448 E468 E463 E471 E474 E462 O464 E477 E474 E470 E477 E457 E468 E451 E447 E447 O442 E433 E448 E446 O456 O458 O451 O448 O445 O456 E446 E454 E463 O463 O464 E463 E461 O449 O464 O457 E461 O464 O432 O435 O427 E433 E439 O427 E417 E410 E416 E418 E385 O398 E366 E376 E371 E366 O374 O372 O342 O339 E330 E313 E315 E327 E338 O405 O405 O399 E390 O394 O398 E429 E445 O456 O449 O457 E466 O465 O465 E462 E454 E446 E463 E459 E457 O440 O450 O458 E452 O481 E468 E478 E471 O473 E477 E461 O456 O457 E448 E456 E442 E442 E438 E418 O423 E423 E420 O435 E421 E428 E431 E407 E408 O414 O417 E420 O422 E404 O413 E416 E404 E371 E380 E380 E373 O403 E394 E385 O393 E388 E379 O409 O416 O402 O418 O422 E413 E412 E399 O410 O406 O408 E404 E403 O393 O387 E393 E380 E393 O401 E397 E401 E398 E378 O370 O373 E373 O367 O366 E370 O378 E378 E389 E393 O403 E424 E424 E438 O494 O495 O485 O479 E478 O507 O497 E500 E487 E486 E484 O485 O490 E486 E487 E490 E481 E481 E501 E492 E496 E494 E496 E502 E498 O490 O492 O498 O494 O502 O504 O494 O501 O516 O514 O512 O512 O521 O514 E498 E495 E495 O497 E510 E509 O512 O477 O477 O475 E470 E473 E476 O481 E486 E477 O482 O490 O478 E469 E481 E487 E487 E489 E486 E491 E486 E483 E488 E494 E499 E489 E498 E507 E507 E510 O506 E492 E495 O500 O568 O567 O567 E572 E565 O563 E576 O576 O584 O567 O579 E573 E528 E525 E533 E529 O535 O519 O509 O515 E510 E501 E488 E491 E483 E489 O485 E485 E489 O499 E498 O470 O478 E487 O489 O477 O489 E477 E478 E470 E467 E471 E470 E478 O483 O489 O475 O478 E484 E490 E463 O473 E471 E476 O501 E494 E494 E498 O505 E494 E493 O486 O487 E486 E484 E489 O478 O472 O480 O472 O476 E478 E465 O495 E481 O471 O502 O502 O502 O512 O503 O506 O504 O493 E496 O486 O494 O482 E484 E481 O478 O476 E489 E466 E469 E469 O474 E469 O465 E473 E469 O546 O538 O538 O538 O524 O520 O545 O536 E523 E525 O518 O515 O517 E521 O541 E544 E509 E499 E503 O409 E392 E396 E400 O353 O357 O366 E354 E357 E361 O367 O363 O358 E360 E328 E299 E304 E315 E305 O283 O280 E271 E280 E263 E253 E245 E242 E248 E250 E238 E246 E261 E289 O291 O281 O286 O291 E274 E269 E269 E292 E295 E288 E289 E286 O317 O324 O316 E309 O309 O303 E305 O304 E297 E305 O307 O297 O306 E290 O306 O307 E299 E278 O234 O234 E224 O220 E221 O224 E230 E212 E242 E251 E252 O244 O254 O264 O252 O231 E222 E225 E227 E222 O228 O225 O229 O221 E245 E241 O247 O236 E231 E222 E235 E234 O242 O246 E248 E226 E229 E258 E237 O233 O237 O227 O223 O245 O237 O243 O239 O250 E243 E244 E242 O247 O255 O243 E248 O261 E236 E237 O233 O228 O223 E226 E236 O242 O241 E236 E229 E226 O223 E236 E239 E239 E236 O234 O231 O221 O197 O185 O182 E173 E165 E182 O194 E185 E194 E177 O148 O152 E152 O154 O148 E145 E119 E129 E122 E107 O118 O129 E115 O160 O157 E148 E140 E157 E159 E158 O151 O176 E177 E184 E183 O185 O189 O146 E141 E130 E129 E125 E123 E139 E131 E125 E122 E131 E135 O145 O148 O140 O133 E142 O152 O131 E135 E133 E146 O148 O140 O143 O136 O152 E149 E149 E146 E155 E151 E142 E155 E137 E128 O144 E137 E132 O140 O132 O135 O137 O132 O136 O127 O124 E112 O132 O131 E121 E138 E141 E131 E140 E139 E143 E143 O144 O128 O129 E128 E126 E131 O120 O122 E123 E113 O115 O115 O115 E120 E113 O110 E124 O124 O125 O110 E109 O120 O114 O109 O107 O155 O159 E172 E179 E188 O189 E172 E175 O168 E156 O180 O176 E172 E173 E171 O183 E178 E180 E173 E190 E191 E185 O177 E179 E179 O190 O189 E189 E181 E192 O191 O183 O181 O192 E190 O182 O177 E168 E172 E172 E182 O177 O185 O179 E175 O179 E182 E178 E182 E170 E168 O181 E178 E168 E202 O202 O206 O209 O193 E197 O200 O189 E206 E195 O195 E191 E184 E201 E202 E196 O188 E190 E190 O222 O223 E226 E208 O216 O220 O222 E195 E188 E200 E203 O190 E185 E194 E199 O194 O185 E193 E193 E185 E197 O196 E198 E190 E201 O207 O194 E212 E205 E202 E210 O200 E205 E207 O215 E205 E172 E171 O171 E159 E173 O183 E180 E178 E184 O177 O177 E181 O178 O181 O176 E175 E181 O174 O193 O194 O194 O180 O180 O181 O174 E182 E185 O187 O184 O184 E182 E190 O180 O182 O190 E252 E285 O288 O289 O289 E294 E280 E314 E309 E299 E301 O303 E314 O311 O294 O306 E300 E315 E306 E313 E302 E311 E327 O313 O324 E319 E320 E322 E314 E328 E328 E332 O251 O252 E254 E246 O255 E249 O248 E246 E249 O266 O277 O274 O286 O271 E273 E268 O265 O257 O261 O270 E291 E298 E278 E274 E258 E265 O272 O265 O268 O275 O265 O267 O266 E270 O274 E276 E267 O274 O276 E272 E265 E263 E266 E261 O260 E260 O277 O262 E268 E268 E271 E271 O260 E278 E277 O280 O279 O282 O279 E282 E286 E286 E281 O283 O285 O273 E267 O267 O271 O280 E268 O281 O278 O271 O281 O281 E276 O272 E274 E273 E271 E281 E277 O269 O274 O282 O273 O274 E281 O281 O285 O229 O236 O224 E229 O229 E225 O236 E223 E214 E221 E215 E216 E212 E214 E215 E220 O229 O225 E221 O225 E223 E228 E225 E215 E223 E218 E214 E205 E227 E221 O216 E207 E233 E227 O234'''.replace("\n","").split(" ")

for r in Gemini_recipe:
	arm.apply_slmake(r)
	
arm.apply_slmake("O274")
arm.apply_slmake("O" + str(312-shift))
arm.apply_slmake("O360")
arm.apply_slmake("O" + str(426-shift))

arm.place(dx + 400 -52, 400)