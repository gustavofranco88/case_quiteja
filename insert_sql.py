import csv
import os
with open('teste.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    linhas_csv = list(leitor_csv)

with open('insert.sql', 'w') as arquivo_sql:
    for linha_csv in linhas_csv:
        tabela = 'nome_da_tabela'
        colunas = 'coluna1, coluna2, coluna3'
        valores = f"'{linha_csv[0]}', '{linha_csv[1]}', '{linha_csv[2]}'"
        instrucao_sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores});\n"
        arquivo_sql.write(instrucao_sql)

'''SELECT DATE(created_at) AS dia, nome_tipo, COUNT(*) AS quantidade
FROM dados_finais
GROUP BY dia, nome_tipo
'''

arquivo_csv.close()
arquivo_sql.close()



