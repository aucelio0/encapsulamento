# import classes as cl
from classes import *

if __name__ == "__main__":
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o email: ")

    # instancia
    usuario = Pessoa(nome, idade, email)

    # saida de dados
    print(f"\nNome: {usuario.nome}.")
    print(f"Nome: {usuario.idade}.")
    print(f"Nome: {usuario.email}.")