from datetime import timedelta, date, datetime
import datetime
import urllib.request
import xml.dom.minidom
from tkinter import *
from tkinter.ttk import Notebook, Frame, Combobox, Radiobutton
import dateutil.relativedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# date
today = date.today()
date_ = date.today().strftime("%d/%m/%Y")
today = date.today()

last_monday_1 = today + datetime.timedelta(days=-today.weekday())
last_monday_2 = today + datetime.timedelta(days=-today.weekday(), weeks=-1)
last_monday_3 = today + datetime.timedelta(days=-today.weekday(), weeks=-2)
last_monday_4 = today + datetime.timedelta(days=-today.weekday(), weeks=-3)

sundey_1 = today + datetime.timedelta(6) - datetime.timedelta(days=today.weekday())
sundey_2 = today + datetime.timedelta(6) - datetime.timedelta(days=today.weekday(), weeks=1)
sundey_3 = today + datetime.timedelta(6) - datetime.timedelta(days=today.weekday(), weeks=2)
sundey_4 = today + datetime.timedelta(6) - datetime.timedelta(days=today.weekday(), weeks=3)

mondey_normal = last_monday_1.strftime("%d/%m/%Y")
sundey_normal = sundey_1.strftime("%d/%m/%Y")
mondey_normal_1 = last_monday_2.strftime("%d/%m/%Y")
sundey_normal_1 = sundey_2.strftime("%d/%m/%Y")
mondey_normal_2 = last_monday_3.strftime("%d/%m/%Y")
sundey_normal_2 = sundey_3.strftime("%d/%m/%Y")
mondey_normal_3 = last_monday_4.strftime("%d/%m/%Y")
sundey_normal_3 = sundey_4.strftime("%d/%m/%Y")
week_m = []
week_1 = mondey_normal + " - " + sundey_normal
week_2 = mondey_normal_1 + " - " + sundey_normal_1
week_3 = mondey_normal_2 + " - " + sundey_normal_2
week_4 = mondey_normal_3 + " - " + sundey_normal_3

week_m.append(week_1)
week_m.append(week_2)
week_m.append(week_3)
week_m.append(week_4)

#parth

valute_slov = {}
temp = ['1', '1']
valute_slov['Российский рубль'] = temp
valute_name = []
valute_name.append('Российский рубль')
url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + date_
response = urllib.request.urlopen(url)
dom = xml.dom.minidom.parse(response)
dom.normalize()
nodeArray = dom.getElementsByTagName("Valute")

for node in nodeArray:
    childList = node.childNodes
    name__ = ''
    val = []
    for child in childList:

        if child.nodeName == "Nominal" or child.nodeName == "Value":
            val.append(child.childNodes[0].nodeValue)
        if child.nodeName == "Name":
            name__ = child.childNodes[0].nodeValue
            valute_name.append(child.childNodes[0].nodeValue)
    valute_slov[name__] = val



# GUI

window = Tk()
window.title("Конвертер валют")
window.geometry("600x400")

# Главное окно
tab_control = Notebook(window)
tab1 = Frame(tab_control)
tab_control.add(tab1, text="Калькулятор валют")


# Дополнительное окно
tab2 = Frame(tab_control)
tab_control.add(tab2, text="Динамика курса")
tab_control.pack(expand = True, fill = BOTH)


# Действия

def print_graph(x, y):
    fig = plt.figure(100)
    plt.clf()
    plt.xlabel('Дата', fontsize=15)
    plt.ylabel('Курс', fontsize=15)
    plt.plot(y, x)
    canvas = FigureCanvasTkAgg(fig, master=tab2)
    plot_widget = canvas.get_tk_widget()
    plot_widget.place(relheight=0.6, relwidth=1, relx=0, rely=0.35)
    fig.canvas.draw()

