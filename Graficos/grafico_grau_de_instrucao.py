import matplotlib.pyplot as plt

def criar_grafico_grau_de_instrucao(data_frame, largura=6, altura=4):
    fig1, ax1 = plt.subplots(figsize=(largura, altura))
    
    ordem = ["Ensino Fundamental", "Ensino Médio", "Superior"]
    
    contagem = (
        data_frame["GrauDeInstrucao"]
        .value_counts()
        .reindex(ordem, fill_value=0)
        )
    
    barras = ax1.bar(contagem.index, contagem.values)

    #Definir limites do eixo y
    ax1.set_ylim(0, contagem.max() + 5)

    #Definir frequência do eixo y
    ax1.set_yticks(range(0, contagem.max() + 5, 5))

    ax1.set_title("Grau de Instrução")
    ax1.tick_params(axis='x', rotation=15)

    # Adicionar números em cima das barras
    for barra in barras:
        altura = barra.get_height()
        ax1.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 0.5,
            str(int(altura)),
            ha='center',
            va='bottom'
        )

    fig1.tight_layout()
    
    return fig1