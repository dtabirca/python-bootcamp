from tkinter import *
import win32api
import random


class App(Frame):

    label = Label()
    width = 150
    height = 50

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.master.wm_state('iconic')
        self.master.title("Still here?")
        self.master.minsize(self.width, self.height)
        self.label.place(x=5, y=5)
        self.label['font'] = ('Arial', 14)
        for monitor in win32api.EnumDisplayMonitors():
            monitor_info = win32api.GetMonitorInfo(monitor[0])
            if monitor_info['Flags'] == 1:
                break
        work_area = monitor_info['Work']
        x = work_area[2]-self.width
        y = work_area[3]-self.height-50
        self.master.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))
        self.master.resizable(False, False)
        self.master.wm_attributes('-topmost', True)
        self.master.attributes('-disabled', True)
        self.master.attributes('-alpha', 0.7)
        self.master.deiconify()
        self.countdown()

    def countdown(self):
        time = int((win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0)
        self.label['fg'] = 'red'
        if time <= 59:
            self.label['fg'] = 'black'
            display = str(time) + 's'#
        elif time < 3600:
            display = str(int(time/60)) + 'm'#min
        elif time < 86400:
            display = str(int(time/3600)) + 'h'#h
        else:
            display = '---'#out of scale
        self.label['text'] = 'Inactive for ' + display
        #if time > 60:# 1min
        #    self.master.deiconify()
        self.after(1000, self.countdown)


myapp = App()
myapp.mainloop()
