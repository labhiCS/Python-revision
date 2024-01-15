world_rivers = {
    'Bishnumati': 'Machhapokhari',
    'Hang Ho': 'China',
    'Nile': 'Egypt',
}

for k, v in world_rivers.items():
    print(k + " river " + "runs through " + v + ".")
    
print("\n The following rivers are included in the data: ")
for key, value in world_rivers.items():
    print(" - " +key + " river.")
