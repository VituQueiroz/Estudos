import customtkinter
import pyautogui as pa
from time import sleep

def fecha_chamado():
    pa.PAUSE = 1

    analista = int(analista_entry.get())
    n = int(n_entry.get())

    pa.press('win')
    sleep(0.5)
    pa.write('chrome')
    sleep(0.5)
    pa.press('enter')
    sleep(3)
    pa.hotkey('win','up')
    pa.write('https://painel.f5sg.com.br/support/dashboard')
    pa.press('enter')
    sleep(10)
    pa.moveTo(x=21, y=305)
    pa.click(x=94, y=370)
    sleep(3)
    pa.press('tab', presses=2)
    pa.press('enter')
    pa.press('down', presses=3)
    pa.press('enter')
    pa.press('tab', presses=2)
    pa.press('enter')

    if analista == 1:
        pa.press('enter')
    elif analista == 2:
        pa.press('down')
        pa.press('enter')
    elif analista == 3:
        pa.press('down', presses=2)
        pa.press('enter')
    elif analista == 4:
        pa.press('down', presses=3)
        pa.press('enter')
    elif analista == 5:
        pa.press('down', presses=4)
        pa.press('enter')
    elif analista == 6:
        pa.press('down', presses=5)
        pa.press('enter')
    elif analista == 7:
        pa.press('down', presses=6)
        pa.press('enter')
    elif analista == 8:
        pa.press('down', presses=7)
        pa.press('enter')

    pa.scroll(-200)
    pa.click(x=218, y=818)
    sleep(3)

    for _ in range(n):
        pa.click(x=619, y=279)
        sleep(1.5)
        pa.click(x=735, y=162)
        pa.press('tab', presses=3)
        pa.press('enter')
        pa.press('tab', presses=3)
        pa.press('enter')
        sleep(2)
        pa.click(x=735, y=162)
        pa.press('tab', presses=9)
        pa.hotkey('ctrl','c')
        pa.click(x=21, y=62)
        sleep(0.5)
        pa.click(x=735, y=162)
        pa.press('tab', presses=7)
        pa.hotkey('ctrl','v')
        pa.press('tab', presses=20)
        pa.press('enter')
        sleep(1)
        pa.press('tab', presses=3)
        pa.write('Atendimento via WhatsApp.')
        pa.press('tab')
        pa.write('Atendimento via WhatsApp.')
        pa.press('tab', presses=4)
        pa.press('enter')
        sleep(1.5)
        pa.click(x=21, y=62)
        sleep(1.5)
        pa.click(x=93, y=63)
        sleep(2)

janela = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")

janela.title("Fechamento de Chamado")
janela.geometry("400x400")
janela.configure(bg='antiquewhite')

user = customtkinter.CTkLabel(janela, text="1 - Todos\n2 - Cobrança\n3 - Daniel Bonatti\n4 - Dayvid Oliveira\n5 - José Roberto\n6 - Luna\n7 - Rodrigo Bonatti\n8 - Victor Homem")
user.pack(pady=20)

analista_entry = customtkinter.CTkEntry(janela, placeholder_text='Digite o N° do usuário')
analista_entry.pack(pady=20)

n_entry = customtkinter.CTkEntry(janela, placeholder_text='Qtd Chamados')
n_entry.pack(pady=20)

fechar = customtkinter.CTkButton(janela, text="Fechar Chamados", command=fecha_chamado)
fechar.pack(pady=20)

janela.mainloop()