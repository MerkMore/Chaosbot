# layout_if.py
#
# interface for the layout structure, used and defined in Merkbot.py, used in placer.py
#
# author: MerkMore
# version 3 july 2020
# python -m pip install Pillow
from PIL import Image, ImageDraw


layout = []
mapname = ''
startx = 0
starty = 0


img = None
#   
grey = (125,125,125)
white = (255,255,255)
green = (0,125,0)
blue = (0,0,125)
red = (125,0,0)
black = (0,0,0)
yellow = (255,255,0)
#   
 

def save_layout():
    text = open('layout.txt','w')
    d=text.write('========================================='+'\n')
    d=text.write(mapname+'\n')
    d=text.write(str(startx)+'\n')
    d=text.write(str(starty)+'\n')
    for col in range(0,200):
        stri = ''
        for row in range(0,100):
            stri = stri+str(layout[col][row])
        d=text.write(stri+'\n')
        stri = ''
        for row in range(100,200):
            stri = stri+str(layout[col][row])
        d=text.write(stri+'\n')
    d=text.write('========================================='+'\n')
    text.close()


def load_layout():
    layout = []
    text = open('layout.txt','r')
    stri=text.readline().rstrip()
    if stri[0] != '=':
        print('layout.txt has a wrong shape')
    mapname = text.readline().rstrip()
    startx = float(text.readline().rstrip())        
    starty = float(text.readline().rstrip())        
    for col in range(0,200):
        collist = []
        stri=text.readline().rstrip()        
        for row in range(0,100):
            collist.append(float(stri[row]))
        stri=text.readline().rstrip()        
        for row in range(0,100):
            collist.append(float(stri[row]))
        layout.append(collist)
    stri=text.readline().rstrip()        
    if stri[0] != '=':
        print('layout.txt has a wrong shape')
    text.close()


def photo_layout():
    img = Image.new('RGB', (450, 450),grey)
    for col in range(0,200):
#       Draw uses a (right,down) notation
        for row in range(0,200):
            swaprow = 200-row
            info = layout[col][row]
            if info == 0:
#               buildable
                rgb = white
            elif info == 1:
                rgb = green
            elif info == 2:
                rgb = blue
            elif info == 3:
                rgb = red
            elif info == 4:
#               own building, realised or planned
                rgb = black
            else:
                rgb = yellow
            ImageDraw.Draw(img).rectangle([25+col*2,25+swaprow*2,27+col*2,27+swaprow*2],fill=rgb,outline=None)
    img.save('layout.png')


            