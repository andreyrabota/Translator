import tkinter, csv, re, random


class CsvDict:
    def read(self):
        with open('data_en2ru.csv') as file:
            datadict1 = {}
            reader = csv.reader(file)
            for row in reader:
                k, v = row
                datadict1[k] = v
            return datadict1

    def quant(self):
        return len(CsvDict.read(self))

    def addi(self, slovo, perevod):
        datadict1 = CsvDict.read(self)
        try:
            with open('data_en2ru.csv', 'a', newline='') as file_wr:
                writer = csv.writer(file_wr)
                writer.writerow([slovo, perevod])
        except ValueError:
            print('chtoto poshlo ne tak')

    def dele(self, a):
        data1 = CsvDict.read(self)
        del data1[a]
        with open('data_en2ru.csv', 'w', newline='') as file_saved:
            writer = csv.writer(file_saved)
            for key, value in data1.items():
                writer.writerow([key,value])

raw_data = CsvDict()
datadict = raw_data.read()


def random_key(datadict):
    return random.choice(list(datadict.keys()))

######################################################


def validate(slovo):
    p = re.compile('(^[^A-Za-zА-Яа-яЁё])|([^A-Za-zА-Яа-яЁё~\-\'])')
    if p.search(slovo) is not None:
        return False
    elif len(slovo) < 2 or len(slovo) > 20:
        return False
    else:
        return True


def click_button_check():
    if pole_vvoda.get().casefold() == datadict[rand_slovo.get()].casefold():
        data.set('Все верно')
        pole_vvoda.delete(0, 'end')
        rand_slovo.set(random_key(datadict))
    else:
        data.set('Неправильно, попробуйте еще раз')


def admin_btn_click():
    admin_window()
    main_window.withdraw()


def admin_window():

    window2 = tkinter.Toplevel(main_window)
    frame2 = tkinter.Frame(window2)
    st_label2 = tkinter.Label(frame2, text='Введите слово и перевод:')
    pole_vvoda_key = tkinter.Entry(frame2)
    pole_vvoda_value = tkinter.Entry(frame2)
    alert_event = tkinter.StringVar()
    quant = tkinter.StringVar()
    showquan = CsvDict()
    quant.set('У Вас в словаре {0} слов'.format(showquan.quant()))

    var_label2 = tkinter.Label(frame2, textvariable=alert_event)

    def button_exit2_click():
        main_window.deiconify()
        window2.destroy()

    def add_value():
        slovo, perevod = str(pole_vvoda_key.get()).lower(), pole_vvoda_value.get()
        added = CsvDict()
        if validate(slovo) is False or validate(perevod) is False:
            alert_event.set('Неверный ввод данных')
        elif slovo in added.read():
            alert_event.set('Такое слово уже есть')
        else:
            added.addi(slovo,perevod)
            pole_vvoda_key.delete(0, 'end')
            pole_vvoda_value.delete(0, 'end')
            alert_event.set('{0} - {1} добавлены в словарь'.format(slovo, perevod))
            quant.set('У Вас в словаре {0} слов'.format(showquan.quant()))

    def del_value():
        slovo = str(pole_vvoda_key.get()).lower()
        deleted = CsvDict()
        if slovo not in deleted.read():
            alert_event.set('Такого слова нет в словаре')
        else:
            deleted.dele(slovo)
            pole_vvoda_key.delete(0, 'end')
            alert_event.set('Слово {0} удалено из словаря'.format(slovo))
            quant.set('У Вас в словаре {0} слов'.format(showquan.quant()))

    lab_quant = tkinter.Label(frame2, textvariable=quant)
    button_add = tkinter.Button(frame2, text='Добавить слово', command=add_value)
    button_del = tkinter.Button(frame2, text='Удалить слово', command=del_value)
    button_exit2 = tkinter.Button(frame2, text='Вернуться', command=button_exit2_click)
    st_label2.pack()
    frame2.pack()
    pole_vvoda_key.pack()
    pole_vvoda_value.pack()
    var_label2.pack()
    lab_quant.pack()
    button_add.pack()
    button_del.pack()
    button_exit2.pack()


def quit():
    from sys import exit
    exit()


main_window = tkinter.Tk()
frame = tkinter.Frame(main_window)
rand_slovo = tkinter.StringVar()
rand_slovo.set(random_key(datadict))
slovo_angl = tkinter.Label(frame, textvariable=rand_slovo)
st_label = tkinter.Label(frame, text='Введите перевод слова')
data = tkinter.StringVar()

pole_vvoda = tkinter.Entry(frame)

otvet = tkinter.Label(frame, textvariable=data)
button_check = tkinter.Button(frame, text='Проверить', command=click_button_check)
admin_btn = tkinter.Button(frame, text='Управление словарем', command=admin_btn_click)
button_exit = tkinter.Button(frame, text='Выход', command=quit)

frame.pack()
slovo_angl.pack()
st_label.pack()
pole_vvoda.pack()
otvet.pack()
button_check.pack()
admin_btn.pack()
button_exit.pack()
main_window.mainloop()
