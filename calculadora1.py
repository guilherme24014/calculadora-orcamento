import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class CalculadoraOrcamento:
    def __init__(self, root):
        self.salario = 0
        self.despesas = []

        root.title("Calculadora de Orçamento")
        root.geometry("400x500")

        tk.Label(root, text="Salário:").pack()
        self.entrada_salario = tk.Entry(root)
        self.entrada_salario.pack()

        tk.Label(root, text="Despesa:").pack()
        self.nome_despesa = tk.Entry(root)
        self.nome_despesa.pack()

        tk.Label(root, text="Valor:").pack()
        self.valor_despesa = tk.Entry(root)
        self.valor_despesa.pack()

        tk.Button(root, text="Adicionar Despesa", command=self.adicionar_despesa).pack(pady=5)

        self.texto_resultado = tk.Label(root, text="", fg="blue")
        self.texto_resultado.pack(pady=10)

        self.lista_despesas = tk.Text(root, height=10, width=45)
        self.lista_despesas.pack()

        tk.Button(root, text="Mostrar Gráfico", command=self.mostrar_grafico).pack(pady=10)

    def adicionar_despesa(self):
        try:
            if self.salario == 0:
                self.salario = float(self.entrada_salario.get())

            nome = self.nome_despesa.get()
            valor = float(self.valor_despesa.get())

            self.despesas.append((nome, valor))
            self.atualizar_resultado()

            self.nome_despesa.delete(0, tk.END)
            self.valor_despesa.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

    def atualizar_resultado(self):
        total = sum(valor for _, valor in self.despesas)
        saldo = self.salario - total

        self.texto_resultado.config(
            text=f"Total de despesas: R$ {total:.2f}\nSaldo restante: R$ {saldo:.2f}",
            fg="green" if saldo >= 0 else "red"
        )

        self.lista_despesas.delete("1.0", tk.END)
        for nome, valor in self.despesas:
            self.lista_despesas.insert(tk.END, f"{nome}: R$ {valor:.2f}\n")

    def mostrar_grafico(self):
        if not self.despesas:
            messagebox.showinfo("Aviso", "Adicione pelo menos uma despesa.")
            return

        categorias = [nome for nome, _ in self.despesas]
        valores = [valor for _, valor in self.despesas]

        plt.figure(figsize=(6, 6))
        plt.pie(valores, labels=categorias, autopct="%1.1f%%", startangle=140)
        plt.title("Distribuição das Despesas")
        plt.axis("equal")
        plt.show()

# Iniciar o app
janela = tk.Tk()
app = CalculadoraOrcamento(janela)
janela.mainloop()



