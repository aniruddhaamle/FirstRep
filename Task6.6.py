def IntersecOfSets(list1, list2, list3):
    # Converting the arrays into sets
    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)
     
    # Calculates intersection of 
    # sets on s1 and s2
    set1 = s1.intersection(s2)         #[80, 20, 100]
     
    # Calculates intersection of sets
    # on set1 and s3
    result_set = set1.intersection(s3)
     
    # Converts resulting set to list
    final_list = list(result_set)
    print("Common Elements in the lists are " , final_list)


 # Elements in Array1
list1 = [1, 5, 10, 20, 40, 80, 100]
# Elements in Array2
list2 = [6, 7, 20, 80, 100]
# Elements in Array3
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

IntersecOfSets(list1, list2, list3)