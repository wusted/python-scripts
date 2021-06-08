long_names_counter = 0
long_names = []

for names in ["Joe", "Sally", "Amy", "Brad"]:
    if len(names) > 3:
        long_names_counter += 1
        long_names += [names]
        
print(long_names)
print(long_names_counter)
