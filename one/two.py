input_measurements = open("input.txt", "r").readlines()

measurements = [int(row) for row in input_measurements]

total_increased = 0
previous_value = 0
for count in range(len(measurements)):
    next_three = measurements[count:count+3]

    the_sum = sum(next_three)

    if count != 0 and the_sum > previous_value:
        total_increased += 1
    
    previous_value = the_sum

print(total_increased)