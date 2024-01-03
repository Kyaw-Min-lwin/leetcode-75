# problem : a rotated sorted list is given and u need to determine the number of rotations
# [3, 4, 5, 1, 2]

def rotate(li):
    if len(li) <= 1:
        return 0
    
    previous = li[0]
    count = 0
    for i in range(1, len(li)):
        if (li[i] < previous):
            count  += 1
            return count
        count += 1


print(rotate([5, 6, 7, 1, 2, 3, 4]))
print(rotate([ 7, 9, 3, 5, 6]))