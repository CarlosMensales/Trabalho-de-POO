import tkinter as tk
from tkinter import Button, Entry, Label, messagebox
from index import *

class InterfaceConstrucao(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Calculadora de Material de Construção")

        self.label_metragem = Label(self, text="Metragem do Cômodo:")
        self.entry_metragem = Entry(self)

        self.label_metragem.grid(row=0, column=0, padx=10, pady=10)
        self.entry_metragem.grid(row=0, column=1, padx=10, pady=10)

        self.btn_calcular = Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=1, column=0, columnspan=2, pady=10)

        self.resultado_label = Label(self, text="")
        self.resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Criar instância da calculadora
        self.calculadora = CalculadoraMaterialConstrucao()

        # Adicionar alguns materiais de exemplo
        self.calculadora.adicionar_material(Tijolo(preco_unitario=0.2, unidades_por_metro_quadrado=50))
        self.calculadora.adicionar_material(Argamassa(preco_unitario=1.5, kg_por_metro_quadrado=2))

    def calcular(self):
        try:
            metragem = float(self.entry_metragem.get())
            resultado = self.calculadora.calcular_materiais(metragem)
            
            mensagem = "\nQuantidade de materiais necessários:\n"
            for material, quantidade in resultado.items():
                mensagem += f"{material}: {quantidade}\n"

            self.resultado_label.config(text=mensagem)

        except ValueError:
            messagebox.showerror("Erro", "Digite uma metragem válida.")

if __name__ == "_main_":
    app = InterfaceConstrucao()
    app.mainloop()