def parth_(_date, valute_for_gr):
    if valute_for_gr == 'Российский рубль':
        temp = ['1', '1']
        return temp

    val = []
    prov = 0
    url_2 = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=" + _date
    response_2 = urllib.request.urlopen(url_2)
    dom_2 = xml.dom.minidom.parse(response_2)
    dom_2.normalize()
    #print(url_2)
    nodeArray_2 = dom_2.getElementsByTagName("Valute")
    for node in nodeArray_2:
        childList = node.childNodes
        val = []
        for child in childList:
            if child.nodeName == "Nominal" or child.nodeName == "Value":
                val.append(child.childNodes[0].nodeValue)
            if child.childNodes[0].nodeValue == valute_for_gr:
                prov = 1
        if prov == 1:
            return val

def click1(event):
    sum_ = entry1.get()
    try:
        sum_ = float(sum_)
    except ValueError:
        return None

    valute_1 = combobox1.get()
    valute_2 = combobox2.get()
    val_1_1 = valute_slov[valute_1][0].replace(",", ".")
    val_1_2 = valute_slov[valute_1][1].replace(",", ".")
    val_2_1 = valute_slov[valute_2][0].replace(",", ".")
    val_2_2 = valute_slov[valute_2][1].replace(",", ".")
    k_1 = float(val_1_2) / float(val_1_1)
    k_2 = float(val_2_2) / float(val_2_1)
    sum_v_rub = sum_ * k_1
    answer_v = round(sum_v_rub / k_2, 3)
    label1['text'] = ' '.join(str(answer_v))

def conventor_date(n):
    if n.find('январь') == 0:
        return '01'
    if n.find('февраль') == 0:
        return '02'
    if n.find('март') == 0:
        return '03'
    if n.find('апрель') == 0:
        return '04'
    if n.find('май') == 0:
        return '05'
    if n.find('июнь') == 0:
        return '06'
    if n.find('июль') == 0:
        return '07'
    if n.find('август') == 0:
        return '08'
    if n.find('сентябрь') == 0:
        return '09'
    if n.find('октябрь') == 0:
        return '10'
    if n.find('ноябрь') == 0:
        return '11'
    if n.find('декабрь') == 0:
        return '12'

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def opred_month_for_cvartal(n):
    if(n.find("январь - март") == 0):
        return '01-04'
    if(n.find("апрель - июнь") == 0):
        return '04-07'
    if(n.find("июль - сентябрь") == 0):
        return '07-10'
    if(n.find("октябрь - декабрь") == 0):
        return '10-01'

def opred_month(n):
    if(n == 1):
        return "январь"
    if (n == 2):
        return "февраль"
    if (n == 3):
        return "март"
    if (n == 4):
        return "апрель"
    if (n == 5):
        return "май"
    if (n == 6):
        return "июнь"
    if (n == 7):
        return "июль"
    if (n == 8):
        return "август"
    if (n == 9):
        return "сентябрь"
    if (n == 10):
        return "октябрь"
    if (n == 11):
        return "ноябрь"
    if (n == 12):
        return "декабрь"

