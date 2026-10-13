import datetime

nascimento = input("Digite data(dd/mm/aaaa): ")
n_list = nascimento.split("/")
print(n_list)

n_data = datetime.date(
    int(n_list[2]), int(n_list[1]), int(n_list[0])
)

print(n_data)
print(type(n_data))