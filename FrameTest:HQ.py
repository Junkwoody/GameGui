from tkinter import *

window = Tk()
window.geometry('1920x1080')
window.eval('tk::PlaceWindow . center')
window.title('Name of Game')
window.attributes('-fullscreen', True)
window.bind('<p>',
	lambda event: window.attributes('-fullscreen', not window.attributes('-fullscreen')))

frame = Frame(window)
frame.pack()
lbl = Label(frame, text="HEADQUARTERS", font=('MS Sans Serif',80))
lbl.grid(column=0, row=0)

txt = Entry(frame,width=10)
txt.grid(column=0, row=2)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.mainloop()
