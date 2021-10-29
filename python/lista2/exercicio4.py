precoProduto = float(input("Coloque o preco do produto: "))

def calculadoraAumentoPreco(precoProduto):
    if precoProduto <= 50:
        precoProduto = precoProduto + precoProduto*0.05
    elif 100>=precoProduto>50:
        precoProduto = precoProduto + precoProduto*0.10
    elif precoProduto>100:
        precoProduto = precoProduto + precoProduto*0.15
    
    print(precoProduto)

calculadoraAumentoPreco(precoProduto)