def extrapolate(arr):
    is_zero = True
    for x in arr:
        is_zero = is_zero and x == 0
    if is_zero:
        return 0
    
    next_arr = [y-x for x, y in zip(arr, arr[1:])]
    added_val = extrapolate(next_arr)
    return arr[-1] + added_val

def extrapolate2(arr):
    is_zero = True
    for x in arr:
        is_zero = is_zero and x == 0
    if is_zero:
        return 0
    
    next_arr = [y-x for x, y in zip(arr, arr[1:])]
    added_val = extrapolate2(next_arr)
    return arr[0] - added_val


tot = 0
tot2 = 0
for line in open('./input.txt').readlines():
    arr = [int(x) for x in line.split()]
    tot += extrapolate(arr)
    tot2 += extrapolate2(arr)

print('Total star1:', tot)
print('Total star2:', tot2)