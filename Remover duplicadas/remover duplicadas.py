import pandas as pd

# Carregar o arquivo Excel em um DataFrame do pandas
file_path = 'C:/Users/marce/OneDrive/Área de Trabalho/Alteração n4 da jouse ltda/gatsdasdasd.xlsx'
df = pd.read_excel(file_path)

# Remover duplicatas e atualizar o DataFrame
df_no_duplicates = df.drop_duplicates()

# Salvar o DataFrame sem duplicatas de volta para um arquivo Excel
output_file_path = 'C:/Users/marce/OneDrive/Área de Trabalho/Alteração n4 da jouse ltda/g.xlsx'
df_no_duplicates.to_excel(output_file_path, index=False)

print("Duplicatas removidas e arquivo salvo sem duplicatas.")
