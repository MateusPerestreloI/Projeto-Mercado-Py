from models.produto import Produto

celular: Produto = Produto(nome='Iphone 9',preco=10639.99)
ps4: Produto = Produto(nome='Playstation 4', preco=1999.99)

print(celular)
print(ps4)