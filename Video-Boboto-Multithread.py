#Do NOT delete. Really important stuffs =)
from vidgear.gears import ScreenGear
from tkinter import *
from PIL import Image

import threading
import PIL.ImageTk as ITk
import numpy as np
import cv2, pyautogui

# X 1270 - Y 190  Size 50 - Padd 70

procc_0 = None
procc_1 = None
procc_2 = None

sec_0 = None

# Variables
options = {}
stream = []
loop = False
terminated = False

raw = []

raw_size = 50
raw_pad = 70
coord_x = 1250
coord_y = 200

left = False
left_pass = None
down = False
down_pass = None
up = False
up_pass = None
right = False
right_pass = None

# Init RGB(?)
# Variables for masking
# RGB(?) 🟣
purp_Bot = np.array([135, 35, 160, 255])
purp_Top = np.array([190, 120, 200, 255])

# RGB(?) 🔵
cian_Bot = np.array([190, 120, 0, 255])
cian_Top = np.array([255, 255, 80, 255])

# RGB(?) 🟢
green_Bot = np.array([0, 135, 20, 255])
green_Top = np.array([95, 255, 90, 255])

# RGB(?) 🔴
red_Bot = np.array([45, 35, 160, 255])
red_Top = np.array([145, 100, 250, 255])
        
# RGB(?) ❗
test_Bot = np.array([0, 0, 0, 255])
test_Top = np.array([0, 0, 0, 255])
                

# Function for 4 video streamings sectors
def videoStream():
    global raw, sec_0

    while(True):
        if(loop == False):
            break

        raw = stream.read()
        sec_0 = raw[0:(raw_size-1), 0:(raw_size-1)]
    
    print('\033[;35m'+'Loop Broken')
       
    # >>>>>>>>>>>>>>>> Copy this and -1 to the coords
    #sec_1 = raw[0:(raw_size-1), ((raw_size+raw_pad)-1):((2*(raw_size)+(raw_pad))-1)]
    #sec_2 = raw[0:(raw_size-1), ((2*(raw_size)+2*(raw_pad))-1):((3*(raw_size)+2*(raw_pad))-1)]
    #sec_3 = raw[0:(raw_size-1), ((3*(raw_size)+3*(raw_pad))-1):((4*(raw_size)+3*(raw_pad))-1)]

def sector1():
    global left, right, up, down, left_pass, right_pass, up_pass, down_pass

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> PURPLE-LEFT <<<<<<<<<<<<<<<<<<<<<<<<<<<
    procc = cv2.inRange(np.array(sec_0), purp_Bot, purp_Top)
    #procc = sec_0

    if(np.mean(procc) > 50):
        left = True
        if (left_pass != left):
            left_pass = left
            #print('Left on')
            #pyautogui.keyDown('left')
    else:
        left = False
        if (left_pass != left):
            left_pass = left
            #print('Left off')
            #pyautogui.keyUp('left')
            
    img = Image.fromarray(procc)
    imgtk = ITk.PhotoImage(image=img)
    lbls_img[0].imgtk = imgtk
    lbls_img[0].configure(image=imgtk)
    lbls_img[0].after(1, sector1)

    
