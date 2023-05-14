from zipfile import ZipFile
import csv

'''
with ZipFile('dados.zip', 'r') as zip:
    zip.extractall()
'''
with open('origem-dados.csv', 'r') as origem,\
     open('tipos.csv', 'r') as tipos,\
     open('teste.csv', 'w', newline='') as teste:

    reader = csv.reader(origem, delimiter=',')
    sorted_reader = sorted(reader, key=lambda row: row[0])
    reader_tipos = csv.reader(tipos, delimiter=',')
    new_csv = csv.writer(teste, delimiter=',')
    new_csv.writerow(
        ['created_at','product_code','customer_code','status','tipo','nome_tipo']
    )

    for row in sorted_reader:
        if row[3] == 'CRITICO':
            print(row)
            new_csv.writerow(row)
# abre o arquivo insert-dados.sql em modo de escrita
with open('insert-dados.sql', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    # gera o SQL para inserir os dados na tabela dados_finais
    for dado in new_csv:
        writer.writerow([
            "INSERT INTO dados_finais (id, tipo_id, status, created_at, nome_tipo) VALUES",
            f"({dado['id']},"
            f" {dado['tipo_id']},"
            f" '{dado['status']}',"
            f" '{dado['created_at']}',"
            f" '{dado['nome_tipo']}');"
        ])
