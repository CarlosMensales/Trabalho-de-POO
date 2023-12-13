class MaterialConstrucao:
    def _init_(self, nome, preco_unitario):
        self.nome = nome
        self.preco_unitario = preco_unitario

    def calcular_quantidade(self, metragem):
        pass 


class Tijolo(MaterialConstrucao):
    def _init_(self, preco_unitario, unidades_por_metro_quadrado):
        super()._init_('Tijolo', preco_unitario)
        self.unidades_por_metro_quadrado = unidades_por_metro_quadrado

    def calcular_quantidade(self, metragem):
        return metragem * self.unidades_por_metro_quadrado

class Argamassa(MaterialConstrucao):
    def _init_(self, preco_unitario, kg_por_metro_quadrado):
        super()._init_('Argamassa', preco_unitario)
        self.kg_por_metro_quadrado = kg_por_metro_quadrado

    def calcular_quantidade(self, metragem):
        return metragem * self.kg_por_metro_quadrado


class CalculadoraMaterialConstrucao:
    def _init_(self):
        self.__materiais = []

    def adicionar_material(self, material):
        self.__materiais.append(material)

    def calcular_materiais(self, metragem):
        resultado = {}
        for material in self.materiais:
            quantidade = material.calcular_quantidade(metragem)
            resultado[material.nome] = quantidade
        return resultado


if __name__ == "_main_":
    tijolo = Tijolo(preco_unitario=0.2, unidades_por_metro_quadrado=50)
    argamassa = Argamassa(preco_unitario=1.5, kg_por_metro_quadrado=2)

    calculadora = CalculadoraMaterialConstrucao()
    calculadora.adicionar_material(tijolo)
    calculadora.adicionar_material(argamassa)

    metragem_do_comodo = float(input("Digite a metragem do cômodo: "))

    resultado = calculadora.calcular_materiais(metragem_do_comodo)

    print("\nQuantidade de materiais necessários:")
    for material, quantidade in resultado.items():
        print(f"{material}: {quantidade}")