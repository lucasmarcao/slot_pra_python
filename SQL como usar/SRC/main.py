# import mySQL
# import minhasFuncoes
import GUI

# vars
interfaceGrafica = GUI
# marcaoSQL = mySQL


def main() -> bool:
    #  python -m auto_py_to_exe
    # inicio
    try:
        # inserirNaTabelaPrisioneiro()
        # selecionarBD()
        # print("\n Funcionou. minhasFuncoes.minha_funcao: ",
        #       minhasFuncoes.minha_funcao(56))

        # marcaoSQL.verificaSeFuncionaMySQL()
        interfaceGrafica.loginGUI()
    except Exception as error:
        print(f"\n não deu certo porque | {error} | . \n")

    # fim
    return True


main()
