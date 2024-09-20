# escrever essas coisas no terminal
# pip install pyautogui
# pip install pillow
import pyautogui
import time


def main():
    print('\n mouse começou a se mover \n')
    time.sleep(1)  # Pausa a execução por 2 segundos
    # Mover o cursor para a posição (100, 200)
    pyautogui.moveTo(250, 800)

    pyautogui.moveRel(50, -50)

    pyautogui.click(clicks=2)  # Clica duas vezes

    pyautogui.write('elaine.py')
    pyautogui.press('enter')

    pyautogui.moveRel(600, -500)

    pyautogui.press('enter')

    pyautogui.write('import \n tkinter as tk')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('from tkinter import ttk')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('janela = tk.Tk()')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('janela.title("TE AMO MAMAE")')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write(
        'label = ttk.Label(janela, text="   EU TE AMO MAEZINHA   ")')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('label.grid(column=0, row=0)')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('janela.geometry("400x400")')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('age=40')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write(
        'print(f" \\n Eu sou a Elaine e tenho -> {age} anos de idade. \\n")'
    )

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('janela.mainloop()')

    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.write('# fim do codigo')
    pyautogui.press('enter')
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('ctrl', 'shift', "'")
    # nao sei
    time.sleep(1)
    pyautogui.write('python elaine.py')
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.hotkey('alt', 'f4')

    time.sleep(1)
    pyautogui.write('rm elaine.py')
    pyautogui.press('enter')
    pyautogui.press('enter')

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'p')
    pyautogui.press('backspace')
    pyautogui.write('mouse')
    pyautogui.press('enter')
    print('fim do programa')


# Executa a função principal
if __name__ == '__main__':
    main()
