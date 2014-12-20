# Origina work and credits to Michal Nansi (details below)
# To use this script, you need to install hdapsd (sudo apt-get install hdapsd)


#!/usr/bin/python
#
# This program is under GPLv3 license --
#
# http://www.gnu.org/licenses/gpl-3.0.html
#
#
# 
# If you think, that this script is usefull, please send me a postcard to
#
# adress:
#
# Michal Nanasi
#
# Azalkova 1
#
# 82101 Bratislava
#
# Slovakia
#
import os,time,re,sys;


#Using with synclient.
#Left/right terminology swapped by Aapo Rantalainen
normal='xrandr  -o normal'
normalPen='xsetwacom set "Wacom ISDv4 E6 Pen stylus" rotate none'
normalFinger='xsetwacom set "Wacom ISDv4 E6 Finger touch" rotate none'
normalEraser='xsetwacom set "Wacom ISDv4 E6 Pen eraser" rotate none'


left='xrandr -o left'
leftPen='xsetwacom set "Wacom ISDv4 E6 Pen stylus" rotate ccw'
leftFinger='xsetwacom set "Wacom ISDv4 E6 Finger touch" rotate ccw'
leftEraser='xsetwacom set "Wacom ISDv4 E6 Pen eraser" rotate ccw'


right='xrandr -o right'
rightPen='xsetwacom set "Wacom ISDv4 E6 Pen stylus" rotate  cw'
rightFinger='xsetwacom set "Wacom ISDv4 E6 Finger touch" rotate cw'
rightEraser='xsetwacom set "Wacom ISDv4 E6 Pen eraser" rotate cw'

inverted='xrandr -o inverted'
invertedPen='xsetwacom set "Wacom ISDv4 E6 Pen stylus" rotate half'
invertedFinger='xsetwacom set "Wacom ISDv4 E6 Finger touch" rotate half'
invertedEraser='xsetwacom set "Wacom ISDv4 E6 Pen eraser" rotate half'

type=0

 
while True:
	time.sleep(0.1);
	try:
		f=open('/sys/devices/platform/hdaps/position','r')
		line=f.readline()
		m=re.search('.([0-9]*).*',line)
		trash=int(m.group(1))

		invertv = line.split(',')
		g= re.search('([0-9]*).*', invertv[1])
		invertv = int(g.group(1))
		
		#debug message (adjust values, if needed)
		#print ("trash: " + str(trash) + "  invertv: " +str(invertv))

		#rotate left
		if(trash < 400): 
			if type!=-1:
				os.system(left)
				os.system(leftPen)
				os.system(leftFinger)
				os.system(leftEraser)
				time.sleep(1);
				type=-1

		#rotate right 
		elif(trash > 590): 
			if type != 1:
				os.system(right)
				os.system(rightPen)
				os.system(rightEraser)
				os.system(rightFinger)
				time.sleep(1);
				type=1

		# #inverted mode
		elif(invertv > 570):
			if type!=2:
				os.system(inverted)
				os.system(invertedEraser)
				os.system(invertedFinger)
				os.system(invertedPen)
				time.sleep(1); 
				type=2

		#normal mode
		elif((trash > 480 and trash < 530)):
			if type!=0:
				os.system(normal)
				os.system(normalPen)
				os.system(normalFinger)
				os.system(normalEraser)
				time.sleep(1);
				type=0
	except:	
		type=47
