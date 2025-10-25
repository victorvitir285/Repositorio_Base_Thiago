# Psso 1 - Importar o SQLite
import sqlite3 # não pecisa instalar

# Passo 2 - Criar um banco de dados
conexao = sqlite3.connect('cofre.db')

# Passo 3 - Criar um cursor (pra executar comando SQL)
cursor = conexao.cursor()

# Passso 4 - Criar um TABLE dentro do banco de dados 
cursor.execute('''

CREATE TABLE IF NOT EXISTS segredo (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   nome TEXT NOT NULL,
   dono TEXT NOT NULL,
   valor DECIMAL NOT NULL                                 
);

               ''')

conexao.commit()
conexao.close()

print('Tabela criada com sucesso!')

# Passo 5 - Inserir dados dentro da tabela que está dentro do banco de dados
conexao = sqlite3.connect('cofre.db')
cursor = conexao.cursor()
'''
cursor.execute("INSERT INTO segredo('nome','dono','valor') VALUES (?,?,?);", ('CARRO','MATHEUS',50000))
cursor.execute("INSERT INTO segredo('nome','dono','valor') VALUES (?,?,?);", ('CROCS','VARESA',800))
cursor.execute("INSERT INTO segredo('nome','dono','valor') VALUES (?,?,?);", ('CASA','NANDO',72000))
cursor.execute("INSERT INTO segredo('nome','dono','valor') VALUES (?,?,?);", ('BRINCO','MARIA',1900))
conexao.commit()
conexao.close()
'''
# Passo 6 - Ler, consultar os dados cadastrados
ler = cursor.execute("select * from segredo;")

for dados in ler.fetchall():
    print(dados)

# Passo 7 - Atualizar um dado cadastrado
# Passo 8 - Apagar um registro da tabela