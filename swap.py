def swap_list(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
    
    
List = []

n = int(input("Enter the list size "))
while n > 0:
    print("\n")
    for i in range(0, n):
        print("Enter number at index", i, )
        item = int(input())
        List.append(item)
    print("User list is ", list)    

    if n % 2 == 1:
        pos1, pos2  = (n//2)+1 , n
        print(swap_list(List, pos1-1, pos2-1))
    
    if n % 2 == 0:
        pos1, pos2  = (n//2) , n
        print(swap_list(List, pos1-1, pos2-1))