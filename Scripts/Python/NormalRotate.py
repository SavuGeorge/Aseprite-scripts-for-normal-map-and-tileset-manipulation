import numpy as np
import PIL as pil
import math
from PIL import Image as img
import sys


def rotateVector2(v, angle):
    x = v[0] * 2 - 255
    y = v[1] * 2 - 255
    a = v[2]
    result = np.empty([3])
    if angle == 90:
        result[0] = -y 
        result[1] = x
    elif angle == 180:
        result[0] = -x
        result[1] = -y
    elif angle == 270:
        result[0] = y
        result[1] = -x
    else:
        sys.exit()

    result[0] = (result[0] + 255) / 2
    result[1] = (result[1] + 255) / 2
    result[2] = a
    return result
    

if len(sys.argv) == 2:
    runPath = sys.path[0] + '\\'
    inputPath = runPath + 'RotateInput\\'
    try:
        redCh = img.open(inputPath + sys.argv[1] + 'R.png')
        grnCh = img.open(inputPath + sys.argv[1] + 'G.png')
    except:
        print('Cant find textures ' + sys.argv[1] + 'R.png and ' + sys.argv[1] + 'G.png');
        sys.exit()    
        
    w,h = redCh.size
    if (redCh.size != grnCh.size) or (w != 2*h):
        print('Wrong sizes')
        sys.exit()
    
    
    redWarning = False
    greenWarning = False
    
    edgeTop = np.empty([h,h,3])
    cornerUpRight = np.empty([h,h,3])
    for x in range(0,math.floor(w/2)):
        for y in range(h):
        
            r1,g1,b1,a = redCh.getpixel((x,y))
            if not(r1==g1==b1):
                redWarning = True
                
            r2,g2,b2,a = grnCh.getpixel((x,y))
            if not(r2==g2==b2):
                greenWarning = True
            
            edgeTop[x,y,0] = r1
            edgeTop[x,y,1] = g2
            edgeTop[x,y,2] = a
            
            r1,g1,b1,a = redCh.getpixel((x+h,y))
            if not(r1==g1==b1):
                redWarning = True
                
            r2,g2,b2,a = grnCh.getpixel((x+h,y))
            if not(r2==g2==b2):
                greenWarning = True
            
            cornerUpRight[x,y,0] = r1
            cornerUpRight[x,y,1] = g2
            cornerUpRight[x,y,2] = a
            
    cornerDownRight = np.empty([h,h,3])
    cornerDownLeft = np.empty([h,h,3])
    cornerUpLeft = np.empty([h,h,3])
    edgeRight = np.empty([h,h,3])
    edgeBottom = np.empty([h,h,3])
    edgeLeft = np.empty([h,h,3])
    
    for x in range(h):
        for y in range(h):
            cornerDownRight[x,y,:] = rotateVector2(cornerUpRight[x,y,:], 270.0)
            cornerDownLeft[x,y,:] = rotateVector2(cornerUpRight[x,y,:], 180.0)
            cornerUpLeft[x,y,:] = rotateVector2(cornerUpRight[x,y,:], 90.0)
            
            edgeRight[x,y,:] = rotateVector2(edgeTop[x,y,:], 270.0)
            edgeBottom[x,y,:] = rotateVector2(edgeTop[x,y,:], 180.0)
            edgeLeft[x,y,:] = rotateVector2(edgeTop[x,y,:], 90.0)
    
    
    cornerDownRight = np.rot90(cornerDownRight, 1)
    cornerDownLeft = np.rot90(cornerDownLeft, 2)
    cornerUpLeft = np.rot90(cornerUpLeft, 3)
    
    edgeRight = np.rot90(edgeRight,1)
    edgeBottom = np.rot90(edgeBottom,2)
    edgeLeft = np.rot90(edgeLeft,3)
    
    donutR = img.new('RGBA', (3*h,3*h))
    donutG = img.new('RGBA', (3*h,3*h))

    if redWarning == True:
        print('Warning:Red map not fully in grayscale')
    if greenWarning == True:
        print('Warning:Green map not fully in grayscale')
    
    for x in range(h):
        for y in range(h):
            #corners
            donutR.putpixel( (x,y) , (math.floor(cornerUpLeft[x,y,0]), math.floor(cornerUpLeft[x,y,0]), math.floor(cornerUpLeft[x,y,0]), math.floor(cornerUpLeft[x,y,2])) )
            donutR.putpixel( (x+2*h,y) , (math.floor(cornerUpRight[x,y,0]), math.floor(cornerUpRight[x,y,0]), math.floor(cornerUpRight[x,y,0]), math.floor(cornerUpRight[x,y,2])) )
            donutR.putpixel( (x+2*h,y+2*h) , (math.floor(cornerDownRight[x,y,0]), math.floor(cornerDownRight[x,y,0]), math.floor(cornerDownRight[x,y,0]), math.floor(cornerDownRight[x,y,2])) )
            donutR.putpixel( (x,y+2*h) , (math.floor(cornerDownLeft[x,y,0]), math.floor(cornerDownLeft[x,y,0]), math.floor(cornerDownLeft[x,y,0]), math.floor(cornerDownLeft[x,y,2])) )
            
            donutG.putpixel( (x,y) , ( math.floor(cornerUpLeft[x,y,1]), math.floor(cornerUpLeft[x,y,1]), math.floor(cornerUpLeft[x,y,1]), math.floor(cornerUpLeft[x,y,2]) ) )
            donutG.putpixel( (x+2*h,y) , ( math.floor(cornerUpRight[x,y,1]), math.floor(cornerUpRight[x,y,1]), math.floor(cornerUpRight[x,y,1]), math.floor(cornerUpRight[x,y,2]) ) )
            donutG.putpixel( (x+2*h,y+2*h) , (math.floor(cornerDownRight[x,y,1]), math.floor(cornerDownRight[x,y,1]), math.floor(cornerDownRight[x,y,1]), math.floor(cornerDownRight[x,y,2]) ) )
            donutG.putpixel( (x,y+2*h) , (math.floor(cornerDownLeft[x,y,1]), math.floor(cornerDownLeft[x,y,1]), math.floor(cornerDownLeft[x,y,1]), math.floor(cornerDownLeft[x,y,2]) ) )
            
            #edges
            donutR.putpixel( (x+h,y), ( math.floor(edgeTop[x,y,0]), math.floor(edgeTop[x,y,0]), math.floor(edgeTop[x,y,0]), math.floor(edgeTop[x,y,2])) )
            donutR.putpixel( (x+2*h,y+h), ( math.floor(edgeRight[x,y,0]), math.floor(edgeRight[x,y,0]), math.floor(edgeRight[x,y,0]), math.floor(edgeRight[x,y,2])) )
            donutR.putpixel( (x+h,y+2*h), ( math.floor(edgeBottom[x,y,0]), math.floor(edgeBottom[x,y,0]), math.floor(edgeBottom[x,y,0]), math.floor(edgeBottom[x,y,2])) )
            donutR.putpixel( (x,y+h), ( math.floor(edgeLeft[x,y,0]), math.floor(edgeLeft[x,y,0]), math.floor(edgeLeft[x,y,0]), math.floor(edgeLeft[x,y,2])) )
            
            donutG.putpixel( (x+h,y), ( math.floor(edgeTop[x,y,1]), math.floor(edgeTop[x,y,1]), math.floor(edgeTop[x,y,1]), math.floor(edgeTop[x,y,2])) )
            donutG.putpixel( (x+2*h,y+h), ( math.floor(edgeRight[x,y,1]), math.floor(edgeRight[x,y,1]), math.floor(edgeRight[x,y,1]), math.floor(edgeRight[x,y,2])) )
            donutG.putpixel( (x+h,y+2*h), ( math.floor(edgeBottom[x,y,1]), math.floor(edgeBottom[x,y,1]), math.floor(edgeBottom[x,y,1]), math.floor(edgeBottom[x,y,2])) )
            donutG.putpixel( (x,y+h), ( math.floor(edgeLeft[x,y,1]), math.floor(edgeLeft[x,y,1]), math.floor(edgeLeft[x,y,1]), math.floor(edgeLeft[x,y,2])) )
            
            #center
            donutR.putpixel( (x+h,y+h) , (0,0,0,255) )
            donutG.putpixel( (x+h,y+h) , (0,0,0,255) )
    
    print("AAAAAAA")
    print(runPath)
    savePath = runPath + 'RotateOutput' + '\\'
    donutR.save(savePath + sys.argv[1] + 'R.png', "PNG")
    donutG.save(savePath + sys.argv[1] + 'G.png', "PNG")
    
else:
    print('Invalid argument count, you should pass in 1 texture name ')
    
    
    

   

