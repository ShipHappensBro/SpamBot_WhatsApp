from __future__ import unicode_literals
import os
import dearpygui.dearpygui as dpg
import Functions_of_maingui


def bd_ok():
    Functions_of_maingui.reading(),dpg.configure_item('bd',show=False)
def license_is_true():
    dpg.create_context()
    with dpg.font_registry():
        with dpg.font(f'C:\\Windows\\Fonts\\Gabriola.ttf', 20, default_font=True, id="Default font",):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            dpg.add_char_remap(0xa8, 0x401)
            dpg.add_char_remap(0xb8, 0x451)
            utf = 0x410
            for i in range(0xc0, 0x100):
              dpg.add_char_remap(i, utf)
              utf += 1
              
            
    dpg.bind_font("Default font")
    dpg.create_viewport(title='Automized', width=600, height=800,clear_color=[237, 206, 206, 1],resizable=False,min_width=600,max_width=600,min_height=800,max_height=800,x_pos=0,y_pos=0,small_icon='smallico.ico')
    
    
    with dpg.window(label="SelectBD_and_formating",modal=True,show=False,tag="bd",no_title_bar=True,width=600,height=300,pos=[0,200],no_move=True,no_resize=True):
        dpg.add_text("Введите номер столбца с номерами телефона в поле 'Введите номер столбца'\n\nГде столбец A=1,B=2,C=3,D=4 и т.д \n\nПосле нажмите кнопку 'Выбрать базу данных'\n И выберите необходимый файл формата xlsx или xls\n\n")
        dpg.add_separator()
        with dpg.group(horizontal=False):
            dpg.add_input_text(label="Введите номер столбца##inputtext",tag='Column')
            dpg.add_button(label="Выбрать базу данных",width=200,height=50,callback=bd_ok)
            dpg.add_button(label="Отмена",width=75,callback=lambda:dpg.configure_item("bd",show=False))
    with dpg.window(label="Выбор базы данных",no_move=True,no_close=True,no_resize=True,no_collapse=True,width=280):
        dpg.add_button(label="Выбрать",width=300,height=200,callback=lambda:dpg.configure_item("bd", show=True))


    with dpg.window(label="SpamBot",modal=True,show=False,tag="wu",no_title_bar=True,width=580,height=300,pos=[0,200],no_move=True,no_resize=True):
        dpg.add_text("Рассылка в WhatsApp\n\nПрежде чем начать операцию,убедитесь что вы авторизованы в WhatsApp\n\n!!Скорость измеряется в секундах,будьте аккуратнее,чем выше скорость,\nтем выше требования к соединению и системе\n\nРекомендуемые значения 7 и 2\n\nВведите требуемый текст для рассылки и нажмите 'НАЧАТЬ'\n\nРекомендуется не пользоваться комьютером во время выполнения операции")
        dpg.add_separator()
        dpg.add_button(label="Ввести текст сообщения",width=200,height=50,callback=Functions_of_maingui.enter_msg)
        dpg.add_separator()
        dpg.add_input_text(label="Скорость отправки##inputtext",tag='speedsend')
        dpg.add_separator()
        dpg.add_input_text(label="Скорость закрытия##inputtext",tag='speedclose')
        dpg.add_separator()
        dpg.add_button(label="НАЧАТЬ",width=200,height=50,callback=Functions_of_maingui.send_whatsapp_message)
        dpg.add_button(label="Отмена",width=75,callback=lambda:dpg.configure_item("wu",show=False))


    with dpg.window(label="Рассылка в WhatsApp",no_move=True,no_close=True,no_resize=True,no_collapse=True,width=310,pos=[280,0]):
        dpg.add_button(label="Начать",width=300,height=200,callback=lambda:dpg.configure_item("wu", show=True))


    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()




def license_was_failed():
    dpg.create_context()
    with dpg.font_registry():
        with dpg.font(f'C:\\Windows\\Fonts\\Gabriola.ttf', 20, default_font=True, id="Default font",):
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
            dpg.add_char_remap(0xa8, 0x401)
            dpg.add_char_remap(0xb8, 0x451)
             # set counter value equal to utf8 code of Russian capital "А" with consequent remapping from "А" to "я"
            utf = 0x410
            for i in range(0xc0, 0x100):
              dpg.add_char_remap(i, utf)
              utf += 1
    dpg.bind_font("Default font")
    def check_license():
        key=dpg.get_value('license')
        if key=='F987E-K001S-NMH4Q-P99UI':
            with open('license.txt','r+') as f:
                f.write(key)
            dpg.destroy_context()
        else:
            dpg.add_text('Неверный ключ лицензии',parent='kek')
    with dpg.window(label="ВВЕДИТЕ КЛЮЧ ЛИЦЕНЗИИ",no_move=True,no_close=True,no_resize=True,no_collapse=True,width=500,height=300,tag='kek'):
        dpg.add_input_text(label="Введите Ключ##inputtext",tag='license')
        dpg.add_button(label='ENTER',callback=check_license)
    dpg.create_viewport(title='LICENSE', width=500, height=300,clear_color=[237, 206, 206, 1],resizable=False,min_width=500,max_width=500,min_height=300,max_height=300,x_pos=0,y_pos=0,small_icon='smallico.ico')
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()




license_key=str('F987E-K001S-NMH4Q-P99UI')
license_file='license.txt'
if os.path.isfile(license_file):
    with open('license.txt','r') as f:
        lines = f.readlines()
        if license_key in lines:
            license_is_true()
        else:
            license_was_failed()
else:
    with open('license.txt','w+') as f:
        license_was_failed()