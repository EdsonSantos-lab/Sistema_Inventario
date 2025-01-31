from tkinter import*
from tkinter import Tk,StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from view import*
from tkinter import messagebox
from tkinter import filedialog as fd


# criar janela
janela = Tk()
janela.title('Edson Santos')
janela.geometry('900x600')
janela.configure(background='#e9edf5')
janela.resizable(width=FALSE, height=FALSE)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#  criando frames

frame_cima = Frame(janela, width=1043, height= 50, bg='#F8F8F2', relief=FLAT)
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=1043, height= 303, bg='#F8F8F2',pady=20, relief=FLAT)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1043, height= 300, bg='#F8F8F2', relief=FLAT)
frame_baixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# criando funcoes
global tree

# enseri
def enseri():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_local.get()
    descrisao = e_descrisao.get()
    modelo = e_modelo.get()
    data = e_calen.get()
    valor = e_valor.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_enseri = [nome, local, descrisao, modelo, data, valor, serie, imagem]

    for i in lista_enseri:
        if i =='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    inseri_form(lista_enseri) 
    
    messagebox.showinfo('Susseso', 'Os dados foram enseridos com susseso') 

    e_nome.delete(0,'end')
    e_local.delete(0,'end')
    e_descrisao.delete(0,'end')
    e_modelo.delete(0,'end')
    e_calen.delete(0,'end')
    e_valor.delete(0,'end')
    e_serie.delete(0,'end')

    

    mostrar()

# funcao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        ver_info = tree.focus()
        ver_dic = tree.item(ver_info)
        ver_lista = ver_dic['values']

        


        id = int(ver_lista[0])
        e_nome.insert(0,ver_lista[1])
        e_local.insert(0,ver_lista[2])
        e_descrisao.insert(0,ver_lista[3])
        e_modelo.insert(0,ver_lista[4])
        e_calen.insert(0,ver_lista[5])
        e_valor.insert(0,ver_lista[6])
        e_serie.insert(0,ver_lista[7])
        imagem_string= ver_lista[8]

        def up_date():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descrisao = e_descrisao.get()
            modelo = e_modelo.get()
            data = e_calen.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string

            if imagem =='':
                imagem= e_serie.insert(0,ver_lista[7])

            lista_atualizar = [nome, local, descrisao, modelo, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i =='':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return
            
            atualizar_(lista_atualizar)
            messagebox.showinfo('Susseso', 'Os dados foram atualizados com susseso')

            e_nome.delete(0,'end')
            e_local.delete(0,'end')
            e_descrisao.delete(0,'end')
            e_modelo.delete(0,'end')
            e_calen.delete(0,'end')
            e_valor.delete(0,'end')
            e_serie.delete(0,'end')

            b_update.destroy()

            mostrar()

        b_update = Button(frame_meio,command= up_date, width=13, text='Confirmar'.upper(), overrelief=RIDGE, font='Ivy 8 bold', bg='#DCDAD5', fg='#18E767')
        b_update.place(x=330, y=185)

    except IndexError:
            messagebox.showerror('Erro', 'selecione uma linha')
        
# funcao deletar
def deletar():

    try:
        ver_info = tree.focus()
        ver_dic = tree.item(ver_info)
        ver_lista = ver_dic['values']   

        valor = ver_lista[0]

        delete_dado([valor])

        mostrar()

        messagebox.showinfo('boa', 'campo deletado..')

    except IndexError:
            messagebox.showerror('Erro', 'selecione uma linha..')
        
# funcao para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()   
    imagem_string = imagem

    # abrir image
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)
    
    l_imagem = Label(frame_meio, image=imagem, bg='#e9edf5',fg='#192422')
    l_imagem.place(x=700, y=10)

# funcao ver iten
def ver_imagem():
    global imagem, imagem_string, l_imagem

    ver_info = tree.focus()
    ver_dic = tree.item(ver_info)
    ver_lista = ver_dic['values']

    valor = [int(ver_lista[0])]

    iten_= ver_form_1a(valor)

    imagem = iten_[0][8]

    # abrir image
    imagem = Image.open(imagem)
    imagem= imagem.resize((170, 170))
    imagem= ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_meio,image=imagem, bg='#e9edf5',fg='#192422')
    l_imagem.place(x=700, y=10)






# trabalhando no freme cima____________________________________________________________

# abrir image
imagem1 = Image.open('iventario.png')
imagem1= imagem1.resize((45, 45))
imagem1= ImageTk.PhotoImage(imagem1)

logo = Label(frame_cima,image=imagem1, text=' Inventário Doméstico', width=900,compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg='#e9edf5',fg='#192422')
logo.place(x=0, y=0)

# crindo entradas 
l_nome = Label(frame_meio, text= 'Nome', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130,y=11)

