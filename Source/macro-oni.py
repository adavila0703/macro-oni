from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key
from pynput import mouse, keyboard
import time, os, re, sys, glob, errno
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack()
        #self.create_widgets()

    def create_widgets(self):
        '''self.test = tk.Entry(self, text="Test ", fg="black", width=20)
        self.test.pack(side="left")

        self.startrecording = tk.Button(self, text="Start Recording Macro", fg="black", command=macro_on, width = 20)
        self.startrecording.pack(side="left")

        self.saverecording = tk.Button(self, text="Save Macro", fg="black", command=saverecording, width=20)
        self.saverecording.pack(side="left")

        self.playrecording = tk.Button(self, text="Play Macro", fg="black", command=playmacro, width=20)
        self.playrecording.pack(side="left")


        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")'''

    def say_random(self):
            print("safsadf")

    def say_hi(self):
            print("hi there, everyone!")

def seconds():
    global counter
    create_file.writelines(str(counter) + "\n")
    return counter

def counting():
    global counter
    counter += .0001
    return 0

def on_move(x, y):
    counting()
    return 0

def on_click(x, y, button, pressed):
    dx = str(x)
    dy = str(y)
    if pressed and button == Button.left:
        create_file.writelines(dx + "|" + dy + "\n")
        create_file.writelines("left" + "\n")
        return False
    if pressed and button == Button.right:
        create_file.writelines(dx + "|" + dy + "\n")
        create_file.writelines("right" + "\n")
        return False

def clickcheck():
    global click_verify


def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))
    global progon
    progon = False


def on_press(key):
    return 0

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def recording():
    global counter
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll,) as listener:
        listener.join()
        seconds()
        counter = 0

def saverecording():
    create_file.close()
    refresh()

def macro_on():
    global create_file, listcount, progon, final_path
    progon = True
    listcount = 0
    file_name = pro_name.get()
    create_file = open(final_path + "\\" + file_name +".txt", "w")
    while progon == True:
        recording()
    pro_name.delete(0, "end")

def playmacro():
    index_selected = stored_prog.curselection()
    file_list = os.listdir(final_path)
    file = file_list[index_selected[0]]
    selected_file = open(final_path + "\\" +file, "r")
    lines = selected_file.readlines()
    dx = ""
    dy = ""
    count = 0
    multiplyer = int(speed_multi.get())
    macrostart = m1.position
    for l in lines:
        search_chord = re.findall(r"\|", l)
        search_sec = re.findall(r"\.", l)
        is_cord = bool(search_chord)
        is_sec = bool(search_sec)
        if is_cord == True:
            split_1 = l.split("|")
            dx = split_1[0]
            dy = split_1[1]
            m1.position = (dx, dy)
        still_going = m1.position
        if l == "left\n":
            m1.click(Button.left)
        if l == "right\n":
            m1.click(Button.right)
        if is_sec == True:
            timein = float(l)
            addmult = timein * multiplyer
            time.sleep(addmult)
        if m1.position != still_going:
            break
    m1.position = macrostart

def refresh():
    file = os.listdir(final_path)
    count = 0
    for f in file:
        if stored_prog.get(count) != f:
            stored_prog.insert(count, f)
        count += 1

def deletemacro():
    index_selected = stored_prog.curselection()
    file_list = os.listdir(final_path)
    file = file_list[index_selected[0]]
    os.remove(final_path + "\\" + file)
    stored_prog.delete(index_selected)



#controllers
m1 = Controller()
#bools
progon = True
writing = True
flipflop = True
mess_bool = True

#files

#ints
counter = 0
listcount = 1
click_verify = 0
multiplyer = 0

#string
mess_counter = ""


## MAIN FUNCTION ##
#os.getcwd()
checkingpath = "programs"
is_file = os.path.isdir(checkingpath)
final_path = os.path.join(os.getcwd(), checkingpath)
if is_file == False:
    os.mkdir(final_path)

root = tk.Tk()
app = Application(master=root)



#spin box
#spin = tk.Spinbox(root, from_ = 0, to = 1000)


#APP VISUALS
pro_label = tk.Label(root, text="Enter Program Name", fg="black").grid(row=1, column=1)
pro_name = tk.Entry(root, text="Test ", fg="black", width=20)
pro_name.grid(row=2, column=1)

speed_txt = tk.Label(root, text="Macro Speed", fg="black", width=20).grid(row=3, column=1, pady=1)
speed_multi = tk.Scale(root, from_=10, to=1, orient="horizontal")
speed_multi.grid(row=4, column=1, pady=5)
speed_multi.set(5)

startrecording = tk.Button(root, text="Start Recording Macro", fg="black", command=macro_on, width = 20).grid(row=5, column=1)

saverecording = tk.Button(root, text="Save Macro", fg="black", command=saverecording, width=20).grid(row=6, column=1)

playrecording = tk.Button(root, text="Play Macro", fg="black", command=playmacro, width=20).grid(row=7, column=1)

delete_macro = tk.Button(root, text="Delete Macro", fg="black", command=deletemacro, width=20).grid(row=8, column=1)


refresh_button = tk.Button(root, text="Refresh", fg="black", command=refresh, width=10).grid(row=25, column=2)


output_txt = tk.Label(root, text="Saved Programs", fg="black", width=20).grid(row=1, column=2)
stored_prog = tk.Listbox(root, height=8, width=35)
stored_prog.grid(row=2, column=2, columnspan=10, rowspan=10, padx=30)




quit = tk.Button(root, text="QUIT", fg="red", command=root.destroy).grid(row=25, column=1, pady=5)

version_label = tk.Label(root, text="v0.5", fg="black").grid(row=30, column=4)
#FRAME / SIZE
size = tk.Canvas(root, width=5, height=30).grid(row=100, column=100)
tk.Frame(root, borderwidth=1, relief="ridge")

#icon
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='macro-oni-icon.png'))

#app title
root.title("Macro-oni")

#app menu
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#get all stored programs
refresh()

#app exec
app.mainloop()