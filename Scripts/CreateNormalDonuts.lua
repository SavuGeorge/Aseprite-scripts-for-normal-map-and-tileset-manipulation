function script_path()
   local str = debug.getinfo(2, "S").source:sub(2)
   return str:match("(.*[/\\])")
end


if app.apiVersion < 1 then
  return app.alert("This script requires Aseprite v1.2.10-beta3")
end

local sprite = app.activeSprite
local frame = app.activeFrame



layersR = {}
layersG = {}

for i,layer in ipairs(sprite.layers) do

    local c1 = string.sub(layer.name,1,1)
    local c2 = string.sub(layer.name,2,2)
    if ( c1 == "r") or ( c1 == "R") then
        if ( c2 == "") then
            layersR[1] = layer
        else
            local nr = tonumber(c2)
            if ( nr >= 2) and ( nr <= 9 ) then
                layersR[nr] = layer
            end
        end
    end
    if (c1 == "g") or (c1 == "G") then
        if ( c2 == "") then
            layersG[1] = layer
        else
            local nr = tonumber(c2)
            if ( nr >= 2) and ( nr <= 9 ) then
                layersG[nr] = layer
            end
        end
    end
    
end

local celsR = {}
local celsG = {}

for i,cel in ipairs(sprite.cels) do
    if (cel.frame == frame) then 
        for j,layer in ipairs(layersR) do
            if (cel.layer == layer) then
                celsR[j] = cel
            end
        end
        
        for j,layer in ipairs(layersG) do
            if (cel.layer == layer) then
                celsG[j] = cel
            end
        end
    end
end


local l = sprite.width / 3 -- Tile size

local mainPieceR = Image(2*l,l)
local mainPieceG = Image(2*l,l)

local centerPieceR = Image(l,l)
local centerPieceG = Image(l,l)

for k,celR in ipairs(celsR) do

    local celG = celsG[k]
    
    local celimgR = celR.image
    local boundsR = celR.bounds
    
    local celimgG = celG.image
    local boundsG = celG.bounds

    for i = 0, boundsR.width-1, 1 do
        for j = 0, boundsR.height-1, 1 do
            X = i + boundsR.x - l
            Y = j + boundsR.y
            if (i+boundsR.x >= l) and (i+boundsR.x <= 3*l) and (j+boundsR.y <= l) then
                mainPieceR:drawPixel(X,Y, celimgR:getPixel(i,j) )
            end
			if (i+boundsR.x >=l) and (i+boundsR.x <= 2*l) and (j+boundsR.y >= l) and (j+boundsR.y <= 2*l) then
				centerPieceR:drawPixel(X,Y-l, celimgR:getPixel(i,j) )
			end 
        end
    end
    
    for i = 0, boundsG.width-1, 1 do
        for j = 0, boundsG.height-1, 1 do
            X = i + boundsG.x - l
            Y = j + boundsG.y
            if (i+boundsG.x >= l) and (i+boundsG.x <= 3*l) and (j+boundsG.y <= l) then
                mainPieceG:drawPixel(X,Y, celimgG:getPixel(i,j) )
            end
			if (i+boundsG.x >=l) and (i+boundsG.x <= 2*l) and (j+boundsG.y >= l) and (j+boundsG.y <= 2*l) then
				centerPieceG:drawPixel(X,Y-l, celimgG:getPixel(i,j) )
			end 
        end
    end
    
	
	path = script_path()
	
    mainPieceR:saveAs(path .. "Python/RotateInput/AsepriteNormalDonutR.png")
    mainPieceG:saveAs(path .. "Python/RotateInput/AsepriteNormalDonutG.png")
    
    os.execute(path .. "Python/NormalRotate.bat " .. path .. "Python/NormalRotate.py AsepriteNormalDonut")
    
    local donutR = Image{ fromFile = path .. "Python/RotateOutput/AsepriteNormalDonutR.png" }
    local donutG = Image{ fromFile = path .. "Python/RotateOutput/AsepriteNormalDonutG.png" }
    
	donutR:drawImage(centerPieceR, Point(l,l))
    celR.image = donutR
    celR.position = Point(0,0)
    
	donutG:drawImage(centerPieceG, Point(l,l))
    celG.image = donutG
    celG.position = Point(0,0)
	
	
    
end



app.refresh()






