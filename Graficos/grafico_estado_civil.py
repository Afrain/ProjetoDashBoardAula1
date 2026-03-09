import matplotlib.pyplot as plt

def criar_grafico_estado_civil(data_frame, largura=6, altura=4):
    #GRAFICO ESTADO CIVIL (PIZZA)

    # Gráfico de barras usando matplotlib
    fig, ax = plt.subplots(figsize=(largura, altura))

    ordem = ["Casado", "Solteiro"]
    
    contagem = (
        data_frame["EstadoCivil"]
        .value_counts()
        .reindex(ordem, fill_value=0)
    )

    ax.pie(
        contagem.values,
        labels=contagem.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Estado Civil")

    return fig
