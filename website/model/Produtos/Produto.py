from ... import db

class Produto(db.Model):
    __tablename__ = 'produto'  

    id = db.Column(db.Integer, primary_key=True)  
    nome = db.Column(db.String(50))  
    descricao = db.Column(db.Text(150)) 
    preco = db.Column(db.Numeric(10, 2))  
    codigo_de_barras = db.Column(db.String(50), unique=True)  
    imagem_url = db.Column(db.String(200))  
    categoria = db.Column(db.String(25))  

    
    estoque = db.relationship('Estoque', uselist=False, cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_on': categoria,
        'polymorphic_identity': 0  
    }
    
    def gerar_relatorio(self):
        relatorio = f"Produto: {self.nome}\nPreço: R${self.preco}\n"
        return relatorio