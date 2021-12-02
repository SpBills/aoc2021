horizontal_index = 0
depth_index = 0

def go(direction_interval):
    direction = direction_interval[0]
    interval = int(direction_interval[1])

    if (direction == "forward"):
        forward(interval)
    elif (direction == "down"):
        down(interval)
    elif (direction == "up"):
        up(interval)

def forward(x):
    global horizontal_index
    horizontal_index += x

def down(x):
    global depth_index
    depth_index += x

def up(x):
    global depth_index
    depth_index -= x

def main():
    with open("input.txt", "r") as positions_list_file:
        positions_list = positions_list_file.readlines()

        for line in positions_list:
            direction_interval = line.split(" ")

            go(direction_interval)

    print(horizontal_index * depth_index)

main()
