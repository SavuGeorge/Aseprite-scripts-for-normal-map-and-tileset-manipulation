import PIL as pil
from PIL import Image as img
import sys



if len(sys.argv) == 2:
    runPath = sys.path[0] + '\\'
    inputPath = runPath + 'SplitInput\\'
    try:
        normal = img.open(inputPath + sys.argv[1] + '.png')
    except:
        print('Cant find texture ' + sys.argv[1] + '.png');
        sys.exit()
    
    
    w,h = normal.size
    redOut = img.new('RGBA', (w,h) )
    grnOut = img.new('RGBA', (w,h) )
    bluOut = img.new('RGBA', (w,h) )
    
    for x in range(w):
        for y in range(h): 
            r,g,b,a = normal.getpixel((x,y))
            redOut.putpixel( (x,y) , (r,r,r,a) )
            grnOut.putpixel( (x,y) , (g,g,g,a) )
            bluOut.putpixel( (x,y) , (b,b,b,a) )
            
    savePath = runPath + 'SplitOutput' + '\\'
    
    print(savePath)
    redOut.save(savePath + sys.argv[1] + 'R.png', "PNG")
    grnOut.save(savePath + sys.argv[1] + 'G.png', "PNG")
    bluOut.save(savePath + sys.argv[1] + 'B.png', "PNG")
    
    
    
else:
    print('Invalid argument count, you should pass in 1 texture name ')