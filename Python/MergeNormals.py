import numpy as np
import PIL as pil
import math
from PIL import Image as img
import sys

extra = False
if(len(sys.argv) == 3):
    extra = True
if len(sys.argv) == 2 or extra == True:
    runPath = sys.path[0] + '\\'
    inputPath = runPath + 'MergeInput\\'
    
    try:
        redCh = img.open(inputPath + sys.argv[1] + 'R.png')
        grnCh = img.open(inputPath + sys.argv[1] + 'G.png')
        bluCh = img.open(inputPath + sys.argv[1] + 'B.png')
        if extra == True:
            ignCh = img.open(inputPath + sys.argv[2] + '.png')
            
    except:
        print('Cant find textures ' + sys.argv[1] + 'R.png and ' + sys.argv[1] + 'G.png' + sys.argv[1] + 'B.png' + ' ' + sys.argv[2] + '.png');
        sys.exit()
        
    w,h = redCh.size
    if (redCh.size != grnCh.size) or (grnCh.size != bluCh.size):
        print('Mismatched sizes')
        sys.exit()
    if extra == True:
        if(bluCh.size != ignCh.size):
            print('Mismatched sizes')
            sys.exit()
        
        
    outputNormal = img.new('RGBA', (w,h) )
    
    redWarning = False
    greenWarning = False
    blueWarning = False
    
    for x in range(w):
        for y in range(h):
        
                r1,g1,b1,_ = redCh.getpixel((x,y))
                if not(r1==g1==b1):
                    redWarning = True
                    
                r2,g2,b2,_ = grnCh.getpixel((x,y))
                if not(r2==g2==b2):
                    greenWarning = True
                    
                r3,g3,b3,_ = bluCh.getpixel((x,y))
                if not(r3==g3==b3):
                    blueWarning = True
                    
                if extra == True:
                    a4,_,_,a = ignCh.getpixel((x,y))
                else:
                    a4 = 0
                
                outputNormal.putpixel( (x,y) , (r1,g2,b3,255 - a4) )
    
    
    savePath = runPath + 'MergeOutput' + '\\'
    outputNormal.save(savePath + sys.argv[1] + 'Normal.png', "PNG")
    
    if redWarning == True:
        print('Warning:Red map not fully in grayscale')
    if greenWarning == True:
        print('Warning:Green map not fully in grayscale')
    if blueWarning == True:
        print('Warning:Blue map not fully in grayscale')
        
    
else:
    print('Invalid argument count, you should pass in 1 or 2 texture names ')
    