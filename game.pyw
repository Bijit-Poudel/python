from tkinter import *
window = Tk()
window.title("Game")
window.geometry("500x500")
window.resizable(False,False)
frame = Frame()
label = Label(frame,background = 'brown',text='GET STARTED!')

def button_start():
    label.configure(text = 'You clicked')
    

button1 = Button(text='Press me', background='red', command=button_start)








button1.place(relx=0.5,rely=0.5, anchor = CENTER)
label.pack()
frame.pack()
window.mainloop()
