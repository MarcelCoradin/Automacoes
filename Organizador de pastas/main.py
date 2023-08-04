import os
from tkinter.filedialog import askdirectory # apartir desta biblioteca importa para mim esta função

caminho = askdirectory(title='Selecione uma pasta')

lista_de_arquivos = os.listdir(caminho)

locais = {
    "imagens": ['.png', '.jpg'],
    "zip":['.zip', '.rar' ],
    "executaveis": ['.exe'],
    "PDF": ['.pdf'],
    "Documentos": ['.docx']   
}

for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')