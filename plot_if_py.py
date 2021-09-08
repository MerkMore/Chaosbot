# plot_if_py.py
#
# interface to plot a picture, used in Merkbot.py
#
# author: MerkMore
# version 17 jul 2021
# python -m pip install Pillow
from PIL import Image, ImageDraw
from sc2.position import Point2

class plot_if:
    #
    grey = (125,125,125)
    colors = [(255,255,255),(0,125,0),(125,125,255),(125,0,0),(0,0,0),(255,255,0),(125,255,125)]
    #
    minx = 99999
    maxx = -99999
    miny = 99999
    maxy = -99999
    points = []
    strings = []
    #

    def plotstart():
        a=1

    def plot(point,stri):
        if stri not in plot_if.strings:
            plot_if.strings.append(stri)
        ix = plot_if.strings.index(stri)
        plot_if.minx = min(point.x,plot_if.minx)
        plot_if.maxx = max(point.x,plot_if.maxx)
        plot_if.miny = min(point.y,plot_if.miny)
        plot_if.maxy = max(point.y,plot_if.maxy)
        plot_if.points.append((point,ix,'c',0))

    def plotsquare(point,radius,stri):
        if stri not in plot_if.strings:
            plot_if.strings.append(stri)
        ix = plot_if.strings.index(stri)
        plot_if.minx = min(point.x-radius,plot_if.minx)
        plot_if.maxx = max(point.x+radius,plot_if.maxx)
        plot_if.miny = min(point.y-radius,plot_if.miny)
        plot_if.maxy = max(point.y+radius,plot_if.maxy)
        plot_if.points.append((point,ix,'s',radius))

    def plotstop():
        if len(plot_if.points) > 0:
            margin = 1 / 6
            broad = 1.5 * (plot_if.maxx - plot_if.minx)
            if broad == 0:
                broad = 1
            high = 1.5 * (plot_if.maxy - plot_if.miny)
            if high == 0:
                high == 1
            img = Image.new('RGB', (450, 450), plot_if.grey)
            # Draw uses a (right,down) notation
            minradius = 150 / len(plot_if.points)
            for (point,ix,shape,inradius) in plot_if.points:
                color = plot_if.colors[ix % 7]
                zeroonepoint = (margin + (point.x-plot_if.minx) / broad, 1 - (margin + (point.y-plot_if.miny) / high))
                drawpoint = (450 * zeroonepoint[0], 450 * zeroonepoint[1])
                radius = 450 * inradius / broad
                radius = max(radius,minradius)
                lurb = (drawpoint[0]-radius,drawpoint[1]-radius,drawpoint[0]+radius,drawpoint[1]+radius)
                if shape == 'c':
                    ImageDraw.Draw(img).ellipse(lurb,fill=color,outline=None)
                elif shape == 's':
                    ImageDraw.Draw(img).rectangle(lurb, fill=color, outline=None)
            img.save('data/plot.png')


            