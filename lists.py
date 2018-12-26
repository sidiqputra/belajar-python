car = ["toyota", "mitsubishi", "daihatsu"]
print(car[1])
car[1] = "datsun"
print(car)

car.insert(1, "mercy")

for x in car:
 print(x)

print("\n")

print("check car list")
carlist = input()

if carlist in car:
 print('yes there is ' + carlist +' in car list')
else:
 print('the entry not exists')