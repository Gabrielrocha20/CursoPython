import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.con = sqlite3.connect(arquivo)
        self.cursor = self.con.cursor()

    def inserir(self, nome, telefone):
        try:
            inserir = f'INSERT INTO agenda  (nome, telefone) VALUES (?, ?)'
            self.cursor.execute(inserir, (nome, telefone))
            self.con.commit()
        except Exception as e:
            print('Nome invalido')

    def editar(self, nome, telefone, id):
        update = f'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(update, (nome, telefone, id))
        self.con.commit()

    def excluir(self, id):
        excluir = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(excluir, (id,))
        self.con.commit()

    def listar(self):
        listar = 'SELECT * FROM agenda'
        self.cursor.execute(listar)
        for linha in self.cursor.fetchall():
            identificador, nome, telefone = linha
            print(identificador, nome, telefone)

    def buscar(self, valor):
        busca = f'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(busca, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(id, nome, telefone)

    def fechar(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.buscar('19')



