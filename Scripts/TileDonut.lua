function script_path()
   local str = debug.getinfo(2, "S").source:sub(2)
   return str:match("(.*[/\\])")
end


if app.apiVersion < 1 then
  return app.alert("This script requires Aseprite v1.2.10-beta3")
end

local cel = app.activeCel
if not cel then
  return app.alert("There is no active image")
end

local celimg = cel.image
local bounds = cel.bounds

local l = cel.sprite.width / 3 -- Tile size

mainPiece = Image(2*l,l)
centerPiece = Image(l,l)


for i = 0, bounds.width-1, 1 do
    for j = 0, bounds.height-1, 1 do
        X = i + bounds.x - l
        Y = j + bounds.y
        if (i+bounds.x >= l) and (i+bounds.x <= 3*l) and (j+bounds.y <= l) then
            mainPiece:drawPixel(X,Y, celimg:getPixel(i,j) )
        end
		if (i+bounds.x >=l) and (i+bounds.x <= 2*l) and (j+bounds.y >= l) and (j+bounds.y <= 2*l) then
			centerPiece:drawPixel(X,Y-l, celimg:getPixel(i,j) )
		end 
    end
end

path = script_path()

mainPiece:saveAs(path .. "Python/TileDonutInput/DonutTileset.png")

os.execute(path .. "Python/TileDonut.bat " .. path .. "Python/TileDonut.py DonutTileset")

local donut = Image{ fromFile = path .. "Python/TileDonutOutput/DonutTileset.png" }

donut:drawImage(centerPiece, Point(l,l))
cel.image = donut
cel.position = Point(0,0)



app.refresh()






