def flippingBits(n):
    # Write your code here
    
    
    n = str(bin(n))[2:]
    b = ((32 - len(n)) * "0") + n
    num_list = [int(num) for num in b]

    for num in range(len(num_list)):
        if num_list[num] == 0:
            num_list[num] += 1
        elif num_list[num] == 1:
            num_list[num] -= 1

    bits_flipped = ""
            
    for num in num_list:
        bits_flipped += str(num)
    
    return int(bits_flipped, 2)
