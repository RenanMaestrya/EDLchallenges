class ItemInventario:
    def __init__(self, codigo, quantidade, localizacao, data_entrada, data_validade=None):
        self.codigo = codigo
        self.quantidade = quantidade
        self.localizacao = localizacao
        self.data_entrada = data_entrada
        self.data_validade = data_validade

# Tabela Hash para armazenar os itens no inventário
tabela_inventario = {}

# Função para adicionar um item ao inventário
def adicionar_item(codigo, quantidade, localizacao, data_entrada, data_validade=None):
    item = ItemInventario(codigo, quantidade, localizacao, data_entrada, data_validade)
    tabela_inventario[codigo] = item

# Função para atualizar a quantidade de um item no inventário
def atualizar_quantidade(codigo, nova_quantidade):
    if codigo in tabela_inventario:
        tabela_inventario[codigo].quantidade = nova_quantidade
    else:
        print("Item não encontrado no inventário.")

# Função para consultar um item no inventário
def consultar_item(codigo):
    return tabela_inventario.get(codigo, "Item não encontrado no inventário.")

# Exemplo de uso
adicionar_item("123ABC", 100, "Prateleira 1", "2023-01-01", "2024-01-01")
atualizar_quantidade("123ABC", 80)
print(consultar_item("123ABC"))
