temps = {}
tempRange = 60
tempRange2 = 150
tempStep = 10

for f in range(tempRange, tempRange2, tempStep):
	temps[f] = (5/9)*(f-32)

print(temps)
