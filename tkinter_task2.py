import tkinter
datadict = {'Wolf': 'Волк', 'Bear': 'Медведь', 'Snowman': 'Снеговик', 'Cop': 'Полицейский', 'Cat': 'Кошка'}
###
def random_key(datadict):
    import random
    return random.choice(list(datadict.keys()))


######################################################
def click_button_check():
    if pole_vvoda.get() == datadict[rand_slovo.get()].lower():
        data.set('pravilno')
        pole_vvoda.delete(0, 'end')
        rand_slovo.set(random_key(datadict))
    else:
        data.set('nepravilno, poprobyite eshe raz')

def quit():
    from sys import exit
    exit()

main_window = tkinter.Tk()
frame = tkinter.Frame(main_window)
rand_slovo = tkinter.StringVar()
rand_slovo.set(random_key(datadict))
slovo_angl = tkinter.Label(frame, textvariable = rand_slovo)
st_label = tkinter.Label(frame, text = 'vvedite perevod slova')
data = tkinter.StringVar()

pole_vvoda = tkinter.Entry(frame)

otvet = tkinter.Label(frame, textvariable = data)
button_check = tkinter.Button(frame, text = 'proverit', command = click_button_check)
button_exit = tkinter.Button(frame, text = 'Exit', command = quit)

frame.pack()
slovo_angl.pack()
st_label.pack()
pole_vvoda.pack()
otvet.pack()
button_check.pack()
button_exit.pack()
main_window.mainloop()
