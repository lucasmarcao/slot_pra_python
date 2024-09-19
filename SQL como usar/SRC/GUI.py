import customtkinter

# var inicial
# unico jeito de fazer um contador
cont = 0


def gete(oiInt, tchauInt) -> None:
    texto_email = email.get()
    numero_senha = 1
    print("\n ", oiInt, tchauInt)
    try:
        numero_senha = int(senha.get())
    except Exception as e:
        print(f"""\n erro: \n {e}
        user escreveu '{senha.get()}' em vez de numero.""")
        numero_senha = 0

    print("\n texto_email -> ", texto_email)
    print(" numero_senha -> ", numero_senha)


def abrir_janelinha():
    # existe 2 jeito nonlocal || global
    global cont
    # Informar que cont é do escopo envolvente
    cont = cont + 1
    # Criar a nova janela
    janelinha = customtkinter.CTkToplevel()
    janelinha.title("Minha Janelinha")

    # Defina as dimensões da janela
    largura_janelinha = 400
    altura_janelinha = 200

    # Obtenha as dimensões da tela
    largura_tela = janelinha.winfo_screenwidth()
    altura_tela = janelinha.winfo_screenheight()

    # Calcule a posição central
    pos_x = (largura_tela // 2) - (largura_janelinha // 4)
    pos_y = (altura_tela // 2) - (altura_janelinha // 2)

    # Posicione a janela no centro da tela
    janelinha.geometry(f"""{
        largura_janelinha
    }x{
        altura_janelinha
    }+{
        pos_x
    }+{
        pos_y
    }""")

    janelinha.grab_set()  # faz o pc focar na janelinha
    # Adicionar widgets à nova janela
    texto = customtkinter.CTkLabel(
        janelinha, text=f"tu já abriu isso | {cont} | vezes")
    texto.pack(padx=20, pady=20)

    botao_fechar = customtkinter.CTkButton(
        janelinha, text="Fechar", command=janelinha.destroy)
    botao_fechar.pack(padx=20, pady=20)

    return cont


def loginGUI():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    janela = customtkinter.CTk()

    texto = customtkinter.CTkLabel(
        janela,
        text="Fazer login"
    )

    global email
    email = customtkinter.CTkEntry(
        janela,
        placeholder_text="email"
    )

    global senha
    senha = customtkinter.CTkEntry(
        janela,
        placeholder_text="senha",
        show="*"
    )

    # Pega o texto do input 'email' e o armazena como string
    botao = customtkinter.CTkButton(
        janela,
        text_color="#FCDC94",
        fg_color="#78ABA8",
        text="LOGIN",
        # não pode fechar a funcao com clique()
        command=lambda: gete(6, 5))

    botao2 = customtkinter.CTkButton(
        janela,
        text="clicou",
        # não pode fechar a funcao com clique()
        command=abrir_janelinha)

    # css
    texto.pack(padx=10, pady=10)
    email.pack(padx=10, pady=10)
    senha.pack(padx=10, pady=10)
    botao.pack(padx=10, pady=10)
    botao2.pack(padx=10, pady=10)

    # finalzin
    janela.title(" Marcão reina chad. ")

    # Defina as dimensões da janela
    largura_janela = 500
    altura_janela = 300

    # Obtenha as dimensões da tela
    largura_telaJanela = janela.winfo_screenwidth()
    altura_telaJanela = janela.winfo_screenheight()

    # Calcule a posição central
    pos_xJanela = (largura_telaJanela // 2) - (largura_janela // 4)
    pos_yJanela = (altura_telaJanela // 2) - (altura_janela // 2)

    # Posicione a janela no centro da tela
    janela.geometry(f"""{
        largura_janela
    }x{
        altura_janela
    }+{
        pos_xJanela
    }+{
        pos_yJanela
    }""")

    janela.mainloop()
    print("O programa finalizou")
