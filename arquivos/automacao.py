import PyPDF2   # Biblioteca Python.
import os       # Biblioteca 'os' manipular arquivos.

merger = PyPDF2.PdfMerger() # merger " mesclar pdf".

lista_arquivos = os.listdir("arquivos")  # 'os.listdir' vai listar o que tem dentro de uma pasta.
lista_arquivos.sort() # '.sort' ordena a lista ex: organiza os pdfs em ordem 1, 2, 3...
print(lista_arquivos)

for arquivo in lista_arquivos:   # 'para cada arquivo dentro da minha lista de arquivos.'
    if ".pdf" in arquivo:        # Verifica se .pdf esta dentro do nome do arquivo.
        merger.append(f'arquivos/{arquivo}') # .append " adiciona"
merger.write("PDF final.pdf")    #'.write' Salve o pdf