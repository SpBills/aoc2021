input_str = open("input.txt", "r").readlines()

total = 0
previous = int(input_str[0])
for line in input_str:
    val = int(line)
    if val > previous:
        total += 1
    
    previous = val

print(total)