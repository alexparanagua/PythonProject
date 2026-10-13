try:
    num = int(input("Digite num: "))
except :
    print("Valor incorreto")
else :
    print(f"Voce digitou {num}")
finally:
    print("Fim")