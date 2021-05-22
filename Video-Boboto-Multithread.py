#Do NOT delete. Really important stuffs =)
from vidgear.gears import ScreenGear
from tkinter import *

import threading
import PIL.ImageTk as ITk
import numpy as np
import cv2, pyautogui

# X 1270 - Y 190  Size 50 - Padd 70 

# THE CLASS
class videoForce:
    def __init__(self):
        # Variables
        self.options = {}
        self.stream = []
        self.loop = True
        self.terminated = False

        self.raw_size = 50
        self.raw_pad = 70

        self.coord_x = 1250
        self.coord_y = 200

        self.left = False
        self.left_pass = None
        self.down = False
        self.down_pass = None
        self.up = False
        self.up_pass = None
        self.right = False
        self.right_pass = None

        # Init HSV
        # Variables for masking
        # HSV 🟣
        self.purp_Bot = np.array([115, 115, 130]) #[135, 90, 145]) #[100, 35, 95])    #[115, 115, 130]
        self.purp_Top = np.array([150, 220, 245]) #[150, 190, 190]) #[155, 210, 250]) #[150, 220, 245]

        # HSV 🔵
        self.cian_Bot = np.array([25, 130, 210]) #[30, 135, 190]) #[25, 160, 150]) #[25, 130, 210]
        self.cian_Top = np.array([35, 255, 255]) #[35, 250, 255]) #[45, 255, 255]) #[35, 255, 255]

        # HSV 🟢
        self.green_Bot = np.array([55, 85, 200]) #[45, 95, 200]) #[45, 95, 140]) #[55, 85, 200]
        self.green_Top = np.array([75, 250, 250]) #[70, 245, 255]) #[70, 250, 255]) #[75, 250, 250]

        # HSV 🔴
        self.red_Bot = np.array([115, 130, 140]) #[120, 115, 180]) #115, 115, 130]) #[115, 130, 140]
        self.red_Top = np.array([125, 205, 250]) #[130, 225, 245]) #[150, 220, 245]) #[125, 205, 250]
        
        # HSV ❗
        self.test_Bot = np.array([0, 0, 0]) 
        self.test_Top = np.array([0, 0, 0])
                

    # Function for 4 video streamings sectors
    def videoStream(self):
        if(self.loop == False):
            self.terminated = True
            return
        else:
            raw = cv2.cvtColor(self.stream.read(), cv2.COLOR_RGB2HSV)
            
            # >>>>>>>>>>>>>>>> Copy this and -1 to the coords
            sec_0 = raw[0:(self.raw_size-1), 0:(self.raw_size-1)]
            sec_1 = raw[0:(self.raw_size-1), ((self.raw_size+self.raw_pad)-1):((2*(self.raw_size)+(self.raw_pad))-1)]
            sec_2 = raw[0:(self.raw_size-1), ((2*(self.raw_size)+2*(self.raw_pad))-1):((3*(self.raw_size)+2*(self.raw_pad))-1)]
            sec_3 = raw[0:(self.raw_size-1), ((3*(self.raw_size)+3*(self.raw_pad))-1):((4*(self.raw_size)+3*(self.raw_pad))-1)]
            
            # Tests for arrays in 
            #print(f'Longitud: {len(scr)}  -  Longitud [0]: {len(scr[0])}')
            #print(f'Longitud sec: {len(sec_0)}  -  Longitud sec [0]: {len(sec_0[0])}')
            #print(f'capture: {cap}')
            #print(f'sector 1: {sec_1}')

        # >>>>>>>>>>>>>>>>>>>>>>>>>>> PURPLE-LEFT <<<<<<<<<<<<<<<<<<<<<<<<<<<
            procc = cv2.inRange(np.array(sec_0), self.purp_Bot, self.purp_Top)

            if(np.mean(procc) > 50):
                self.left = True
                if (self.left_pass != self.left):
                    self.left_pass = self.left
                    #print('Left on')
                    pyautogui.keyDown('left')
            else:
                self.left = False
                if (self.left_pass != self.left):
                    self.left_pass = self.left
                    #print('Left off')
                    pyautogui.keyUp('left')
            
            #img = Image.fromarray(procc)
            #imgtk = ITk.PhotoImage(image=img)
            #lbls_img[0].imgtk = imgtk
            #lbls_img[0].configure(image=imgtk)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>> CIAN-DOWN <<<<<<<<<<<<<<<<<<<<<<<<<<<
            procc = cv2.inRange(np.array(sec_1), self.cian_Bot, self.cian_Top)

            if(np.mean(procc) > 50):
                self.down = True
                if (self.down_pass != self.down):
                    self.down_pass = self.down
                    #print('Down on')
                    pyautogui.keyDown('down')
            else:
                self.down = False
                if (self.down_pass != self.down):
                    self.down_pass = self.down
                    #print('Down off')
                    pyautogui.keyUp('down')
            
            #img = Image.fromarray(procc)
            #imgtk = ITk.PhotoImage(image=img)
            #lbls_img[1].imgtk = imgtk
            #lbls_img[1].configure(image=imgtk)
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>> GREEN-UP <<<<<<<<<<<<<<<<<<<<<<<<<<<
            procc = cv2.inRange(np.array(sec_2), self.green_Bot, self.green_Top)

            if(np.mean(procc) > 50):
                self.up = True
                if (self.up_pass != self.up):
                    self.up_pass = self.up
                    #print('Up on')
                    pyautogui.keyDown('up')
            else:
                self.up = False
                if (self.up_pass != self.up):
                    self.up_pass = self.up
                    #print('Up off')
                    pyautogui.keyUp('up')
            
            #img = Image.fromarray(procc)
            #imgtk = ITk.PhotoImage(image=img)
            #lbls_img[2].imgtk = imgtk
            #lbls_img[2].configure(image=imgtk)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>> RED-RIGHT <<<<<<<<<<<<<<<<<<<<<<<<<<<
            procc = cv2.inRange(np.array(sec_3), self.red_Bot, self.red_Top)

            if(np.mean(procc) > 50):
                self.right = True
                if (self.right_pass != self.right):
                    self.right_pass = self.right
                    #print('Right on')
                    pyautogui.keyDown('right')
            else:
                self.right = False
                if (self.right_pass != self.right):
                    self.right_pass = self.right
                    #print('Right off')
                    pyautogui.keyUp('right')
            

            #img = Image.fromarray(procc)
            #imgtk = ITk.PhotoImage(image=img)
            #lbls_img[3].imgtk = imgtk
            #lbls_img[3].configure(image=imgtk)

            lbls_img[3].after(1, self.videoStream)
        
    
    def start(self):
        self.options = {
            "top": self.coord_y,
            "left": self.coord_x,
            "width": ((4*self.raw_size)+(3*self.raw_pad)),
            "height": self.raw_size
        }
        self.stream = ScreenGear(monitor=1, logging=True, **self.options).start()
        self.loop = True
        self.videoStream()
    
    def stop(self):
        self.stream = []
        self.loop = False
    
    def changeCoord(self):
        self.stop()
        if(self.terminated == True):
            self.coord_x = int(spn_B1.get())
            self.coord_y = int(spn_B2.get())
    
    def changeSizePad(self):
        self.stop()
        if(self.terminated == True):
            self.raw_size = int(spn_B3.get())
            self.raw_pad = int(spn_B4.get())

    # Test Color
    def changeColor(self):
        self.test_Bot = np.array([int(spn_test_B1.get()), int(spn_test_B2.get()), int(spn_test_B3.get())])
        self.test_Top = np.array([int(spn_test_B4.get()), int(spn_test_B5.get()), int(spn_test_B6.get())])
    
        print (
            f'Test Bottom: [{self.test_Bot[0]}, {self.test_Bot[1]}, {self.test_Bot[2]}] - '+
            f'Test Top: [{self.test_Top[0]}, {self.test_Top[1]}, {self.test_Top[2]}]'
        )


