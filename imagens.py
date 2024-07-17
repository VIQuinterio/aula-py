from tkinter import Tk, Button, Label
from PIL import ImageTk, Image
import random

# use o comando para instalar a biblioteca ( pip install Pillow )
# Lista de imagens
imagens = [r'C:\Users\professor\Downloads\dog2.jpg',
           'C:/Users/professor/Downloads/dog-eyebrow-2.jpg',
           'C:/Users/professor/Downloads/shiba.png']

# Função para mudar a imagem
def muda_imagem():
    global foto
    imagem_selecionada = random.choice(imagens)
    imagem = Image.open(imagem_selecionada)
    foto = ImageTk.PhotoImage(imagem)
    label.config(image=foto)

# Cria a janela
janela = Tk()

# Cria o botão
botao = Button(janela, text="Mudar imagem", command=muda_imagem)
botao.pack()

# Cria o rótulo da imagem
foto = ImageTk.PhotoImage(Image.open(imagens[0]))  # Imagem inicial
label = Label(janela, image=foto)
label.pack()

# Inicia a janela
janela.mainloop()
