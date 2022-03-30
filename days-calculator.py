from tkinter import *
import datetime as dt
from tkinter import font
import tkinter.ttk as ttk
from functools import partial
from datetime import datetime
from tkinter import messagebox


date = dt.datetime.now()

window = Tk()
title = Label(window, text='Date Calculator', font=("Arial", 20, font.BOLD), fg='#0560B6').pack(pady=25)

def main():
    style = ttk.Style(window)
    window.tk.call('source', '/Users/Amarn/OneDrive - Da Vinci College/Da Vinci College/software_developen/Assignments/jaar_1/periode_1/fase_1/08_wat_zie_ik_nou_GUI-beuren/leerpad_03/gui-formulieren/themes/sun-valley.tcl')
    style.theme_use('sun-valley-light')
     
    centerFrame = Frame(window)
    centerFrame.pack(pady=0)
    
    monthDay = f'{date:%d}'
    monthName = f'{date:%b}'
    year = f'{date:%Y}'
    
    window.title('Days Calculator')
    window.geometry('400x220')
       
    monthDayStringVar = StringVar(window)
    monthDayStringVar.set(monthDay)
    
    monthNameStringVar = StringVar(window)
    monthNameStringVar.set(monthName)
       
    print(monthDay)
    print(monthName)
    print(year)
    
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthDaysList = []

    monthList.insert(0, monthName)
    def monthDayAmount(monthName):
        print(monthName)

        if monthName in {'Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'}:
            monthDayAmountVar = 32
            print('31 days')
        if monthName == 'Feb':
            monthDayAmountVar = 29
            print('28 days')
        if monthName in {'Apr', 'Jun', 'Sep', 'Nov'}:
            monthDayAmountVar = 31
            print('30 days')

        return monthDayAmountVar                           
        
    monthDayAmountVar = monthDayAmount(monthName)

    def monthDayAmountFunction(monthDayAmountVar):         
        monthDaysList.append(monthDay)
        score = 1
        for a in range(1, monthDayAmountVar):
            score = a

            monthDaysList.append(score)
    monthDayAmountFunction(monthDayAmountVar)            


    monthDayDropdown = ttk.OptionMenu(centerFrame, monthDayStringVar, *monthDaysList)
    monthDayDropdown.config(width=6)
    monthDayDropdown.pack(side=LEFT)
    
    

    line1 = Label(centerFrame, text='-', font=("Arial", 15, font.BOLD), fg='#0560B6')
    line1.pack(side=LEFT)
    
    monthNameDropdown = ttk.OptionMenu(centerFrame, monthNameStringVar, *monthList)
    monthNameDropdown.config(width=6)
    monthNameDropdown.pack(side=LEFT)

    def displaySelected(*args):
        monthDaysList.clear()
        monthName = monthNameStringVar.get()
        monthDayAmountVar = monthDayAmount(monthName)
        monthDayAmountFunction(monthDayAmountVar)
        menu = monthDayDropdown['menu']            
        menu.delete(0, 'end')
        if monthDay == monthDaysList[0]:
            monthDaysList.pop(0) 
        for string in monthDaysList: 
            menu.add_command(label=string, command=partial(monthDayStringVar.set, string))
        monthDayStringVarStr = monthDayStringVar.get().split()
        monthDayStringVarStrOnly = int(monthDayStringVarStr[0]) 
        if monthDayStringVarStrOnly in monthDaysList:
            pass
        else:            
            monthDayStringVar.set(monthDaysList[len(monthDaysList)-1])
                       
        return monthDayAmountVar, monthName
    
    traceCommand = monthNameStringVar.trace
    traceCommand('w', displaySelected)

    
    line2 = Label(centerFrame, text='-', font=("Arial", 15, font.BOLD), fg='#0560B6')
    line2.pack(side=LEFT)
    
    yearEntry = ttk.Entry(centerFrame)
    yearEntry.insert(END, year)
    yearEntry.config(width=10)
    yearEntry.pack(side=LEFT)
    
    def buttonClick():
        selectedMonthDay = monthDayStringVar.get()
        selectedMonthName = monthNameStringVar.get()
        userInputYear = yearEntry.get()
              
        selectedMonthNameNumber = datetime.strptime(selectedMonthName, '%b').month
        todayMonthNameNumber = datetime.strptime(monthName, '%b').month
               
        date_format = "%m/%d/%Y"
        today = datetime.strptime(f'{todayMonthNameNumber}/{monthDay}/{year}', date_format)
        selectedDate = datetime.strptime(f'{selectedMonthNameNumber}/{selectedMonthDay}/{userInputYear}', date_format)
        delta = selectedDate - today
        deltaStr = f'{delta}'
        selectedDate=deltaStr.split()
        differenceDays = selectedDate[0]
        
        if differenceDays == '-1':
            differenceDaysWithoutDash = differenceDays.replace('-','')
            messagebox.showinfo(None, f'Dit is {differenceDaysWithoutDash} dag geleden')
        elif differenceDays < '0':
            differenceDaysWithoutDash = differenceDays.replace('-','')
            messagebox.showinfo(None, f'Dit is {differenceDaysWithoutDash} dagen geleden')
        elif differenceDays == '0:00:00':    
            messagebox.showinfo(None, f'Dit is vandaag')
        elif differenceDays == '1':
            messagebox.showinfo(None, f'Dit is {differenceDays} dag in de toekomst')            
        else: 
            messagebox.showinfo(None, f'Dit is {differenceDays} dagen in de toekomst' )
                
            
    def button():
        goButton = ttk.Button(window, text="GO", style="Accent.TButton", comman=buttonClick)
        goButton.config(width=10)
        goButton.pack(side=TOP, pady=33)
    button()
    




main()

window.mainloop()