motorcycles = ["Pulsar220", "BMW", "Ducati","Honda" ]
motorcycles.sort()     #To organize
print(motorcycles)
print("\n")

message = "My first bike was " + motorcycles[1] + "."
print(message)

motorcycles[1] = 'Ns200'
motorcycles.append("ducati1000") #To add
motorcycles.append("Toyota")
motorcycles.append("Suzuki")

del motorcycles[-1]     #To remove.
del motorcycles[3]
motorcycles.remove("BMW")
print(motorcycles)

motorcycles.reverse()   #To reverse.
motorcycles.pop(0)
print(motorcycles)

len(motorcycles)  #To find the length of the list.

print(motorcycles[-2])
print(motorcycles[-1])