def click2(event):
    period = r_var.get()
    date_find = combobox4.get()
    valute_for_graph = combobox3.get()

    if period == 0:
        start_week_ = date_find[0:10:1]
        finish_week_ = date_find[13:23:1]
        start_week = datetime.datetime.strptime(start_week_, "%d/%m/%Y")
        finish_week = datetime.datetime.strptime(finish_week_, "%d/%m/%Y")
        finish_week = finish_week + datetime.timedelta(1)
        nd = finish_week_[0:2:1]
        td = str(today)
        td = td[len(td) - 2: len(td): 1]
        year__ = date_find[len(date_find) - 4: len(date_find): 1]
        month__ = date_find[3: 5: 1]
        if int(nd) > int(td) and int(month__) >= int(today.month):
            finish_week_ = str(today)
            finish_week = datetime.datetime.strptime(finish_week_, "%Y-%m-%d")
            finish_week = finish_week + datetime.timedelta(1)
        x_for_graph = []
        y_for_graph = []
        for single_date in daterange(start_week, finish_week):
            curs_for_graph = []
            tmp = single_date.strftime("%d/%m/%Y")
            curs_for_graph = parth_(tmp, valute_for_graph)
            x_for_graph.append(float(curs_for_graph[1].replace(",", ".")) / float(curs_for_graph[0].replace(",", ".")))
            y_for_graph.append(single_date.strftime("%d"))
        print_graph(x_for_graph, y_for_graph)

    if period == 1:
        month__ = conventor_date(date_find)
        year__ = date_find[len(date_find) - 4: len(date_find): 1]
        data__ = year__ + '-' + month__ + '-01'
        m_1 = datetime.datetime.strptime(data__, "%Y-%m-%d")
        m_2 = m_1 - dateutil.relativedelta.relativedelta(months=-1)
        nd = str(m_2)[len(str(m_2)) - 11 :len(str(m_2)) - 9 :1]
        td = str(today)
        td = td[len(td) - 2: len(td): 1]
        month__ = date_find[0: len(date_find)-5: 1]
        month__ = conventor_date(month__)
        if int(month__) == int(today.month):
            m_2_ = str(today)
            m_2 = datetime.datetime.strptime(m_2_, "%Y-%m-%d")
            m_2 = m_2 + datetime.timedelta(1)
        x_for_graph = []
        y_for_graph = []
        for single_date in daterange(m_1, m_2):
            curs_for_graph = []
            tmp = single_date.strftime("%d/%m/%Y")
            curs_for_graph = parth_(tmp, valute_for_graph)
            x_for_graph.append(float(curs_for_graph[1].replace(",", ".")) / float(curs_for_graph[0].replace(",", ".")))
            y_for_graph.append(single_date.strftime("%d"))
        print_graph(x_for_graph, y_for_graph)

    if period == 2:
        chisla_month = opred_month_for_cvartal(date_find)
        first_month = chisla_month[0:2:1]
        second_month = chisla_month[3:5:1]
        year__ = date_find[len(date_find) - 4: len(date_find): 1]
        data__1 = year__ + '-' + first_month + '-01'
        data__2 = year__ + '-' + second_month + '-01'
        c_1 = datetime.datetime.strptime(data__1, "%Y-%m-%d")
        c_2 = c_1 - dateutil.relativedelta.relativedelta(months=-3)
        c_2 = c_2.strftime("%Y-%m-%d")
        c_3 = datetime.datetime.strptime(c_2, "%Y-%m-%d")
        nd = str(c_3)
        nd = nd[5 :7: 1]
        td = str(today)
        td = td[5: 7: 1]
        print(int(today.year))
        if int(nd) > int(td) and int(year__) >= int(today.year):
            c_2 = str(today)
            c_3 = datetime.datetime.strptime(c_2, "%Y-%m-%d")
            c_3 = c_3 + datetime.timedelta(1)
        x_for_graph = []
        y_for_graph = []
        kk = 0
        for single_date in daterange(c_1, c_3):
            if kk % 7 == 0:
                curs_for_graph = []
                tmp = single_date.strftime("%d/%m/%Y")
                curs_for_graph = parth_(tmp, valute_for_graph)
                if(curs_for_graph != None):
                    x_for_graph.append(float(curs_for_graph[1].replace(",", ".")) / float(curs_for_graph[0].replace(",", ".")))
                    y_for_graph.append(single_date.strftime("%d.%m"))
            kk += 1
        print_graph(x_for_graph, y_for_graph)

    if period == 3:
        year__ = date_find
        year_chislo = int(date_find) + 1
        data_first_ = year__ + '-01-01'
        data_second_ = str(year_chislo) + '-01-01'
        y_1 = datetime.datetime.strptime(data_first_, "%Y-%m-%d")
        y_2 = datetime.datetime.strptime(data_second_, "%Y-%m-%d")
        if int(year__) >= int(today.year):
            y_3 = str(today)
            y_2 = datetime.datetime.strptime(y_3, "%Y-%m-%d")
        x_for_graph = []
        y_for_graph = []
        kk = 0
        que = 0
        for single_date in daterange(y_1, y_2):
            if int(single_date.strftime("%m")) > que:
                que = int(single_date.strftime("%m"))
                curs_for_graph = []
                tmp = single_date.strftime("%d/%m/%Y")
                curs_for_graph = parth_(tmp, valute_for_graph)
                if(curs_for_graph != None):
                    x_for_graph.append(float(curs_for_graph[1].replace(",", ".")) / float(curs_for_graph[0].replace(",", ".")))
                    y_for_graph.append(opred_month(int(single_date.strftime("%m"))))
            kk += 1
        print_graph(x_for_graph, y_for_graph)

