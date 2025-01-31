# começo
import sqlite3 as lite

# conecxão
conexão = lite.connect('dadosfinal.bd')

# criar tabela
with conexão:
    cursor = conexão.cursor()
    cursor.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descrisao TEXT, marca TEXT, data_da_compra, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")