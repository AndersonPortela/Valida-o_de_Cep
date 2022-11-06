import requests

from valida_cep import BuscaEndereco
cep = input("Digite seu cep para busca:")
objeto_cep = BuscaEndereco(cep)

cidade, uf = objeto_cep.acessa_via_cep()

print("Seu Cep é válido,esta localizado na cidade de {} em {}".format(cidade, uf))