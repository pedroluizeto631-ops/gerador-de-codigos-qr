import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk


# ---------------- FUNÇÕES ----------------

def gerar_qrcode():
    texto = entrada.get()

    if texto.strip() == "":
        messagebox.showwarning(
            "Atenção",
            "Digite um texto ou link para gerar o QR Code."
        )
        return

    # Criando o QR Code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(texto)
    qr.make(fit=True)

    imagem = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Salva temporariamente
    imagem.save("qrcode.png")

    # Mostra na interface
    imagem_tk = Image.open("qrcode.png")
    imagem_tk = imagem_tk.resize((250, 250))

    foto = ImageTk.PhotoImage(imagem_tk)

    label_qrcode.config(image=foto)
    label_qrcode.image = foto


def salvar_qrcode():
    try:
        imagem = Image.open("qrcode.png")

        caminho = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("Imagem PNG", "*.png")
            ]
        )

        if caminho:
            imagem.save(caminho)

            messagebox.showinfo(
                "Sucesso",
                "QR Code salvo com sucesso!"
            )

    except FileNotFoundError:
        messagebox.showwarning(
            "Atenção",
            "Gere um QR Code primeiro."
        )


# ---------------- JANELA ----------------

janela = tk.Tk()

janela.title("Gerador de QR Code")
janela.geometry("450x500")
janela.resizable(False, False)


# ---------------- TÍTULO ----------------

titulo = tk.Label(
    janela,
    text="Gerador de QR Code",
    font=("Arial", 22, "bold")
)

titulo.pack(pady=20)


# ---------------- INSTRUÇÃO ----------------

texto_label = tk.Label(
    janela,
    text="Digite um texto ou link:",
    font=("Arial", 12)
)

texto_label.pack()


# ---------------- ENTRADA ----------------

entrada = tk.Entry(
    janela,
    font=("Arial", 12),
    width=40
)

entrada.pack(pady=10)


# ---------------- BOTÃO GERAR ----------------

botao_gerar = tk.Button(
    janela,
    text="Gerar QR Code",
    font=("Arial", 12),
    command=gerar_qrcode
)

botao_gerar.pack(pady=5)


# ---------------- QR CODE ----------------

label_qrcode = tk.Label(janela)

label_qrcode.pack(pady=15)


# ---------------- BOTÃO SALVAR ----------------

botao_salvar = tk.Button(
    janela,
    text="Salvar QR Code",
    font=("Arial", 12),
    command=salvar_qrcode
)

botao_salvar.pack(pady=5)


# ---------------- EXECUTAR ----------------

janela.mainloop()