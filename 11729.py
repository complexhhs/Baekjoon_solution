def hanoi_tower(disk):
    if disk == 1:
        count = 1
        return count
    count = 2*hanoi_tower(disk-1)+1
    return count

def hanoi_movement(height,start,assist,goal):
    if height == 1:
        print(str(start)+' '+str(goal))
        return 

    hanoi_movement(height-1,start,goal,assist)
    print(str(start)+' '+str(goal))
    hanoi_movement(height-1,assist,start,goal)



number_disk = int(input())
count = hanoi_tower(number_disk)
print(count)
hanoi_movement(number_disk,1,2,3)
