carrinho = []
carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))

carrinho = sum([valor for produto, valor in carrinho])

print(carrinho)