from tkinter import *

SEC = 5
LOC = 2
loc_timer = None
global_timer = None

sec_2_len = 0
sec_1_len = 0


# function to start the timer

def start_timer():
    # prompt.delete("1.0", END)
    prompt.focus()
    loc = LOC
    local_count_down(loc)


# this function will check the length of the prompt
def local_count_down(sec):
    global sec_2_len
    global sec_1_len, loc_timer
    if sec == 2:
        sec_2_len = len(prompt.get("1.0", END))
        loc_timer = window.after(1000, local_count_down, sec - 1)
    if sec == 1:
        sec_1_len = len(prompt.get("1.0", END))
        loc_timer = window.after(1000, local_count_down, sec - 1)
    if sec == 0:
        if sec_1_len == sec_2_len:
            window.after_cancel(loc_timer)
            global_count_down(SEC)
        else:
            window.after(1000, local_count_down, sec + 2)


# this function will start the timer for 5 sec
def global_count_down(sec):
    global sec_1_len, sec_2_len, global_timer

    sec_1_len = len(prompt.get("1.0", END))
    if sec == 0:
        window.after_cancel(global_timer)
        prompt.delete("1.0", END)
        prompt.focus()

    if sec_1_len == sec_2_len:
        global_timer = window.after(1000, global_count_down, sec - 1)
    else:
        window.after_cancel(global_timer)
        local_count_down(LOC)


# ###########################--------UI SETUP--------##################################################

window = Tk()
window.title("Disappearing text prompt")
window.minsize(500, 300)
window.config(padx=10, pady=5)

title_label = Label(text="Write Your Story", font=('Courier', 24, 'bold'))
title_label.pack(pady=10)

prompt = Text(width=50, height=10, font=('Microsoft Tai Le', 14, 'normal'), bg="#fefbd8")
prompt.pack(pady=10)

button = Button(text="Start", command=start_timer, bg="#987d9a", fg="white", font=("Courier", 16, 'bold'))
button.pack(pady=10)

window.mainloop()
