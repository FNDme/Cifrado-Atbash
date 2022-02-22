from tkinter import messagebox, Tk, Canvas, Text, Button, Label, Entry, END, DISABLED, NORMAL
from Atbash import encrypt

base = Tk()

base.title('Atbash Cipher')
base.resizable(False, False)
base.geometry('500x400')
base.configure(background='#232426')


Canva = Canvas(base, width=500, height=65, bg='#2a2b2d', highlightthickness=0)
Canva.place(x=0, y=335)


def gui_encrypt():
    encrypted = encrypt(inputText.get('1.0', END))

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.insert(END, encrypted)
    outputText.config(state=DISABLED)

    return


def clear():
    inputText.delete('1.0', END)

    outputText.config(state=NORMAL)
    outputText.delete('1.0', END)
    outputText.config(state=DISABLED)


inputTextLabel = Label(base, text='Input Text')
inputTextLabel.place(x=30, y=30)
inputTextLabel.configure(background='#232426', foreground='#F2F2F2')

outputTextLabel = Label(base, text='Output Text')
outputTextLabel.place(x=30, y=170)
outputTextLabel.configure(background='#232426', foreground='#BFBFBD')

inputText = Text(base, width=50, height=5)
inputText.place(x=20, y=60)
inputText.configure(background='#04BF68', foreground='#232426', borderwidth=0)

outputText = Text(base, width=50, height=5)
outputText.place(x=20, y=200)
outputText.config(state=DISABLED, bg='#155939', fg='#BFBFBF', borderwidth=0)

Encrypt = Button(base, text='Convert', command=lambda: gui_encrypt())
Encrypt.place(x=30, y=355)
Encrypt.configure(background='#04BF68', foreground='#155939',
                  borderwidth=0, activebackground='#232426', pady=5, padx=10)

Clear = Button(base, text='Clear', command=lambda: clear())
Clear.place(x=410, y=355)
Clear.configure(background='#04BF68', foreground='#155939',
                borderwidth=0, activebackground='#232426', pady=5, padx=10)


base.mainloop()
