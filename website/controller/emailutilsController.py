from flask import render_template
from ..service.ProdutoDatabaseService import ProdutoDatabaseService

def gerar_resumo_venda_email_html(venda):
    itens = venda.itens_vendidos
    texto = f"Resumo da sua compra #{venda.id}\n"
    texto += f"Data: {venda.data_venda.strftime('%d/%m/%Y %H:%M')}\n\n"
    texto += "Itens:\n"
    for item in itens:
        produto_nome = item.produto.nome if item.produto else "Produto desconhecido"
        subtotal = item.quantidade * item.preco_unitario
        texto += f"- {produto_nome} | Qtde: {item.quantidade} | Unit: R$ {item.preco_unitario:.2f} | Subtotal: R$ {subtotal:.2f}\n"
    total = sum(item.quantidade * item.preco_unitario for item in itens)
    texto += f"\nTotal da compra: R$ {total:.2f}\n"

    html = f"""
    <html>
    <body>        
        <h2>Resumo da sua compra #{venda.id}</h2>
        <p>Data: {venda.data_venda.strftime('%d/%m/%Y')}</p>
        <p>Obrigada por comprar na Untouched, você só cresce se comprar conosco!</p>        
        <table border="1" cellpadding="5" cellspacing="0">
            <thead>
                <tr><th>Produto</th><th>Quantidade</th><th>Preço Unit.</th><th>Subtotal</th></tr>
            </thead>
            <tbody>
    """
    for item in itens:
        produto_nome = item.produto.nome if item.produto else "Produto desconhecido"
        subtotal = item.quantidade * item.preco_unitario
        html += f"<tr><td>{produto_nome}</td><td>{item.quantidade}</td><td>R$ {item.preco_unitario:.2f}</td><td>R$ {subtotal:.2f}</td></tr>"
    html += f"""
            </tbody>
        </table>
        <p><strong>Total: R$ {total:.2f}</strong></p>
        <p>Em breve nós liberaremos o segredo dos monstros, are you ready?</p>
    </body>
    </html>
    """
    print(texto)
    return texto, html