def pangrams(s):
    # Write your code here
    x = 'abcdefghijklmnopqrstuvwxyz'
    s=s.lower()
    for i in x:
        if i.isalpha and i.lower() not in s:
            return 'not pangram'
    return 'pangram'