def weeek_(event):
    date_ishod = date.today()
    today = date.today()
    wd = date.weekday(today)

    mondey = date_ishod.today() - datetime.timedelta(wd)
    sundey = mondey + datetime.timedelta(wd)
    mondey_1 = mondey - datetime.timedelta(wd+1)
    sundey_1 = mondey_1 + datetime.timedelta(wd)
    mondey_2 = mondey_1 - datetime.timedelta(wd+1)
    sundey_2 = mondey_2  + datetime.timedelta(wd)
    mondey_3 = mondey_2 - datetime.timedelta(wd+1)
    sundey_3 = mondey_3 + datetime.timedelta(wd)

    mondey_normal = mondey.strftime("%d/%m/%Y")
    sundey_normal = sundey.strftime("%d/%m/%Y")
    mondey_normal_1 = mondey_1.strftime("%d/%m/%Y")
    sundey_normal_1 = sundey_1.strftime("%d/%m/%Y")
    mondey_normal_2 = mondey_2.strftime("%d/%m/%Y")
    sundey_normal_2 = sundey_2.strftime("%d/%m/%Y")
    mondey_normal_3 = mondey_3.strftime("%d/%m/%Y")
    sundey_normal_3 = sundey_3.strftime("%d/%m/%Y")
    week_m = []
    week_1 = mondey_normal + " - " + sundey_normal
    week_2 = mondey_normal_1 + " - " + sundey_normal_1
    week_3 = mondey_normal_2 + " - " + sundey_normal_2
    week_4 = mondey_normal_3 + " - " + sundey_normal_3
    week_m.append(week_1)
    week_m.append(week_2)
    week_m.append(week_3)
    week_m.append(week_4)
    combobox4["values"] = (week_m)
    combobox4.current(0)

def month_(event):
    month_massiv = []
    m_1 = today.replace(day=1)
    m_2 = m_1 + dateutil.relativedelta.relativedelta(months=-1)
    m_3 = m_2 + dateutil.relativedelta.relativedelta(months=-1)
    m_4 = m_3 + dateutil.relativedelta.relativedelta(months=-1)
    month_massiv.append(m_1.strftime(opred_month(m_1.month) + " %Y"))
    month_massiv.append(m_2.strftime(opred_month(m_2.month) + " %Y"))
    month_massiv.append(m_3.strftime(opred_month(m_3.month) + " %Y"))
    month_massiv.append(m_4.strftime(opred_month(m_4.month) + " %Y"))
    combobox4["values"] = (month_massiv)
    combobox4.current(0)

def opred_cvartal(n):
    if(n <= 3):
        return "январь - март "
    if(n >= 4 and n <= 6):
        return "апрель - июнь "
    if(n >= 7 and n <= 9):
        return "июль - сентябрь "
    if(n >= 10 and n <= 12):
        return "октябрь - декабрь "

def cvartal(event):
    cvartal_massiv = []
    m_1 = today.replace(day=1)
    m_2 = m_1 + dateutil.relativedelta.relativedelta(months=-3)
    m_3 = m_2 + dateutil.relativedelta.relativedelta(months=-3)
    m_4 = m_3 + dateutil.relativedelta.relativedelta(months=-3)
    c_1 = opred_cvartal(m_1.month)
    с_2 = opred_cvartal(m_2.month)
    с_3 = opred_cvartal(m_3.month)
    с_4 = opred_cvartal(m_4.month)
    cvartal_massiv.append(m_1.strftime(c_1 + "%Y"))
    cvartal_massiv.append(m_2.strftime(с_2 + "%Y"))
    cvartal_massiv.append(m_3.strftime(с_3 + "%Y"))
    cvartal_massiv.append(m_4.strftime(с_4 + "%Y"))
    combobox4["values"] = (cvartal_massiv)
    combobox4.current(0)

