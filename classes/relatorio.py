class Relatorio:
    def __init__(self, lista_vendas):
        # Aqui recebemos a lista de objetos 'Venda'
        self._lista_vendas = lista_vendas

    def gerar_vendas_financeiro(self):
        print("\n" + "="*50)
        print("📊 RELATÓRIO FINANCEIRO - CONSOLIDADO")
        print("="*50)
        print(f"{'ID':<5} | {'Cliente':<18} | {'Valor (R$)':<10} | {'Metodo'}")
        print("-" * 50)        
       
        no_atual = self._lista_vendas.cabeca # Começa do primeiro Nó
        total = 0             
        contador = 101

        while no_atual:
            v = no_atual.produto 
            valor_venda = v._valor_total
            nome_cliente = v._usuario.nome
            valor = v._valor_total if hasattr(v, 'valor_total') else 0
            
            print(f"{contador:<5} | {v._usuario.nome[:18]:<18} | {valor_venda:<10.2f} | PIX")
            total += valor_venda
            no_atual = no_atual.proximo
            contador += 1
            
        print("-" * 50)
        print(f"💰 FATURAMENTO TOTAL: R$ {total:.2f}")
        print(f"✅ Total de Transações: {contador - 101}")
        print("="*50)

    def gerar_consumo_perfil(self):
        print("\n" + "="*50)
        print("🍕 RELATÓRIO DE CONSUMO POR CATEGORIA")
        print("="*50)
        print(f"{'Consumidor':<18} | {'Tipo':<10} | {'Produto'}")
        print("-" * 50)
        
        no_atual = self._lista_vendas.cabeca
        contador = 1
        total = 0

        no_atual = self._lista_vendas.cabeca
        while no_atual:
            v = no_atual.produto
            tipo = type(v._usuario).__name__
            valor_venda = v._valor_total
            print(f"{contador:<5} | {v._usuario.nome[:18]:<18} | {valor_venda:<10.2f} | PIX")
            no_atual = no_atual.proximo

            total += valor_venda
            contador += 1
            no_atual = no_atual.proximo
            
        print("-" * 50)
        print("📊 Fim do Relatório de Consumo")
        print("="*50)
        print(f"\n💰 TOTAL ACUMULADO NESTE PERFIL: R$ {total:.2f}")