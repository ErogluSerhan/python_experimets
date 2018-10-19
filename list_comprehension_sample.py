
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6,7,8]

print [item*2 for item in arr1 if item>4 and item<8]

print [[item1, item2] for item1 in arr1 for item2 in arr2 if item1+item2==8]

print [[item1, item2] for item1 in arr1 for item2 in arr2 if item1+item2==8]

# print [[item1, item2, sum(item1, item2)] for item1 in arr1 for item2 in arr2 if item1+item2==8]

