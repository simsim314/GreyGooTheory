local g = golly()

function string:split(delimiter)
  local result = { }
  local from  = 1
  local delim_from, delim_to = string.find( self, delimiter, from  )
  while delim_from do
    table.insert( result, string.sub( self, from , delim_from-1 ) )
    from  = delim_to + 1
    delim_from, delim_to = string.find( self, delimiter, from  )
  end
  table.insert( result, string.sub( self, from  ) )
  return result
end


glds = {}

glds[0] = g.parse("3o$o$bo!")
glds[1] = g.evolve(g.parse("3o$o$bo!"), 2)
--blck = g.parse("6bo$5bobo$5bobo$6bo2$b2o7b2o$o2bo5bo2bo$b2o7b2o2$6bo$5bobo$5bobo$6bo!", -7, -8)
blck = g.parse("2o$2o!", -4, 0)

function place_glider(i, dx)
	if i%2 == 0 then
		g.putcells(glds[0], 15 * math.floor(i/2) + dx, 15 * math.floor(i/2))
	else
		g.putcells(glds[1], 8 + 15 * math.floor(i/2) + dx, 8 + 15 * math.floor(i/2))
	end 
end 
g.new("")
file = 'C:\\Users\\SimSim314\\Documents\\GitHub\\Glue\\Glue++\\P30_results_105.txt'
lines = {}

dx = 0
for line in io.lines(file) do 
	res = line:split(',')
	g.putcells(blck, dx)
	
	for i = 1, #res do 
		if res[i] == '1' then
			place_glider(i, dx)
		end
	end 
	
	place_glider(#res + 1, dx)
	
	dx = dx + 100
end