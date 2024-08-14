#dicionario
"""subalgoritimos"""

def exibicao_manual(d: dict) -> None:
    print(f"Nome.............: {d['nome']}")
    print(f"Idade............: {d['idade']}")
    print(f"Estado civil.....: {d['casado']}")
    print(f"Peso.............: {d['peso']}")

def exibicao_automatica(d: dict) -> None:
    for k, v in contato.items():
        print(f"{k} -> {v}")


"""código"""
import os
os.system("cls")

contato = {
    #Key : value,

    'nome' : 'André',
    'idade' : 17,
    'casado' : False,
    'peso' : 49 
}

print(contato)

print(contato.keys())

#os.system("cls")
