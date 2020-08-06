from tkinter import *
import time

root = Tk()
root.overrideredirect(1)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',True)
#root.state('zoomed')
time_comparison = ''
clock = Label(root, font=('bold', 15, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
def tick():
    global time_comparison
    time2 = time.strftime('%H:%M:%S')
    if time2 != time_comparison:
        time_comparison = time2
        clock.config(text=time2)
        # вызовы идут каждые 200 милисекунд
    clock.after(200, tick)
root.lift()
tick()
root.mainloop()