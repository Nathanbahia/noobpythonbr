# Autor:     Nathan Bahia
# GitHub:    github.com/nathanbahia
# Instagram: instagram.com/noobpythonbr
# LinkedIn:  linkedin.com/in/nathanbahia

# Versão do Python: 3.8.3

import sqlite3
from tkinter import *
from tkinter import font

FONT_MD = "Courier 12 bold"
FONT_SM = "Courier 10"
BG = "#58D3F7"
FG = "#121212"

class Banco:
    def __init__(self):
        """ Inicia conexão com o banco de dados e cria tabela de usuários """
        
        self.conn = sqlite3.connect("database/users.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def create_user(self, username, password):
        """ Insere no banco de dados um novo usuário com username e password"""
        
        self.cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        self.conn.commit()
        return True


    def check_user(self, username, password):
        """ Verifica através dos parâmetros passados se há algum usuário com as mesmas credenciais e retorna
            True se encontrar, ou False caso contrário.
        """
        
        users = self.cursor.execute("SELECT * FROM users")
        for u in users.fetchall():
            if u[0] == username and u[1] == password:
                return True
        return False

banco = Banco()
        

class App:
    def __init__(self, master):
        """ Inicia a inteface gráfica do sistema """
        
        self.master = master
        self.master.configure(background=BG)

        self.img_login = PhotoImage(file="images/login.png")
        self.lbl_img_login = Label(self.master, image=self.img_login, bg=BG)
        self.lbl_img_login.image = self.img_login
        self.lbl_img_login.place(x=0, y=20, w=270)

        self.lbl_user = Label(self.master, text="Username", bg=BG, fg=FG, font=FONT_SM)
        self.lbl_user.place(x = 10, y = 100)

        self.lbl_pass = Label(self.master, text="Password", bg=BG, fg=FG, font=FONT_SM)
        self.lbl_pass.place(x = 10, y = 150)

        self.ent_user = Entry(self.master, font=FONT_MD)
        self.ent_user.focus()
        self.ent_user.place(x = 10, y = 125, w=250)

        self.ent_pass = Entry(self.master, show="*", font=FONT_MD)
        self.ent_pass.place(x = 10, y = 175, w=220)
        self.ent_pass_is_showing = False

        self.img_eye = PhotoImage(file="images/exibir.png")
        self.btn_eye = Label(self.master, image=self.img_eye, bg=BG)
        self.btn_eye.image=self.img_eye        
        self.btn_eye.bind("<Button-1>", self.show_password_login)
        self.btn_eye.place(x=240, y=175)

        self.btn_login = Button(self.master, text="Login", font=FONT_MD)
        self.btn_login.bind("<Return>", self.login)
        self.btn_login.bind("<Button-1>", self.login)
        self.btn_login.place(x = 10, y = 210, w=250)

        self.lbl_fail_login = Label(self.master, text="", fg="#ff0000", bg=BG, font="Courier 10 bold")
        self.lbl_fail_login.place(x = 10, y = 250, w=250)

        self.lbl_signin = Label(self.master, text="Create an account", cursor="hand2", fg="#2E64FE", bg=BG, font=FONT_SM)
        self.lbl_signin.bind("<Button-1>", self.create_user)
        self.lbl_signin.place(x=0, y=270, w=270)        
        f = font.Font(self.lbl_signin, self.lbl_signin.cget("font"))
        f.configure(underline=True)
        self.lbl_signin.configure(font=f)

        """ Propriedades que precisam ser globais """

        self.frame = Frame()
        self.ent_new_user = Entry()
        self.ent_new_pass = Entry()
        

    def show_password_login(self, event):
        """ Exibe ou oculta a senha na tela de login """
        
        if self.ent_pass_is_showing == False:
            self.img_eye = PhotoImage(file="images/ocultar.png")
            self.btn_eye["image"] = self.img_eye        
            self.ent_pass["show"] = ""
            self.ent_pass_is_showing = True

        else:
            self.img_eye = PhotoImage(file="images/exibir.png")
            self.btn_eye["image"] = self.img_eye        
            self.ent_pass["show"] = "*"
            self.ent_pass_is_showing = False

                         
    def create_user(self, event):
        """ Inicia a interface de criação de novos usuários """

        self.lbl_fail_login["text"] = ""
        
        self.frame = Frame(self.master)
        self.frame.configure(background=BG)
        self.frame.place(x=0, y=0, w=270, h=300)

        lbl_img_create = Label(self.frame, text="Create User", font=FONT_MD, bg=BG)        
        lbl_img_create.place(x=0, y=20, w=270)        

        lbl_user = Label(self.frame, text="Username", bg=BG, fg=FG, font=FONT_SM)
        lbl_user.place(x = 10, y = 100)

        lbl_pass = Label(self.frame, text="Password", bg=BG, fg=FG, font=FONT_SM)
        lbl_pass.place(x = 10, y = 150)

        self.ent_new_user = Entry(self.frame, font=FONT_MD)
        self.ent_new_user.focus()
        self.ent_new_user.place(x = 10, y = 125, w=250)

        self.ent_new_pass = Entry(self.frame, show="*", font=FONT_MD)
        self.ent_new_pass.place(x = 10, y = 175, w=220)

        self.img_eye_create = PhotoImage(file="images/exibir.png")
        self.btn_eye_create = Label(self.frame, image=self.img_eye_create, bg=BG)
        self.btn_eye_create.image=self.img_eye        
        self.btn_eye_create.bind("<Button-1>", self.show_password_create)
        self.btn_eye_create.place(x=240, y=175)        

        btn_cancel = Button(self.frame, text="Cancel", font=FONT_MD)
        btn_cancel["command"] = self.frame.destroy
        btn_cancel.place(x = 10, y = 225, w=120)        

        btn_create = Button(self.frame, text="Create User", font=FONT_MD)
        btn_create.bind("<Return>", self.db_create_user)
        btn_create.bind("<Button-1>", self.db_create_user)
        btn_create.place(x = 140, y = 225, w=120)


    def db_create_user(self, event):
        """ Captura os valores inseridos lançados nas caixas de texto, verifica se contém algum conteúdo
            e os usa como parâmetros para o método create_user do banco de dados. Limpa as caixas de texto.
        """
        
        username = self.ent_new_user.get()
        password = self.ent_new_pass.get()

        if username != "" and password != "":
            success = banco.create_user(username, password)
            self.ent_new_user.delete(0, "end")
            self.ent_new_pass.delete(0, "end")
            self.ent_user.delete(0, "end")
            self.ent_pass.delete(0, "end")
            
            if success:
                self.frame.destroy()


    def show_password_create(self, event):
        """ Exibe ou oculta a senha na tela de criação de usuários """
        
        if self.ent_pass_is_showing == False:
            self.img_eye_create = PhotoImage(file="images/ocultar.png")            
            self.btn_eye_create["image"] = self.img_eye_create        
            self.ent_new_pass["show"] = ""            
            self.ent_pass_is_showing = True

        else:
            self.img_eye_create = PhotoImage(file="images/exibir.png")            
            self.btn_eye_create["image"] = self.img_eye_create                            
            self.ent_new_pass["show"] = "*"            
            self.ent_pass_is_showing = False
            

    def login(self, event):
        """ Captura os valores inseridos lançados nas caixas de texto e os usa como parâmetros
            para o método check_user do banco de dados. Limpa as caixas de texto.
        """
        
        username = self.ent_user.get()
        password = self.ent_pass.get()
        user = banco.check_user(username, password)

        if user:            
            self.create_main_content()
            self.ent_user.delete(0, "end")
            self.ent_pass.delete(0, "end")
            self.lbl_fail_login["text"] = ""
            
        else:
            self.lbl_fail_login["text"] = "Usuário e/ou senha inválidos"
            

    def create_main_content(self):
        """ Exibe o conteúdo da aplicação após o usuário realizar o login """

        content = Frame(self.master, bg="#ffff00")
        content.place(x=0, y=0, w=270, h=300)

        img_python = PhotoImage(file="images/python-img.png")
        lbl_python = Label(content, image=img_python, bg="#ffff00")
        lbl_python.image = img_python
        lbl_python.place(x=0, y=30, w=270)

        lbl_instagram = Label(content, text = "@NoobPythonBR", font=FONT_MD, bg="#ffff00")
        lbl_instagram.place(x=0, y=200, w=270)

        btn_logout = Button(content, text="Logout", font=FONT_SM, bg="#ffff00", fg="#ff0000", cursor="hand2")
        btn_logout["command"] = content.destroy
        btn_logout.place(x=0, y=270, w=270)




# Configurações da janela
root = Tk()
App(root)
#root.iconbitmap("images/python-icon.ico")
root.title("Login | @NoobPythonBR")
root.geometry("270x300+200+200")
root.resizable(False, False)
root.mainloop()
