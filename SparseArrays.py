def matchingStrings(strings, queries):
    # Write your code here
    Arr = []
    for x in queries:
        Arr.append(strings.count(x))
    return Arr