def sector2():
    # >>>>>>>>>>>>>>>>>>>>>>>>>>> CIAN-DOWN <<<<<<<<<<<<<<<<<<<<<<<<<<<
    procc = cv2.inRange(np.array(sec_1), cian_Bot, cian_Top)

    if(np.mean(procc) > 50):
        down = True
        if (down_pass != down):
            down_pass = down
            #print('Down on')
            #pyautogui.keyDown('down')
    else:
        down = False
        if (down_pass != down):
            down_pass = down
            #print('Down off')
            #pyautogui.keyUp('down')
            
    img = Image.fromarray(procc)
    imgtk = ITk.PhotoImage(image=img)
    lbls_img[1].imgtk = imgtk
    lbls_img[1].configure(image=imgtk)
        
    # >>>>>>>>>>>>>>>>>>>>>>>>>>> GREEN-UP <<<<<<<<<<<<<<<<<<<<<<<<<<<
    procc = cv2.inRange(np.array(sec_2), green_Bot, green_Top)

    if(np.mean(procc) > 50):
        up = True
        if (up_pass != up):
            up_pass = up
            #print('Up on')
            #pyautogui.keyDown('up')
    else:
        up = False
        if (up_pass != up):
            up_pass = up
            #print('Up off')
            #pyautogui.keyUp('up')
            
    img = Image.fromarray(procc)
    imgtk = ITk.PhotoImage(image=img)
    lbls_img[2].imgtk = imgtk
    lbls_img[2].configure(image=imgtk)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>> RED-RIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<
    procc = cv2.inRange(np.array(sec_3), red_Bot, red_Top)

    if(np.mean(procc) > 50):
        right = True
        if (right_pass != right):
            right_pass = right
            #print('Right on')
            #pyautogui.keyDown('right')
    else:
        right = False
        if (right_pass != right):
            right_pass = right
            #print('Right off')
            #pyautogui.keyUp('right')
            

    img = Image.fromarray(procc)
    imgtk = ITk.PhotoImage(image=img)
    lbls_img[3].imgtk = imgtk
    lbls_img[3].configure(image=imgtk)
        
    
def start():
    global options, loop, stream, procc_0, procc_1

    if (loop):
        return 0
    
    options = {
        "top": coord_y,
        "left": coord_x,
        "width": ((4*raw_size)+(3*raw_pad)),
        "height": raw_size
    }
    loop = True
    stream = ScreenGear(monitor=1, logging=True, **options).start()


    procc_0 = threading.Thread(target=videoStream)
    procc_1 = threading.Thread(target=sector1)

    procc_0.start()
    procc_1.start()
    
def stop():
    global loop, stream

    try:
        stream.stop()
    except:
        print('Already stopped!')
    stream = []
    loop = False
    
def changeCoord():
    global coord_x, coord_y, loop

    stop()
    if(loop == False):
        coord_x = int(spn_B1.get())
        coord_y = int(spn_B2.get())
    
def changeSizePad():
    global raw_pad, raw_size

    stop()
    if(loop == False):
        raw_size = int(spn_B3.get())
        raw_pad = int(spn_B4.get())

# Test Color
def changeColor():
    global test_Bot, test_Top

    test_Bot = np.array([int(spn_test_B1.get()), int(spn_test_B2.get()), int(spn_test_B3.get()), 255])
    test_Top = np.array([int(spn_test_B4.get()), int(spn_test_B5.get()), int(spn_test_B6.get()), 255])
    
    print (
        f'Test Bottom: [{test_Bot[0]}, {test_Bot[1]}, {test_Bot[2]}, 255] - '+
        f'Test Top: [{test_Top[0]}, {test_Top[1]}, {test_Top[2]}, 255]'
    )


if(__name__ == '__main__'):
    # Prepare the window
    window = Tk()
    window.title("Roboto")
    window.geometry("400x370")
    #window.resizable(0, 0)

    # Components of the window
    # ------------------- Frame 1 start -------------------
    f1 = Frame()
    f1.config(bg="black")

    lbls_img = [
        Label(f1, borderwidth=0, highlightthickness=0),
        Label(f1, borderwidth=0, highlightthickness=0),
        Label(f1, borderwidth=0, highlightthickness=0),
        Label(f1, borderwidth=0, highlightthickness=0)
    ]

    lbls_img[0].pack(padx=25, pady=20, side=LEFT)
    lbls_img[1].pack(padx=25, pady=20, side=LEFT)
    lbls_img[2].pack(padx=25, pady=20, side=LEFT)
    lbls_img[3].pack(padx=25, pady=20, side=LEFT)

    f1.pack(fill=X)
    # -------------------  Frame 1 end  -------------------

    # ------------------- Frame 2 start -------------------
    f_c_0 = Frame()

    f2 = Frame(f_c_0)
    f3 = Frame(f_c_0)

    btn1 = Button(f2, text='Start', command = start)
    btn2 = Button(f3, text='Stop', command = stop)

    btn1.pack(padx=20)
    btn2.pack(padx=20)

    f2.pack(side=RIGHT, pady=30)
    f3.pack(side=LEFT, pady=30)

    f_c_0.pack()
    # -------------------  Frame 2 end  -------------------
