def breakingRecords(scores):
    # Write your code here
    
    min = scores[0]
    c =0
    max = scores[0]
    c1 =0
    for i in scores:
        if i < min:
            min = i
            c+=1
        if i > max:
            max = i
            c1+=1
    return c1,c
