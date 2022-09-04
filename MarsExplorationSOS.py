def marsExploration(s):
    # Write your code here
    nums=0
    for i in s:
        if i!= 'S' and i!='O':
            nums+=1
    return nums
