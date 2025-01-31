import sqlite3 as lite

# conecxão
conexão = lite.connect('dadosfinal.bd')

# montar tabela
def inseri_form(i):
    #i dados = ['vaso', 'sala de estar', 'vaso que eu comprei no mercado ao lado', 'marca x', '26/01/2025', '100', 'xxx', 'C:Imagem']
    with conexão:
        cursor = conexão.cursor()
        quiry = "INSERT INTO inventario(nome, local, descrisao, marca, data_da_compra, valor_da_compra, serie, imagem)VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(quiry, i)
# atualizar dados
def atualizar_(i):
    # i atualizar_dados = ['vas', 'sala de estar', 'vaso que eu comprei no mercado ao lado', 'marca x', '26/01/2025', '100', 'xxx', 'C:Imagem', 1]
    with conexão:
        cursor = conexão.cursor()
        quiry = "UPDATE inventario SET nome=?, local=?, descrisao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cursor.execute(quiry, i)
# deletar dados
def delete_dado(i):
    #i deletar_dados = str(1)
    with conexão:
        cursor = conexão.cursor()
        quiry = "DELETE FROM inventario WHERE id=?"
        cursor.execute(quiry, i)
# ver dados todos
def ver_form():
    ver_dados = []
    with conexão:
        cursor = conexão.cursor()
        quiry = "SELECT * FROM inventario"
        cursor.execute(quiry)

        linhas = cursor.fetchall()
        for linha in linhas:
            ver_dados.append(linha)
    return ver_dados    
# ver dados de um
def ver_form_1a(id):
    ver_dados_individuais = []
    with conexão:
        cursor = conexão.cursor()
        quiry = "SELECT * FROM inventario WHERE id=?"
        cursor.execute(quiry, id)

        linhas = cursor.fetchall()
        for linha in linhas:
            ver_dados_individuais.append(linha)

    return ver_dados_individuais
    