l_local = Label(frame_meio, text= 'Sala/Área', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_local.place(x=10, y=40)
e_local = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_local.place(x=130,y=41)

l_descrisao = Label(frame_meio, text= 'Descrisão', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_descrisao.place(x=10, y=70)
e_descrisao = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_descrisao.place(x=130,y=71)

l_modelo = Label(frame_meio, text= 'Marca', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_modelo.place(x=10, y=100)
e_modelo = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_modelo.place(x=130,y=101)

l_calen = Label(frame_meio, text= 'Data da Compra', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_calen.place(x=10, y=130)
e_calen = DateEntry(frame_meio, width=12, Background='darkblue', bordewidth=2, year=2025)
e_calen.place(x=130,y=131)

l_valor = Label(frame_meio, text= 'Valor da Compra', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_valor.place(x=10, y=160)
e_valor = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130,y=161)

l_serie = Label(frame_meio, text= 'Serie', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_serie.place(x=10, y=190)
e_serie = Entry(frame_meio, width=30, justify='left', relief=SOLID)
e_serie.place(x=130,y=191)

# criando botoes
l_carregar = Label(frame_meio, text= 'Imagem do Iten', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_carregar.place(x=10, y=220)
b_carregar = Button(frame_meio, width=30,command=escolher_imagem, text='Carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font='Ivy 8', bg='#DCDAD5', fg='#0096EE')
b_carregar.place(x=130, y=221)

# botao enseri
imagem_aad = Image.open('adicionar.png')
imagem_aad = imagem_aad.resize((20, 20))
imagem_aad = ImageTk.PhotoImage(imagem_aad)

b_enseri = Button(frame_meio,command=enseri, image=imagem_aad, width=95, text='  Adicinar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg='#DCDAD5', fg='#0096EE')
b_enseri.place(x=330, y=10)

# botao atualizar
imagem_at = Image.open('atual.png')
imagem_at = imagem_at.resize((20, 20))
imagem_at = ImageTk.PhotoImage(imagem_at)

b_at = Button(frame_meio,command= atualizar, image=imagem_at, width=95, text='  Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg='#DCDAD5', fg='#0096EE')
b_at.place(x=330, y=50)

# botao deletar
imagem_del = Image.open('delete.png')
imagem_del = imagem_del.resize((20, 20))
imagem_del = ImageTk.PhotoImage(imagem_del)

b_del = Button(frame_meio,command=deletar, image=imagem_del, width=95, text='  Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg='#DCDAD5', fg='#0096EE')
b_del.place(x=330, y=90)

# botao ver imagem
imagem_ver = Image.open('pasta.png')
imagem_ver = imagem_ver.resize((20, 20))
imagem_ver = ImageTk.PhotoImage(imagem_ver)

b_ver = Button(frame_meio,command=ver_imagem, image=imagem_ver, width=95, text='  Ver Imagem'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font='Ivy 8', bg='#DCDAD5', fg='#0096EE')
b_ver.place(x=330, y=221)

# label quantidade total e valores 
l_total = Label(frame_meio,width=14, text= '', height=2, anchor=CENTER, font='Ivy 17 bold', bg='#0096EE', fg='#F8F8F2')
l_total.place(x=450, y=17)
l_total_2 = Label(frame_meio, text= '  Valor total de todos os itens   ', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_total_2.place(x=450, y=12)


l_qt = Label(frame_meio,width=14, text= '', height=2,pady=5, anchor=CENTER, font='Ivy 17 bold', bg='#0096EE', fg='#F8F8F2')
l_qt.place(x=450, y=90)
l_qt_2 = Label(frame_meio, text= '  Quantidade total de itens   ', height=1, anchor=NW, font='Ivy 10 bold', bg='#0096EE', fg='#F8F8F2')
l_qt_2.place(x=450, y=92)

# tabela
def mostrar():

    global tree

    # Definindo os cabeçalhos
    tabela_head = ['#Item', 'Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo', 'Data da compra', 'Valor da compra', 'Número de série']

    lista_itens = ver_form()

    

    # Configurando Treeview
    tree = ttk.Treeview(
        frame_baixo, 
        selectmode="extended",
        columns=tabela_head, 
        show="headings"
    )

    # Scrollbars
    vsb = ttk.Scrollbar(frame_baixo, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_baixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Posicionando Treeview e Scrollbars
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_baixo.grid_rowconfigure(0, weight=12)

    # Configuração das colunas
    hd = ["center"] * len(tabela_head)
    h = [40, 150, 100, 160, 130, 100, 100, 100]

    for n, col in enumerate(tabela_head):
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        # Inserindo itens na tabela
        for item in lista_itens:
            tree.insert('', 'end', values=item)

        # Calculando totais
        quantidade = [iten[6] for iten in lista_itens]
        Total_valor = sum(quantidade)
        Total_itens = len(quantidade)

        # Atualizando Labels
        l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
        l_qt['text'] = Total_itens

   

mostrar()


janela.mainloop()

