import matplotlib.pyplot as plt

def criar_grafico_numero_filhos(data_frame, largura=6, altura=4):
    fig, ax = plt.subplots(figsize=(largura, altura))

    ordem = [0, 1, 2, 3, 4, 5]
    
    contagem = (
        data_frame["NumeroFilhos"]
        .value_counts()
        .reindex(ordem, fill_value=0)
    )

    barras = ax.barh(contagem.index.astype(str), contagem.values)

    # Definir limites do eixo x (agora é horizontal)
    ax.set_xlim(0, contagem.max() + 5)

    # Definir frequência do eixo x
    ax.set_xticks(range(0, contagem.max() + 5, 5))

    ax.set_title("Número de Filhos")
    ax.set_xlabel("Quantidade de pessoas")
    ax.set_ylabel("Número de filhos")

    # Adicionar números ao lado das barras
    for barra in barras:
        largura_barra = barra.get_width()
        ax.text(
            largura_barra + 0.3,
            barra.get_y() + barra.get_height() / 2,
            str(int(largura_barra)),
            va='center'
        )

    return fig