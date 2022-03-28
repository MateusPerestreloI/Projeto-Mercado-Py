from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda as fm

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    pass

def cadastrar_produto() -> None:
    pass

def listar_produto() -> None:
    pass

def comprar_produto() -> None:
    pass

def visaualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    pass

def achar_por_codigo() -> None:
    pass

if __name__ == '__main__':
    main()