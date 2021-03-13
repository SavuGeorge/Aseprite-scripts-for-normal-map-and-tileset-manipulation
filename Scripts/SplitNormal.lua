function script_path()
   local str = debug.getinfo(2, "S").source:sub(2)
   return str:match("(.*[/\\])")
end


if app.apiVersion < 1 then
  return app.alert("This script requires Aseprite v1.2.10-beta3")
end

local sprite = app.activeSprite
local cel = app.activeCel
if not cel then
  return app.alert("There is no active image")
end

path = script_path()

cel.image:saveAs(path .. "Python/SplitInput/AsepriteSplitNormal.png")

os.execute(path .. "Python/SplitNormal.bat " .. path .. "Python/SplitNormalMap.py AsepriteSplitNormal")
    
finalR = Image{ fromFile= path .. "Python/SplitOutput/AsepriteSplitNormalR.png" }
finalG = Image{ fromFile= path .. "Python/SplitOutput/AsepriteSplitNormalG.png" }
finalB = Image{ fromFile= path .. "Python/SplitOutput/AsepriteSplitNormalB.png" }

finalSpriteR = Sprite(sprite.width,sprite.height)
finalSpriteR.filename = sprite.filename.."Red"
finalCelR = finalSpriteR.cels[1]
finalCelR.image = finalR

finalSpriteG = Sprite(sprite.width,sprite.height)
finalSpriteG.filename = sprite.filename.."Red"
finalCelG = finalSpriteG.cels[1]
finalCelG.image = finalG

finalSpriteB = Sprite(sprite.width,sprite.height)
finalSpriteB.filename = sprite.filename.."Red"
finalCelB = finalSpriteB.cels[1]
finalCelB.image = finalB

app.refresh()






