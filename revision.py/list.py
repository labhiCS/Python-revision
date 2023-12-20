motorcycles = ["BMW", "Ducati", "Pulsar220","Honda" ]
message = "My first bike was " + motorcycles[1].title() + "."
print(message)
print(motorcycles)
motorcycles[1] = 'Ns200'
motorcycles.append("ducati600") #To add
motorcycles.append("Toyota")
del motorcycles[-1]  #To remove
del motorcycles[4]
print(motorcycles)
print(motorcycles[-4])
