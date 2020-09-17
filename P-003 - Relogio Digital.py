from tkinter import *
from datetime import datetime


# constantes
FONTE_PEQUENA = "Courier 11 bold"
FONTE_GRANDE = "Courier 36 bold"
BACKGROUND = "#484848"
CORTEXTO1 = "#64FE2E"
CORTEXTO2 = "#FF8000"


class App:
    def __init__(self):
        """ Método construtor """
        
        # Criação da janela principal
        self.master = Tk()
        self.master.configure(background=BACKGROUND)
        self.master.geometry("250x100+200+200")
        self.master.title("@Noobpythonbr")
        
        # Criação  dos widgets da tela
        self.label_data = Label(self.master, text="", font=FONTE_PEQUENA, bg=BACKGROUND, fg=CORTEXTO1)
        self.label_data.place(x=10, y=10)
        
        self.label_hora = Label(self.master, text="", font=FONTE_GRANDE, bg=BACKGROUND, fg=CORTEXTO2)
        self.label_hora.place(x=10, y=40)
        
        self.botao_start = Button(self.master, text="START", font=FONTE_GRANDE)
        self.botao_start['command'] = self.start
        self.botao_start.place(x=30, y=35, w=190, h=40)
        
    def start(self):
        """ Função que obtém a data e hora do sistema e altera o texto das Labels a cada segundo
        com a data e hora atualizados """

        agora = datetime.now()        
        data = agora.strftime("%d/%m/%Y")
        hora = agora.strftime("%H:%M:%S")
        
        self.label_data['text'] = data
        self.label_hora['text'] = hora
        
        self.botao_start.destroy()
        
        self.master.after(1000, self.start)
                
    def run(self):
        """ O método mainloop mantém a janela aberta em um loop infinito """
        
        self.master.mainloop()


# Criação de uma instância (objeto) da classe App
relogio = App()
relogio.run()
