import PIL as pil
import math
from PIL import Image as img
import sys

    

if len(sys.argv) == 2:
    runPath = sys.path[0] + '\\'
    inputPath = runPath + 'TileDonutInput\\'
    print("SAAAAAAAAAAAAAAAAAAAAAAAA")
    try:
        baseTiles = img.open(inputPath + sys.argv[1] + '.png')
    except:
        print('Cant find texture ' + sys.argv[1]);
        sys.exit()    
        
    w,h = baseTiles.size
    
    leftTiles = baseTiles.rotate(90, expand = True)
    botTiles = baseTiles.rotate(180)
    rightTiles = baseTiles.rotate(270, expand = True)
    
    
    finalOutput = img.new('RGBA', (3*h,3*h) )
    
    box = ( 0, 0, h, 2*h )
    finalOutput.paste(leftTiles, box)
    
    box = ( 0, 2*h, 2*h, 3*h )
    finalOutput.paste(botTiles, box)
    
    box = ( 2*h, h, 3*h, 3*h)
    finalOutput.paste(rightTiles, box)
    
    box = (h, 0, 3*h, h)
    finalOutput.paste(baseTiles, box)
    
    
    savePath = runPath + 'TileDonutOutput' + '\\'
    finalOutput.save(savePath + sys.argv[1] + '.png', "PNG")
    
else:
    print('Invalid argument count, you should pass in 1 texture name ')
    
    
    

   

