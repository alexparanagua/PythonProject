nums = [1,2,3,4,5,6,7,8,9,10,11,12]

nova = []

for i in range(len(nums)):
    nova.append(nums[i]*2)

nova2 = [x*2 for x in nums]

print(nums)

print(nova)

print(nova2)

#aula69

nova3 = [x**2 for x in nums if(x % 2)]

print(nova3)

nova4 = [x/2 for x in nums if not (x%2)]

print(nova4)

amigos = ["ana","marcela","fernando","pedro","roberto","alex","brena","aurelino", "barbara"]
print(amigos)
print([amigo.title() for amigo in amigos])