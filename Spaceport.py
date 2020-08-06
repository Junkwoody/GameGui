from tkinter import *

window = Tk()
window.geometry('1920x1080')
window.eval('tk::PlaceWindow . center')
window.title('Name of Game')
window.attributes('-fullscreen', True)
window.bind('<f>',
	lambda event: window.attributes('-fullscreen', not window.attributes('-fullscreen')))

lbl = Label(window, text="SPACEPORT", font=('MS Sans Serif',80))
lbl.grid(column=0, row=0)

btn = Button(window, text=' HQ ', font=('MS Sans Serif', 60))
btn.grid(column=1, row=2)
btn = Button(window, text='DOCK', font=('MS Sans Serif', 60))
btn.grid(column=2, row=2)
btn = Button(window, text='TRADE DEPOT', font=('MS Sans Serif', 60))
btn.grid(column=3, row=2)
btn = Button(window, text='EXIT', font=('MS Sans Serif', 60))
btn.grid(column=3, row=3)

window.mainloop()

'''
The buttons don't do anything yet, I'll look at frames and whatnot
but here's a basic (Read: garbage) window with stuffs
'''
