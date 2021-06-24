from PySimpleGUI import PySimpleGUI as sg



def login():
    sg.theme('DarkBlue15')
    layout = [
        [sg.Text('Nome:'),sg.Input(key='nome')],
        [sg.Text('Senha'),sg.Input(key = 'senha',password_char='*')],
        [sg.Button('Entrar')],
        [sg.Button('Cadastrar usuário')]
    ]
    return sg.Window('Login',layout = layout,finalize=True)
def Erro():
    sg.theme("DarkBLue15")
    layout = [
        [sg.Text("Usuário ou senha incorreto")],
        [sg.Button('Voltar')]
    ]

    return sg.Window('Error', layout=layout, finalize=True)

def eiv():
    sg.theme("DarkBLue15")
    layout = [
        [sg.Text("Valor mensal das parcelas superior ao pemitido")],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Empréstimo inválido', layout=layout, finalize=True)

def ev():
    sg.theme("DarkBLue15")
    layout = [
        [sg.Text("Empréstimo aceito ao usuário")],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Empréstimo válido', layout=layout, finalize=True)


def Cadastro():
    sg.theme('DarkBlue15')
    layout = [
        [sg.Text('Nome: '), sg.Input(key='user')],
        [sg.Text('Senha:'), sg.Input(key='pass')],
        [sg.Text('CPF: '),sg.Input(key='cpf')],
        [sg.Text('Renda Mensal: '), sg.Input(key='rm')],
        [sg.Button('Cadastrar')],
        [sg.Button('Voltar')]
   ]


    return sg.Window('Cadastro', layout=layout, finalize=True)

def Emprestimo():
    sg.theme('DarkBlue15')
    layout = [
        [sg.Text('Valor do empréstimo: '), sg.Input(key='emp')],
        [sg.Text('Número de mensalidades: '), sg.Input(key='nm')],
        [sg.Button('Validar')],
        [sg.Button('Ficha do usuário')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Emprestimo', layout=layout, finalize=True)

def Ficha():
    sg.theme('DarkBlue15')
    layout = [
        [sg.Print("Nome:",x)],
        [sg.Print("CPF:", z)],
        [sg.Print("Renda Mensal:", x1)],
        [sg.Button("Voltar")]

    ]

    return sg.Window('Ficha', layout=layout, finalize=True)

janela1,janela2,janela3 = login(),None,None

while True:
        window,event,values = sg.read_all_windows()

        if window == janela1 and event == sg.WIN_CLOSED:
            break
        if window == janela2 and event == sg.WIN_CLOSED:

            break




        if window == janela1 and event == 'Entrar':

            if values['nome'] == x and values['senha'] == y:

                janela2 = Emprestimo()
                janela1.hide()

            else:
                janela2 = Erro()
                janela1.hide()


        if window == janela1 and event == 'Cadastrar usuário':

            janela2 = Cadastro()
            janela1.hide()

        if window == janela2 and event == 'Cadastrar':
            x = values['user']
            y = values['pass']
            z = values['cpf']
            x1 = values['rm']

        if window == janela2 and event == 'Validar':
            if (int(values['emp'])/int(values['nm']))/int(x1) > 0.3:
                janela3 = eiv()

            else:
                janela3 = ev()

        if window == janela2 and event == 'Ficha do usuário':

            janela3 = Ficha()

        if window == janela2 and event == "Voltar":
            janela2.hide()
            janela1.un_hide()

        if window == janela3 and event == "Voltar":
            janela3.hide()




