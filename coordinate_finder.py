import pyautogui
from time import sleep
pyautogui.PAUSE = 1
sleep(5)

#this pyautogui.position() returns the x and y coordinates of the mouse
#one you start the execution of the file, you have 5 seconds to position the mouse on a point who's coordinates you need
#for example: if i place the mouse on top of the google chrome icon in my taskbar,I'll get the coordinates of the icon
x,y=pyautogui.position()
print(x,y)


#pyautogui.moveTo(x,y) is used to move the mouse from any position to the point x,y pyautogui.click() is used to simulate a 
#mouse click over here.
#w.r.t this example, the mouse will move on its own to the google chrome icon and open it
pyautogui.moveTo(x,y)
pyautogui.click()

#repeat this program to find the coordinates of all the places where you'll have to do a mouse click to open an application in the web


#1366*768 Resolution
#{
#Opening Meet 263 281
#Enter code box 979 410
#Meet code meet.google.com/yef-dzof-pjo
#Continue  859 512
#Mic Off 406 578
#Camera Off 507 604
#Join 972 425
#Open ChatBox 1120 92
#click on chat 1060 683

#Close meet 474 682

#TopLeft, Top Right, BottomLeft
#1005 185,1364 185,1006 657

#SmallestX , BiggestX, SmallestY, Biggest y
#1005, 1364, 185, 657
#Crop coordinates [185:657, 1005:1364]

#Typing answer 1282 154, 1092 685, 1340 693
#}
