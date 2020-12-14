# layout_if_py.py
#
# interface for the layout structure, used and defined in Merkbot.py, used in placer.py
#
# author: MerkMore
# version 6 dec 2020
# python -m pip install Pillow
from PIL import Image, ImageDraw

class layout_if:
    layout = []
    height = []
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
    lightgreen = (125,255,125)
    #   

    linenr = 0
    goodlines = []
    
    def save_layout():
        mapplace = 'map: '+layout_if.mapname+' '+str(layout_if.startx)+' '+str(layout_if.starty)
        old = False
        with open('data/layout.txt','r') as open_file:
            for linen in open_file:
                line = linen.rstrip('\n')
                if line == mapplace:
                    old = True
        if not old:
            text = open('data/layout.txt','a')
            text.write('========================================='+'\n')
            text.write(mapplace+'\n')
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
            text.write('++++++++++++++++++++++++++++++++++++++++++'+'\n')
            for col in range(0,200):
                stri = ''
                for part in [0,50,100,150]:
                    for row in range(part,part+50):
                        stri = stri+str(layout_if.height[col][row])+' '
                    text.write(stri+'\n')
            text.write('========================================='+'\n')
            text.close()
    
    def get_line():
        line = layout_if.goodlines[layout_if.linenr]
        layout_if.linenr += 1
        return line
    
    def load_layout(mapplace):
        layout_if.layout = []
        layout_if.goodlines = []
        good = False
        with open('data/layout.txt','r') as open_file:
            for linen in open_file:
                line = linen.rstrip('\n')
                if line == mapplace:
                    good = True
                elif line[0] == '=':
                    good = False
                if good:
                    layout_if.goodlines.append(line)
        if len(layout_if.goodlines) == 0:
            print('data/layout.txt does not contain '+mapplace)
        layout_if.linenr = 0
        dummy = layout_if.get_line()
        layout_if.mapname = layout_if.get_line()
        layout_if.startx = float(layout_if.get_line())        
        layout_if.starty = float(layout_if.get_line())        
        layout_if.enemyx = float(layout_if.get_line())
        layout_if.enemyy = float(layout_if.get_line())
        for col in range(0,200):
            collist = []
            stri=layout_if.get_line()        
            for row in range(0,100):
                collist.append(float(stri[row]))
            stri=layout_if.get_line()        
            for row in range(0,100):
                collist.append(float(stri[row]))
            layout_if.layout.append(collist)
        layout_if.height = []
        dummy = layout_if.get_line()
        for col in range(0,200):
            collist = []
            for part in [0,50,100,150]:
                stri=layout_if.get_line()
                stri = stri.split()
                for row in range(part,part+50):
                    collist.append(float(stri[row]))
            layout_if.height.append(collist)

    
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
        img.save('data/layout.png')


    def photo_height():
        img = Image.new('RGB', (450, 450),layout_if.grey)
        for col in range(0,399): # min 0 max 398
            #       Draw uses a (right,down) notation
            for row in range(0,399): # min 0 max 398
                swaprow = 398-row # min 0 max 398
                # info = (layout_if.height[(col+1) // 2][(row+1) // 2] + layout_if.layout[col // 2][row // 2]) % 7
                info = layout_if.height[(col + 1) // 2][(row + 1) // 2] % 7
                if info == 0:
                    rgb = layout_if.white
                elif info == 1:
                    rgb = layout_if.green
                elif info == 2:
                    rgb = layout_if.lightblue
                elif info == 3:
                    rgb = layout_if.red
                elif info == 4:
                    rgb = layout_if.black
                elif info == 5:
                    rgb = layout_if.lightgreen
                else:
                    rgb = layout_if.yellow
                ImageDraw.Draw(img).rectangle([25+col,25+swaprow,27+col,27+swaprow],fill=rgb,outline=None)
        img.save('data/height.png')


            