import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
import re
import pywhatkit
import dearpygui.dearpygui as dpg
import keyboard
from tkinter import *
from tkinter import ttk
def reading():

    try:
        Tk().withdraw()
        filename=askopenfilename()
        readtable=pd.read_excel(filename)
        input_a = dpg.get_value('Column')
        input_b = int(input_a)
        input_c=input_b-1
        select_rows = readtable.iloc[:,input_c]
        print(select_rows)
        np.savetxt('rowtable.txt', select_rows, fmt='%r')
    except Exception as error1:
        print(str(error1))
        pass
    try:
        rowtable=open('rowtable.txt','r+')
        done_table=open('done_table.txt','w+')
        regex = r'[^\n,0-9]'
        reading_row_table=rowtable.read()
        matches = re.sub(regex,'',reading_row_table)
        # finallymatches=re.sub(',.*', '', matches, flags=re.DOTALL)
        print(matches)
        done_table.write(''.join(matches))
    except Exception as error2:
        print(str(error2))
        pass
def formattable():

    try:
        rowtable=open('rowtable.txt','r+')
        done_table=open('done_table.txt','w+')
        regex = r'[^\n,0-9]'
        reading_row_table=rowtable.read()
        matches = re.sub(regex,'',reading_row_table)
        # finallymatches=re.sub(',.*', '', matches, flags=re.DOTALL)
        print(matches)
        done_table.write(''.join(matches))
    except Exception as error2:
        print(str(error2))
        pass

def Terminate():
    global send_whatsapp_message
    return(send_whatsapp_message)
keyboard.add_hotkey('esc',Terminate)
def send_whatsapp_message():                               
    speedsend=dpg.get_value('speedsend')
    speedclose=dpg.get_value('speedclose')
    speedsend2=int(speedsend)
    speedclose2=int(speedclose)

    try:
        done_table=open('done_table.txt', 'r')
        for line in done_table:
            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone_no='+'+line,
                    message=msg,
                    tab_close=True,
                    wait_time=speedsend2,
                    close_time=speedclose2
                )
            except Exception as e:
                print(str(e))
            with open('done_table.txt', 'r') as f:
                lines = f.readlines()
            with open('done_table.txt', 'w') as f:
                f.writelines(lines[1:])
            with open('message.txt', 'r',encoding='utf-8') as f:
                msg = f.readline()
        done_table.close()
    except Exception as error3:
        print(str(error3))
        pass
def enter_msg():
    def show_message():
        label = entry.get()     # получаем введенный текст
        label2=str(label)
        file=open('message.txt','w+',encoding='utf-8')
        file.write(label2)
        root.destroy()
        
    root = Tk()
    root.title("Запись сообщения")
    root.geometry("500x200") 
    
    entry = ttk.Entry()
    entry.pack(anchor=NW, padx=6, pady=6,ipadx=200,ipady=20)
    
    btn = ttk.Button(text="Записать текст и закрыть", command=show_message)
    btn.pack(anchor=NW, padx=6, pady=6)
    
    label = ttk.Label()
    label.pack(anchor=NW, padx=6, pady=6)
    
    root.mainloop()