import tkinter        
import cv2         
import threading   


from functools import partial
import imutils
import time

import PIL.Image, PIL.ImageTk  
 

SET_WIDTH = 650
SET_HEIGHT = 500

stream = cv2.VideoCapture("p.mp4")
def play(speed):
    print(f"The speed is {speed}")
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
        
        
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image = frame, anchor= tkinter.NW)


def pending(decision):
    frame = cv2.cvtColor(cv2.imread("DRS.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    canvas.create_text(300,30, fill ="black" , font= "times 26 bold", text= "huzaifa 3rd empire software " )
    time.sleep(4)
   
    
  
    frame = cv2.cvtColor(cv2.imread("index.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)
   
    
    time.sleep(3)
    
    
    if decision== 'out':
        decisionI = "index.jpg"
    else:
        decisionI = "notout.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionI), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width = SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame

    canvas.create_image(0,0,image = frame, anchor= tkinter.NW)
    
    
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1


    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


root = tkinter.Tk()       
root.title("huzaifa Qureshi third umpire Rewiew kit")  

cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(root,width=SET_WIDTH, height=SET_HEIGHT) 

\
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image = photo)
canvas.pack()




btn = tkinter.Button(root, text= "<Previous Fast", width=50, command=partial(play, -25))
btn.pack()

btn = tkinter.Button(root, text="<<Previous Slow", width=50, command=partial(play,-2))
btn.pack()

btn = tkinter.Button(root,text="Next (slow)>", width = 50, command=partial(play,2))
btn.pack()


photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, anchor = tkinter.NW, image = photo)
canvas.pack()

btn = tkinter.Button(root, text="Next fast >" , width = 50, command=partial(play,25))
btn.pack()

btn = tkinter.Button(root , text = "out " , width=50, command= partial(out,))
btn.pack()

btn = tkinter.Button(root,  text  ="Give not out" , width =50, command=partial(not_out,))
btn.pack()


root.mainloop()  