if(__name__ == '__main__'):
    broForce = videoForce()

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

    btn1 = Button(f2, text='Start', command = broForce.start)
    btn2 = Button(f3, text='Stop', command = broForce.stop)

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
    
    spn_test_B1 = Spinbox(f_test_3, from_=0, to=255, increment=5, width=6, command= broForce.changeColor)
    spn_test_B2 = Spinbox(f_test_4, from_=0, to=255, increment=5, width=6, command= broForce.changeColor)
    spn_test_B3 = Spinbox(f_test_5, from_=0, to=255, increment=5, width=6, command= broForce.changeColor)

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
    
    spn_test_B4 = Spinbox(f_test_6, from_=0, to=255, increment=5, width=6, command= broForce.changeColor)
    spn_test_B5 = Spinbox(f_test_7, from_=0, to=255, increment=5, width=6, command= broForce.changeColor)
    spn_test_B6 = Spinbox(f_test_8, from_=0, to=255, increment=5, width=6, command= broForce.changeColor)

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
    spn_B1 = Spinbox(f3, from_=0, to=1500, increment=10, width=6, textvariable=v1, command= broForce.changeCoord)
    v1.set(1250)
    spn_B1.pack()

    Label(f4, text='Y').pack()
    v2 = StringVar()
    spn_B2 = Spinbox(f4, from_=0, to=1000, increment=10, width=6, textvariable=v2, command= broForce.changeCoord)
    v2.set(200)
    spn_B2.pack()
    
    f5 = Frame(f_c_2)
    f6 = Frame(f_c_2)

    Label(f5, text='Size').pack()
    v3 = StringVar()
    spn_B3 = Spinbox(f5, from_=0, to=100, increment=10, width=6, textvariable=v3, command= broForce.changeSizePad)
    v3.set(50)
    spn_B3.pack()

    Label(f6, text='Pad').pack()
    v4 = StringVar()
    spn_B4 = Spinbox(f6, from_=0, to=100, increment=2, width=6, textvariable=v4, command= broForce.changeSizePad)
    v4.set(70)
    spn_B4.pack()

    f4.pack(padx=20, side=RIGHT)
    f3.pack(padx=20, side=RIGHT)
    f5.pack(padx=20, side=LEFT)
    f6.pack(padx=20, side=LEFT)

    f_c_1.pack(side=LEFT)
    f_c_2.pack(side=RIGHT)

    window.mainloop()