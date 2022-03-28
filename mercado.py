from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda as fm

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('========================================')
    print('============= Bem-vindo(a) =============')
    print('================ Shop ==================')
    print('========================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('-------------------------------------------------------------------------')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome=nome, preco=preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listar de Produto')
        print('-------------------------------------------------------------------------')
        for produto in produtos:
            print(produto)
            print('------------------------------------')
            sleep(1)
    else:
        print('Ainda não existe(m) produto(s) cadastrado(s)!')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('========================= Produtos Disponíveis =========================')
        for produto in produtos:
            print(produto)
            print('------------------------------------')
            sleep(1)
        print('========================================================================')
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('------------------------------------------------------------------------')
        codigo: int = int(input())

        produto: Produto = achar_por_codigo(codigo)
        print(f'Quanta(s) unidade(s) do produto {produto.nome} você deseja adicionar ao carrinho?')
        quant_quer: int = int(input())
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + quant_quer
                        print(f'O produto {produto.nome} agora possui {quant + 1} de unidade(s) no carrinho!')
                        tem_no_carrinho = True
                if not tem_no_carrinho:
                    prod = {produto: quant_quer}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho!')
            else:
                item = {produto: quant_quer}
                carrinho.append(item)
                print(f'O Produto {produto.nome} foi adicionado ao carrinho!')
        else:
            print(f'O produto com código {codigo} não foi encontrado!')
    else:
        print('Ainda não existe(m) produto(s) para vender!')
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-------------------------------')
                sleep(1)
    else:
        print('Ainda não existe(m) produto(s) no carrinho!')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        print('Produtos no Carrinho')
        print('-------------------------------------------------------------------------')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-------------------------')
                sleep(1)
        print(f'Sua fatura é {fm(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existe(m) produto(s) no carrinho!')
    sleep(2)
    menu()

def achar_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()