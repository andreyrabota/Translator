import tkinter
import csv


class CsvDict:
    def read(self):
        with open('data_en2ru.csv') as file:
            datadict = {}
            reader = csv.reader(file)
            for row in reader:
                k, v = row
                datadict[k] = v
            return datadict

    def addi(self, slovo, perevod):
        with open('data_en2ru.csv') as file:
            datadict1 = {}
            reader = csv.reader(file)
            for row in reader:
                k, v = row
                datadict1[k] = v
            try:
                if slovo not in datadict1:
                    with open('data_en2ru.csv', 'a', newline='') as file_wr:
                        writer = csv.writer(file_wr)
                        writer.writerow([slovo, perevod])

                else:
                    print('yje est')
            except ValueError:
                print('chtoto poshlo ne tak')

raw_data = CsvDict()
datadict = raw_data.read()
# {'Wolf': 'Волк', 'Bear': 'Медведь', 'Snowman': 'Снеговик', 'Cop': 'Полицейский', 'Cat': 'Кошка'}
###
def random_key(datadict):
    import random
    return random.choice(list(datadict.keys()))


######################################################
def click_button_check():
    if pole_vvoda.get().casefold() == datadict[rand_slovo.get()].casefold():
        data.set('pravilno')
        pole_vvoda.delete(0, 'end')
        rand_slovo.set(random_key(datadict))
    else:
        data.set('nepravilno, poprobyite eshe raz')

def admin_btn_click():
    admin_window()



def admin_window():

    window2  = tkinter.Toplevel(main_window)
    frame2 = tkinter.Frame(window2)
    st_label2 = tkinter.Label(frame2, text='vvedite slovo i perevod')
    pole_vvoda_key = tkinter.Entry(frame2)
    pole_vvoda_value = tkinter.Entry(frame2)
    var_label2 = tkinter.Label(frame2, text = 'varvar')

    def add_value():
        slovo, perevod = pole_vvoda_key.get(), pole_vvoda_value.get()
        print(slovo,perevod)
        added = CsvDict()
        added.addi(slovo,perevod)
        pole_vvoda_key.delete(0, 'end')
        pole_vvoda_value.delete(0, 'end')

    button_add = tkinter.Button(frame2, text='Add', command=add_value)
    button_exit2 = tkinter.Button(frame2, text='Return', command=window2.destroy)
    st_label2.pack()
    frame2.pack()
    pole_vvoda_key.pack()
    pole_vvoda_value.pack()
    var_label2.pack()
    button_add.pack()
    button_exit2.pack()



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
admin_btn = tkinter.Button(frame, text = 'adminka', command = admin_btn_click)
button_exit = tkinter.Button(frame, text = 'Exit', command = quit)

frame.pack()
slovo_angl.pack()
st_label.pack()
pole_vvoda.pack()
otvet.pack()
button_check.pack()
admin_btn.pack()
button_exit.pack()
main_window.mainloop()
