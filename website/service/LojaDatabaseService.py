from .. import db
from ..model.Loja import Loja # Importar o modelo Loja

class LojaDatabaseService:
    @staticmethod
    def adicionar_loja(endereco, cnpj, latitude, longitude, nome):
        """
        Adiciona uma nova loja ao banco de dados.
        Retorna o objeto Loja criado em caso de sucesso, ou None em caso de erro.
        """
        try:
            nova_loja = Loja(
                endereco=endereco,
                cnpj=cnpj,
                latitude=latitude,
                longitude=longitude,
                nome=nome
            )
            db.session.add(nova_loja)
            db.session.commit()
            return nova_loja
        except Exception as e:
            db.session.rollback() # Desfaz a operação em caso de erro
            print(f"Erro ao adicionar loja: {e}") # Loga o erro para depuração
            return None

    @staticmethod
    def listar_lojas():
        """
        Lista todas as lojas cadastradas no banco de dados.
        Retorna uma lista de objetos Loja.
        """
        return Loja.query.all()

    @staticmethod
    def excluir_loja(loja_id):
        """
        Exclui uma loja do banco de dados pelo seu ID.
        Retorna True se a loja foi excluída com sucesso, False caso contrário (loja não encontrada ou erro).
        """
        loja = Loja.query.get(loja_id)
        if loja:
            try:
                db.session.delete(loja)
                db.session.commit()
                return True
            except Exception as e:
                db.session.rollback() # Desfaz a operação em caso de erro
                print(f"Erro ao excluir loja: {e}") # Loga o erro para depuração
                return False
        return False # Retorna False se a loja não for encontrada