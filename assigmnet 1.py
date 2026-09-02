# operation on list
list1=["ayush","soham","dhyan","manish"]
print("your original list is",list1)

            ### add name###
list1.append("rudra")
print("your new list after appending is",list1)

            ### delete name ###
list1.remove("ayush")
print("your new list after removing is",list1)

            ### update list ###
list1[2]="vihaan"
print("your new list after updating is",list1)


# operation on tuples
tup1=("sachi","aayushi","yashvi","bhakti")
print("your new tuple is",tup1)

            ### add name ###

new_list=list(tup1) # to perform operation on tuple you will have ot convert it into list #
new_list.append("aarzoo")
tup2=tuple(new_list)
print("new tuple after adding name is",tup2)

            ### deleted name ###

list_2= list(tup2)
list_2.remove("yashvi")
tup3 = tuple(list_2)
print("new tuple after removing name is",tup3)

            ### update name ###

list_3=list(tup3)
list_3[1]="kiara"
tup4=tuple(list_3)
print("new tuple after updating name is",tup4)

#operations on dictionary#
dict1={"dhyan":18,"year":2008,"soham":"sachi"}
print("original dictionary is",dict1)

            ### add element ###
dict1.update({"month":7})
print("new dictionary after updating name is",dict1)

            ### update element ###
dict1.update({"nem month":9})
print("new dictionary after updating name is",dict1)

            ### delete elemnt ###
del dict1["soham"]
print("new dictionary after removing name is",dict1)


