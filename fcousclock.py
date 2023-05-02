import time
import tkinter as tk

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timeformat)
        time.sleep(1)
        t -= 1
    timer_label.config(text='Time up!')

root = tk.Tk()
root.title("Focus Timer")
root.geometry("300x100")

timer_label = tk.Label(root, font=('Helvetica', 48), text='25:00')
timer_label.pack()

start_button = tk.Button(root, text="Start", command=lambda: countdown_timer(1500))
start_button.pack(side=tk.LEFT, padx=20)

stop_button = tk.Button(root, text="Stop", command=root.destroy)
stop_button.pack(side=tk.RIGHT, padx=20)

root.mainloop()