def year_(event):
    year_massiv = []
    year_massiv.append(today.year)
    year_massiv.append(today.year - 1)
    year_massiv.append(today.year - 2)
    year_massiv.append(today.year - 3)
    combobox4["values"] = (year_massiv)
    combobox4.current(0)

# В этой части добавляются элементы главного меню

btn1 = Button(tab1, text="Конвертировать",
              bg="Light gray",
              fg="Black",
              # font = ("Times New Roman"),
              bd=2,
              justify=CENTER,
              heigh=2,
              width=15
              )
btn1.place(relheight=0.1, relwidth=0.2, relx=0.75, rely=0.1)

btn1.bind('<Button-1>', click1)

label1 = Label(tab1, text="Вычисляем...",
               bg="Light gray",
               fg="Black",
               font=("Times new Roman", 10, "bold"),
               bd=10,
               justify=CENTER,
               heigh=2,
               width=15)

label1.place(relheight=0.1, relwidth=0.45, relx=0.5, rely=0.3)

entry1 = Entry(tab1, width=40)
entry1.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.1)

combobox1 = Combobox(tab1)
combobox1["values"] = (valute_name)
combobox1.current(0)
combobox1.place(relheight=0.1, relwidth=0.4, relx=0.055, rely=0.1)

combobox2 = Combobox(tab1)
combobox2["values"] = (valute_name)
combobox2.current(1)
combobox2.place(relheight=0.1, relwidth=0.4, relx=0.055, rely=0.3)

# В этой части добавляются элементы дополнительного меню

btn2 = Button(tab2, text="Построить график",
              bg="Light gray",
              fg="Black",
              #font=("Times new Roman", 1, "bold"),
              bd=2,
              justify=CENTER,
              heigh=2,
              width=15
              )
btn2.place(relheight=0.1, relwidth=0.2, relx=0.025, rely=0.225)

btn2.bind('<Button-1>', click2)

label2 = Label(tab2, text="Валюта",
               bd=10,
               justify=CENTER,
               heigh=2,
               width=15)

label2.place(relheight=0.1, relwidth=0.1, relx=0.05, rely=0.01)

label3 = Label(tab2, text="Период",
               bd=10,
               justify=CENTER,
               heigh=2,
               width=15)

label3.place(relheight=0.1, relwidth=0.1, relx=0.25, rely=0.01)

label4 = Label(tab2, text="Выбор периода",
               bd=10,
               justify=CENTER,
               heigh=2,
               width=15)

label4.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.01)

r_var = IntVar()
r_var.set(0)

r1 = Radiobutton(tab2, text='Неделя', variable=r_var, value=0)
r1.place(relheight=0.05, relwidth=0.2, relx=0.25, rely=0.1)
r1.bind('<Button-1>', weeek_)

r2 = Radiobutton(tab2, text='Месяц', variable=r_var, value=1)
r2.place(relheight=0.05, relwidth=0.2, relx=0.25, rely=0.15)
r2.bind('<Button-1>', month_)

r3 = Radiobutton(tab2, text='Квартал', variable=r_var, value=2)
r3.place(relheight=0.05, relwidth=0.2, relx=0.25, rely=0.2)
r3.bind('<Button-1>', cvartal)

r4 = Radiobutton(tab2, text='Год', variable=r_var, value=3)
r4.place(relheight=0.05, relwidth=0.2, relx=0.25, rely=0.25)
r4.bind('<Button-1>', year_)

combobox3 = Combobox(tab2)
combobox3["values"] = (valute_name)
combobox3.current(1)
combobox3.place(relheight=0.1, relwidth=0.2, relx=0.025, rely=0.1)

combobox4 = Combobox(tab2)
combobox4["values"] = (week_m)
combobox4.current(0)
combobox4.place(relheight=0.1, relwidth=0.15, relx=0.4, rely=0.1)



window.mainloop()

