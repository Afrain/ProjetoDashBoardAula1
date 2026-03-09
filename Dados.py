import pandas as pd

def carregar_dados():
    
    dados = [
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":4.00,"IdadeAnos":26,"IdadeMeses":3,"Regiao":"Interior"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":1,"Salario":4.56,"IdadeAnos":32,"IdadeMeses":10,"Regiao":"Capital"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":2,"Salario":5.25,"IdadeAnos":36,"IdadeMeses":5,"Regiao":"Capital"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":5.73,"IdadeAnos":20,"IdadeMeses":10,"Regiao":"Outra"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":6.26,"IdadeAnos":40,"IdadeMeses":7,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":6.66,"IdadeAnos":28,"IdadeMeses":0,"Regiao":"Interior"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":6.86,"IdadeAnos":41,"IdadeMeses":0,"Regiao":"Interior"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":7.39,"IdadeAnos":43,"IdadeMeses":4,"Regiao":"Capital"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":1,"Salario":7.59,"IdadeAnos":34,"IdadeMeses":10,"Regiao":"Capital"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":7.84,"IdadeAnos":23,"IdadeMeses":6,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":2,"Salario":8.12,"IdadeAnos":33,"IdadeMeses":6,"Regiao":"Interior"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":8.46,"IdadeAnos":27,"IdadeMeses":11,"Regiao":"Capital"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":8.74,"IdadeAnos":37,"IdadeMeses":5,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":3,"Salario":8.95,"IdadeAnos":44,"IdadeMeses":2,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":9.13,"IdadeAnos":30,"IdadeMeses":5,"Regiao":"Interior"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":9.35,"IdadeAnos":38,"IdadeMeses":8,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":1,"Salario":9.77,"IdadeAnos":31,"IdadeMeses":7,"Regiao":"Capital"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":2,"Salario":9.80,"IdadeAnos":39,"IdadeMeses":7,"Regiao":"Outra"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Superior","NumeroFilhos":0,"Salario":10.53,"IdadeAnos":25,"IdadeMeses":8,"Regiao":"Interior"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":10.76,"IdadeAnos":37,"IdadeMeses":4,"Regiao":"Interior"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":1,"Salario":11.06,"IdadeAnos":30,"IdadeMeses":9,"Regiao":"Outra"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":11.59,"IdadeAnos":34,"IdadeMeses":2,"Regiao":"Capital"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":12.00,"IdadeAnos":41,"IdadeMeses":0,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Superior","NumeroFilhos":0,"Salario":12.79,"IdadeAnos":26,"IdadeMeses":1,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":2,"Salario":13.23,"IdadeAnos":32,"IdadeMeses":5,"Regiao":"Interior"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":2,"Salario":13.60,"IdadeAnos":35,"IdadeMeses":0,"Regiao":"Outra"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Ensino Fundamental","NumeroFilhos":0,"Salario":13.85,"IdadeAnos":46,"IdadeMeses":7,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":0,"Salario":14.69,"IdadeAnos":29,"IdadeMeses":8,"Regiao":"Interior"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":5,"Salario":14.71,"IdadeAnos":40,"IdadeMeses":6,"Regiao":"Interior"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":2,"Salario":15.99,"IdadeAnos":35,"IdadeMeses":10,"Regiao":"Capital"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Superior","NumeroFilhos":0,"Salario":16.22,"IdadeAnos":31,"IdadeMeses":5,"Regiao":"Outra"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":1,"Salario":16.61,"IdadeAnos":36,"IdadeMeses":4,"Regiao":"Interior"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Superior","NumeroFilhos":3,"Salario":17.26,"IdadeAnos":43,"IdadeMeses":7,"Regiao":"Capital"},
        {"EstadoCivil":"Solteiro","GrauDeInstrucao":"Superior","NumeroFilhos":0,"Salario":18.75,"IdadeAnos":33,"IdadeMeses":7,"Regiao":"Capital"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Ensino Médio","NumeroFilhos":2,"Salario":19.40,"IdadeAnos":48,"IdadeMeses":11,"Regiao":"Capital"},
        {"EstadoCivil":"Casado","GrauDeInstrucao":"Superior","NumeroFilhos":3,"Salario":23.30,"IdadeAnos":42,"IdadeMeses":2,"Regiao":"Interior"}
    ]

    return pd.DataFrame(dados)