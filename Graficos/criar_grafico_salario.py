import matplotlib.pyplot as plt

def criar_grafico_salario(data_frame, largura=6, altura=4):
    fig, ax = plt.subplots(figsize=(largura, altura))

    salarios = data_frame["Salario"]

    # Histograma
    ax.hist(salarios, bins=8, edgecolor="black")

    ax.set_title("Distribuição de Salários")
    ax.set_xlabel("Salário (em salários mínimos)")
    ax.set_ylabel("Quantidade de pessoas")

    return fig