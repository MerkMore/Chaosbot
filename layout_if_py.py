# layout_if_py.py
#
# interface for the layout structure, used and defined in Merkbot.py, used in placer.py
#
# author: MerkMore
# version 8 july 2020
# python -m pip install Pillow
from PIL import Image, ImageDraw

class layout_if:
    layout = []
    mapname = ''
    startx = 0
    starty = 0
    enemyx = 0
    enemyy = 0
    
    #   
    grey = (125,125,125)
    white = (255,255,255)
    green = (0,125,0)
    lightblue = (125,125,255)
    red = (125,0,0)
    black = (0,0,0)
    yellow = (255,255,0)
    #   
     
    
    def save_layout():
        text = open('layout.txt','w')
        text.write('========================================='+'\n')
        text.write(layout_if.mapname+'\n')
        text.write(str(layout_if.startx)+'\n')
        text.write(str(layout_if.starty)+'\n')
        text.write(str(layout_if.enemyx)+'\n')
        text.write(str(layout_if.enemyy)+'\n')
        for col in range(0,200):
            stri = ''
            for row in range(0,100):
                stri = stri+str(layout_if.layout[col][row])
            text.write(stri+'\n')
            stri = ''
            for row in range(100,200):
                stri = stri+str(layout_if.layout[col][row])
            text.write(stri+'\n')
        text.write('========================================='+'\n')
        text.close()
    
    
    def load_layout():
        layout_if.layout = []
        text = open('layout.txt','r')
        stri=text.readline().rstrip()
        if stri[0] != '=':
            print('layout.txt has a wrong shape')
        layout_if.mapname = text.readline().rstrip()
        layout_if.startx = float(text.readline().rstrip())        
        layout_if.starty = float(text.readline().rstrip())        
        layout_if.enemyx = float(text.readline().rstrip())
        layout_if.enemyy = float(text.readline().rstrip())
        for col in range(0,200):
            collist = []
            stri=text.readline().rstrip()        
            for row in range(0,100):
                collist.append(float(stri[row]))
            stri=text.readline().rstrip()        
            for row in range(0,100):
                collist.append(float(stri[row]))
            layout_if.layout.append(collist)
        stri=text.readline().rstrip()        
        if stri[0] != '=':
            print('layout.txt has a wrong shape')
        text.close()
    
    
    def photo_layout():
        img = Image.new('RGB', (450, 450),layout_if.grey)
        for col in range(0,200):
    #       Draw uses a (right,down) notation
            for row in range(0,200):
                swaprow = 200-row
                info = layout_if.layout[col][row]
                if info == 0:
    #               buildable
                    rgb = layout_if.white
                elif info == 1:
                    rgb = layout_if.green
                elif info == 2:
    #               walkable
                    rgb = layout_if.lightblue
                elif info == 3:
                    rgb = layout_if.red
                elif info == 4:
    #               own building, realised or planned
                    rgb = layout_if.black
                else:
                    rgb = layout_if.yellow
                ImageDraw.Draw(img).rectangle([25+col*2,25+swaprow*2,27+col*2,27+swaprow*2],fill=rgb,outline=None)
        img.save('layout.png')


            