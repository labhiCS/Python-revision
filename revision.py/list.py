motorcycles = ["Pulsar220", "BMW", "Ducati","Honda" ]
motorcycles.sort()     #To organize
print(motorcycles)
print("\n")

message = "My first bike was " + motorcycles[1].title() + "."
print(message)

motorcycles[1] = 'Ns200'
motorcycles.append("ducati600") #To add
motorcycles.append("Toyota")

del motorcycles[-1]     #To remove.
del motorcycles[4]
motorcycles.remove("BMW")
print(motorcycles)

motorcycles.reverse()   #To reverse.
print(motorcycles)

len(motorcycles)  #To find the length of the list.

print(motorcycles[-2])
print(motorcycles[-1])
