def main():

    # Problem : There are 100 doors in a row that are all initially closed. You make 100 passes by the doors. The
    #     # first time through, visit every door and  toggle  the door  (if the door is closed,  open it;   if it is open,
    #     # close it). The second time, only visit every 2nd door   (door #2, #4, #6, ...),   and toggle it. The third
    #     # time, visit every 3rd door   (door #3, #6, #9, ...), etc,   until you only visit the 100th door. Answer the
    #     # question:   what state are the doors in after the last pass?   Which are open, which are closed?

    # create the list with 100 closed doors

   doors = []
    for i in range(100):
        doors.append(0)
    print(doors)

    # first pass to open all the doors

    for i in range(100):
        doors[i] = 1
    print(doors)

    # checks if door is open or closed . if open = closed

    for i in range(1, 100):
        for j in range(i, 100, i + 1):
            if doors[j] == 1:
                doors[j] = 0
            else:
                doors[j] = 1
        print(doors)
    # state the open positions
    for index, i in enumerate(doors):
        if doors[index]:
            print(f'Door at position {index} is Open')


if __name__ == '__main__':
    main()
