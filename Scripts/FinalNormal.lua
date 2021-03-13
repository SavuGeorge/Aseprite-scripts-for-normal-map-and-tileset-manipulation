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
layersB = {}
layersI = {}

hasIgnore = false

for i,layer in ipairs(sprite.layers) do

    local c1 = string.sub(layer.name,1,1)
    local c2 = string.sub(layer.name,2,2)
	local c3 = string.sub(layer.name,3,3)
	
	if(c3 == "") then
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
		if (c1 == "b") or (c1 == "B") then
			if ( c2 == "") then
				layersB[1] = layer
			else
				local nr = tonumber(c2)
				if ( nr >= 2) and ( nr <= 9 ) then
					layersB[nr] = layer
				end
			end
		end
		if (c1 == "i") or (c1 == "I") then
			hasIgnore = true
			if ( c2 == "") then
				layersI[1] = layer
			else
				local nr = tonumber(c2)
				if ( nr >= 2) and ( nr <= 9 ) then
					layersI[nr] = layer
				end
			end
		end
    end
	
end


local celsR = {}
local celsG = {}
local celsB = {}
local celsI = {}


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
        
        for j,layer in ipairs(layersB) do
            if (cel.layer == layer) then
                celsB[j] = cel
            end
        end
		
		if (hasIgnore == true) then
			for j,layer in ipairs(layersI) do
				if (cel.layer == layer) then
					celsI[j] = cel
				end
			end
		end
		
    end
end


w = app.activeSprite.width
h = app.activeSprite.height

for k,celR in ipairs(celsR) do

    local celG = celsG[k]
    local celB = celsB[k]
	local celI = celsI[k]
	

    if(celR.bounds.width ~= celG.bounds.width) then
        return app.alert("RG cel width mismatched")
    end

    if(celG.bounds.width ~= celB.bounds.width) then
        return app.alert("GB cel width mismatched")
    end
    
    if(celR.bounds.height ~= celG.bounds.height) then
        return app.alert("RG cel height mismatched")
    end

    if(celG.bounds.height ~= celB.bounds.height) then
        return app.alert("GB cel height mismatched")
    end

	path = script_path()

	imgR = Image(w,h)
	imgG = Image(w,h)
	imgB = Image(w,h)
	imgR:drawImage(celR.image, Point(celR.position.x, celR.position.y))
	imgG:drawImage(celG.image, Point(celG.position.x, celG.position.y))
	imgB:drawImage(celB.image, Point(celB.position.x, celB.position.y))
	imgR:saveAs(path .. "Python/MergeInput/AsepriteMergeR.png")
    imgG:saveAs(path .. "Python/MergeInput/AsepriteMergeG.png")
    imgB:saveAs(path .. "Python/MergeInput/AsepriteMergeB.png")    
	
	
	if (hasIgnore == false) then
		os.execute(path .. "Python/MergeNormals.bat " .. path .. "Python/MergeNormals.py AsepriteMerge")
    else
		imgI = Image(w,h)
		imgI:drawImage(celI.image, Point(celI.position.x, celI.position.y))
		imgI:saveAs(path .. "Python/MergeInput/AsepriteMergeI.png")
		os.execute(path .. "Python/MergeNormalsIgnore.bat " .. path .. "Python/MergeNormals.py AsepriteMerge AsepriteMergeI")
	end
	
	
    finalImg = Image{ fromFile = path .. "Python/MergeOutput/AsepriteMergeNormal.png" }
	
	
	finalSprite = Sprite(sprite.width,sprite.height)
	finalSprite.filename = "Normal"..tostring(k)..sprite.filename

	finalCel = finalSprite.cels[1]
	finalCel.image = finalImg

end


app.refresh()