# Color Force Start
    # ------------------- Frame 3-5 start -------------------
    f_test_1 = Frame()
    f_test_3 = Frame(f_test_1)
    f_test_4 = Frame(f_test_1)
    f_test_5 = Frame(f_test_1)
    
    spn_test_B1 = Spinbox(f_test_3, from_=0, to=255, increment=5, width=6, command= changeColor)
    spn_test_B2 = Spinbox(f_test_4, from_=0, to=255, increment=5, width=6, command= changeColor)
    spn_test_B3 = Spinbox(f_test_5, from_=0, to=255, increment=5, width=6, command= changeColor)

    Label(f_test_3, text='R').pack()
    Label(f_test_4, text='G').pack()
    Label(f_test_5, text='B').pack()
    spn_test_B1.pack()
    spn_test_B3.pack()
    spn_test_B2.pack()

    f_test_3.pack(side=LEFT)
    f_test_4.pack(side=LEFT)
    f_test_5.pack(side=LEFT)

    f_test_1.pack(fill=X, expand=True)
    # -------------------  Frame 3-5 end  -------------------
    
    # ------------------- Frame 6-9 start -------------------
    f_test_2 = Frame()
    f_test_6 = Frame(f_test_2)
    f_test_7 = Frame(f_test_2)
    f_test_8 = Frame(f_test_2)
    
    spn_test_B4 = Spinbox(f_test_6, from_=0, to=255, increment=5, width=6, command= changeColor)
    spn_test_B5 = Spinbox(f_test_7, from_=0, to=255, increment=5, width=6, command= changeColor)
    spn_test_B6 = Spinbox(f_test_8, from_=0, to=255, increment=5, width=6, command= changeColor)

    Label(f_test_6, text='R').pack()
    spn_test_B4.pack()
    Label(f_test_7, text='G').pack()
    spn_test_B5.pack()
    Label(f_test_8, text='B').pack()
    spn_test_B6.pack()
    
    f_test_6.pack(side=LEFT)
    f_test_7.pack(side=LEFT)
    f_test_8.pack(side=LEFT)

    f_test_2.pack(fill=X, expand=True)
    # -------------------  Frame 3-5 end  -------------------
# Color Force End

    f_c_1 = Frame()
    f_c_2 = Frame()
    
    f3 = Frame(f_c_1)
    f4 = Frame(f_c_1)

    Label(f3, text='X').pack()
    v1 = StringVar()
    spn_B1 = Spinbox(f3, from_=0, to=1500, increment=5, width=6, textvariable=v1, command= changeCoord)
    v1.set(1250)
    spn_B1.pack()

    Label(f4, text='Y').pack()
    v2 = StringVar()
    spn_B2 = Spinbox(f4, from_=0, to=1000, increment=5, width=6, textvariable=v2, command= changeCoord)
    v2.set(200)
    spn_B2.pack()
    
    f5 = Frame(f_c_2)
    f6 = Frame(f_c_2)

    Label(f5, text='Size').pack()
    v3 = StringVar()
    spn_B3 = Spinbox(f5, from_=0, to=100, increment=5, width=6, textvariable=v3, command= changeSizePad)
    v3.set(50)
    spn_B3.pack()

    Label(f6, text='Pad').pack()
    v4 = StringVar()
    spn_B4 = Spinbox(f6, from_=0, to=100, increment=2, width=6, textvariable=v4, command= changeSizePad)
    v4.set(70)
    spn_B4.pack()

    f4.pack(padx=20, side=RIGHT)
    f3.pack(padx=20, side=RIGHT)
    f5.pack(padx=20, side=LEFT)
    f6.pack(padx=20, side=LEFT)

    f_c_1.pack(side=LEFT)
    f_c_2.pack(side=RIGHT)

    window.mainloop()

    try:
        stream.stop()
    except:
        pass