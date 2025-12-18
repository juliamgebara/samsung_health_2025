import csv
import pandas as pd

def limpeza_dados(arquivo):
    deve_processar = True
    nome_colunas = []
    dados_para_df = [] 

    try:
        with open(arquivo, 'r', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            
            try:
                next(csv_reader) 
            except StopIteration:
                print("Arquivo CSV vazio após a primeira linha de metadado. Abortando.")
                deve_processar = False
                
            if deve_processar:
                try:
                    header_row_with_empty = next(csv_reader)
                    header_with_source = header_row_with_empty[1:] 
                    nome_colunas = header_with_source[1:] 
                    print("Cabeçalho corrigido, pronto para uso no DataFrame.")
                    
                except StopIteration:
                    print("Apenas metadado encontrado, sem cabeçalho e sem dados.")
                    deve_processar = False

            if deve_processar:
                for row in csv_reader:
                    dados_tratados = row[1:-1]
                    dados_para_df.append(dados_tratados)
                    
                print(f"\nColetadas {len(dados_para_df)} linhas de dados.")

        if nome_colunas and dados_para_df:
                # Cria o DataFrame usando os dados coletados e o cabeçalho corrigido
                df_final = pd.DataFrame(dados_para_df, columns=nome_colunas)
                return df_final
        else:
            return pd.DataFrame() # Retorna um DF vazio se não houver dados
            
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return pd.DataFrame()