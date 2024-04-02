import random
import tkinter as tk
import os

x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the image path relative to the 'img' directory
impath = os.path.join(current_dir, 'img')

# Example usage of the image path
idle_path = os.path.join(impath, 'idlecat.gif')
sleep_path = os.path.join(impath, 'sleeping.gif')
drowsy_path = os.path.join(impath, 'drowsy.gif')
waking_path = os.path.join(impath, 'waking.gif')
walkleft_path = os.path.join(impath, 'walkleft.gif')
walkright_path = os.path.join(impath, 'walkright.gif')


def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100, update, cycle, check, event_number, x)  # no 8,9 = walk towards right
    elif event_number in sleep_num:
        check = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10,11,12,13,15 = sleep
    elif event_number == 14:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 15 = sleep to idle


def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


def update(cycle, check, event_number, x):
    # idle
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)

    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    # sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    # walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3
    # walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x -= -3
    window.geometry('100x100+' + str(x) + '+'+str(win_height - 140))
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)

window = tk.Tk()  
win_height = window.winfo_screenheight()

# call buddy's action gif
idle = [tk.PhotoImage(file=idle_path, format='gif -index %i' % (i)) for i in range(5)]  # idle gif
idle_to_sleep = [tk.PhotoImage(file=drowsy_path, format='gif -index %i' % (i)) for i in range(8)]  # idle to sleep gif
sleep = [tk.PhotoImage(file=sleep_path, format='gif -index %i' % (i)) for i in range(3)]  # sleep gif
sleep_to_idle = [
    tk.PhotoImage(file=waking_path, format='gif -index %i' % (i)) for i in range(8)]  # sleep to idle gif
walk_positive = [
    tk.PhotoImage(file=walkleft_path, format='gif -index %i' % (i)) for i in range(8)]  # walk to left gif
walk_negative = [
    tk.PhotoImage(file=walkright_path, format='gif -index %i' % (i)) for i in range(8)]  # walk to right gif

menu = tk.Menu(window, tearoff=0)
menu.add_command(label="Exit", command=window.destroy)

# Configure window
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black', '-topmost', True)

# Create and place the label
label = tk.Label(window, bd=0, bg='black')
label.pack()

# Bind the right-click event to show the menu
label.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

# Start the update loop
window.after(1, update, cycle, check, event_number, x)

# Start the Tkinter main loop
window.mainloop()