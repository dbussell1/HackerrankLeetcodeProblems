def countingValleys(steps, path):
    # Write your code here
    level=0
    valleys=0  
    for i in path:
        if i == 'D':
            level -= 1
        else:
            if level+1 == 0:
                valleys += 1
            level += 1

    return valleys
