from tkinter import *
import pyautogui as pa
from time import sleep

def fecha_chamado():
    pa.PAUSE = 1

    print("Qual analista? ")
    print("1 - Todos")
    print("2 - Cobrança")
    print("3 - Daniel Bonatti")
    print("4 - Dayvid Oliveira")
    print("5 - José Roberto")
    print("6 - Luna")
    print("7 - Rodrigo Bonatti")
    print("8 - Victor Homem")
    analista = int(input("Digite o número: "))
    n = int(input("Quantos chamados fechar? "))

    pa.click(x=124, y=880) # ABRE O GOOGLE
    pa.hotkey('ctrl', 't') # ABRE A JANELA DE CHAMADO
    pa.write('https://painel.f5sg.com.br/support/dashboard') # ABRE O LINK DO PAINEL
    pa.press('enter')
    sleep(10)
    pa.moveTo(x=21, y=305) # VAI ATÉ A PARTE DE CHAMADO NA LISTA
    pa.click(x=94, y=370) # CLICA NA LISTA DE CHAMADOS
    sleep(3)
    pa.press('tab', presses=2) # TAB 2 VEZES PARA IR ATÉ O TIPO DE CHAMADO
    pa.press('enter') # ABRE O TIPO DE CHAMADO
    pa.press('down', presses=3) # VAI ATÉ "DUVIDAS E FUNCIONALIDADE"
    pa.press('enter') # "SELECIONA DUVIDAS E FUNCIONALIDADES"
    pa.press('tab', presses=2) # VAI ATÉ O ANALISTA
    pa.press('enter') # SELECIONA O CAMPO DE ANALISTA

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

    pa.scroll(-200) # ROLA A TELA
    pa.click(x=218, y=818) # CLICA EM PESQUISAR
    sleep(3)

    for i in range(n):
        pa.click(x=619, y=279) # CLICA NO CHAMADO 
        sleep(1.5)
        pa.click(x=735, y=162) # CLICA NA TELA SUPERIOR
        pa.press('tab', presses=3) # VAI ATÉ O BOTÃO DE OPÇÃO
        pa.press('enter') # ABRE O BOTÃO DE OPÇÃO
        pa.press('tab', presses=3) # VAI ATE VER LICENÇA
        pa.press('enter') # ABRE A LICENÇA
        sleep(2)
        pa.click(x=735, y=162) # CLICA NA TELA SUPERIOR
        pa.press('tab', presses=9) # VAI ATÉ O NOME DA LICENÇA
        pa.hotkey('ctrl','c') # COPIA A LICENÇA
        pa.click(x=21, y=62) # CLICA NA SETA DE VOLTAR PÁGINA
        sleep(1)
        pa.click(x=735, y=162) # CLICA NA TELA SUPERIOR
        sleep(3)
        pa.press('tab', presses=7) # VAI ATÉ O CONTATO
        sleep(1)
        pa.hotkey('ctrl','v') # COLA O NOME
        sleep(1)
        pa.press('tab', presses=20) # VAI ATE O FECHAMENTO
        sleep(1)
        pa.press('enter') # ABRE O FECHAMENTO
        sleep(1)
        pa.press('tab', presses=3) # BOX1
        pa.write('Atendimento via WhatsApp.') # FECHAMENTO PUB
        pa.press('tab') #BOX2
        pa.write('Atendimento via WhatsApp.') # FECHAMENTO PRIV
        pa.press('tab', presses=4) # FECHAR
        sleep(1)
        pa.press('enter') # CONCLUI
        sleep(2)
        pa.click(x=21, y=62) # SETA PARA VOLTAR PÁGINA
        sleep(2.5)
        pa.click(x=93, y=63) # RECARREGA AS PÁGINAS
        sleep(2.5)

janela = Tk()
janela.title("Fechamento de Chamado")

texto = Label(janela, text="Teste")
texto.grid(column=0, row=0)

fechar = Button(janela, text="Fechar Chamados", command=fecha_chamado)
fechar.grid(column=0, row=1)

janela.mainloop()