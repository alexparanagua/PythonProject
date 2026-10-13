import statistics as ss

dados = [1.2,3.4,1.7,4.5,3.2,2.3,5.6,2.4,1.6]

media = ss.mean(dados)

acima_media = filter(lambda x: x>media,dados)

print(f'Média = {media}')
print(list(acima_media))