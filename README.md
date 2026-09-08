# 📱 Gerador de QR Code

<p align="center">
  <strong>Um gerador de QR Codes simples, rápido e intuitivo desenvolvido em Python.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge" alt="Status">
</p>

---

# 📌 Sobre o projeto

O **Gerador de QR Code** é uma aplicação desenvolvida em **Python** que permite transformar textos, links e outras informações em QR Codes de maneira rápida e prática.

O projeto possui uma interface gráfica criada com **Tkinter**, permitindo que o usuário gere, visualize e salve seus QR Codes sem precisar utilizar o terminal.

---

# ✨ Funcionalidades

* 🔗 Gerar QR Code a partir de **links**
* 📝 Gerar QR Code a partir de **textos**
* 🖥️ Interface gráfica com **Tkinter**
* 👀 Visualização do QR Code na própria aplicação
* 💾 Salvar QR Code como imagem `.png`
* ⚠️ Validação de campos vazios
* 🚀 Interface simples e fácil de utilizar

---

# 🛠️ Tecnologias utilizadas

|    Tecnologia   | Função                             |
| :-------------: | ---------------------------------- |
|  🐍 **Python**  | Linguagem principal                |
| 🖥️ **Tkinter** | Criação da interface gráfica       |
|  📦 **qrcode**  | Geração dos QR Codes               |
|  🖼️ **Pillow** | Manipulação e exibição das imagens |

---

# 📋 Requisitos

Antes de começar, certifique-se de possuir:

* **Python 3.x**
* **pip**
* Um computador com Windows, Linux ou macOS

Para verificar a versão do Python:

```bash
python --version
```

Se estiver utilizando Linux ou macOS, pode ser necessário:

```bash
python3 --version
```

---

# 📥 Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/pedroluizeto631-ops/gerador-de-codigos-qr.git
```

Depois entre na pasta:

```bash
cd gerador-de-qrcode
```

---

## 2. Instale as dependências

Execute no terminal:

```bash
pip install qrcode pillow
```

No Linux ou macOS:

```bash
pip3 install qrcode pillow
```

---

# ▶️ Executando o projeto

Depois de instalar todas as dependências, execute:

```bash
python gerador_qrcode.py
```

Ou, dependendo do sistema:

```bash
python3 gerador_qrcode.py
```

A janela do aplicativo será aberta automaticamente. 🚀

---

# 🖥️ Como utilizar

## 1. Digite o conteúdo

No campo de texto, coloque o conteúdo que deseja transformar em QR Code.

### Exemplo:

```text
https://www.google.com
```

Também é possível utilizar um texto:

```text
Olá! Este é meu QR Code.
```

---

## 2. Clique em **Gerar QR Code**

Depois de inserir o conteúdo, clique no botão:

> **Gerar QR Code**

O programa irá criar o QR Code automaticamente e exibi-lo na tela.

---

## 3. Salve o QR Code

Depois de gerar o código, clique em:

> **Salvar QR Code**

Escolha o local onde deseja salvar a imagem.

O arquivo será salvo no formato:

```text
.png
```

---

# 🔄 Funcionamento

O funcionamento básico da aplicação pode ser representado da seguinte forma:

```text
       📝 Usuário
           │
           ▼
    Digita um texto/link
           │
           ▼
     📦 Biblioteca qrcode
           │
           ▼
       🔳 QR Code
           │
           ▼
     🖥️ Tkinter
           │
           ▼
      👀 Visualização
           │
           ▼
        💾 PNG
```

---

# 📂 Estrutura do projeto

```text
gerador-qrcode/
│
├── 📄 gerador_qrcode.py
├── 🖼️ qrcode.png
└── 📖 README.md
```

### `gerador_qrcode.py`

Arquivo principal responsável pelo funcionamento da aplicação.

### `qrcode.png`

Imagem gerada pelo programa.

### `README.md`

Documentação do projeto.

---

# 🧠 Conceitos praticados

Este projeto foi desenvolvido para praticar conceitos importantes de Python, como:

* 🐍 Funções
* 📦 Importação de bibliotecas
* 🖥️ Interfaces gráficas
* 🎯 Eventos e comandos do Tkinter
* 📁 Manipulação de arquivos
* 🖼️ Manipulação de imagens
* ⚠️ Tratamento de erros
* 📚 Utilização de bibliotecas externas

---

# 🔮 Melhorias futuras

O projeto pode ser expandido com diversas funcionalidades:

* 🎨 Personalização das cores
* 📐 Controle do tamanho do QR Code
* 🌙 Modo escuro
* 📋 Botão para copiar o conteúdo
* 🕘 Histórico de QR Codes
* 📶 Gerador de QR Code para Wi-Fi
* 📧 QR Code para e-mail
* 📞 QR Code para telefone
* 🖼️ Adicionar logotipo ao QR Code
* 🗂️ Escolher diferentes formatos de exportação
* ✨ Interface mais moderna

---

# 🎯 Objetivo

O principal objetivo deste projeto é colocar em prática conhecimentos de **Python e desenvolvimento de interfaces gráficas**, criando uma aplicação funcional e fácil de utilizar.

Apesar de ser um projeto simples, ele serve como base para aplicações maiores e mais completas.

---

# ⭐ Contribuição

Contribuições, sugestões e melhorias são bem-vindas!

Se você encontrou algum problema ou tem uma ideia para melhorar o projeto, fique à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

---

# 📄 Licença

Este projeto foi desenvolvido para fins de **estudo e aprendizado**.

---

<p align="center">
  Desenvolvido com 🐍 Python e ☕ dedicação
</p>

<p align="center">
  ⭐ Se este projeto foi útil para você, considere deixar uma estrela!
</p>
