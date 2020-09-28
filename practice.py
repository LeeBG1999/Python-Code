# my_list=[1,2,3,4,5,6,7,8,9]
# sum_list=0
# for i in my_list:
#     sum_list+=i
# print(sum_list)
# for char in enumerate('hello'):
#     print(char)


#--------------------------------------------------------------------------


# picture=[[0,0,0,1,0,0,0],
#          [0,0,1,1,1,0,0],
#          [0,1,1,1,1,1,0],
#          [1,1,1,1,1,1,1],
#          [0,0,0,1,0,0,0],
#          [0,0,0,1,0,0,0]]

# for a in picture:
#     save=''
#     for b in a:
#         if b==1:
#             save =save + '*'
#         else:
#             save =save + ' '
#     print(save)


#-------------------------------------------------------------



# my_list=[10,2,3,4,6,2,11]
# def highest_value(values):
#     values.sort(reverse=True)
#     return values[0]
# print(highest_value(my_list))



#-------------------------------------------------------------


# sp = {
#     'a':1,
#     'b':2
# }
# my = {k:v*2 for k,v in sp.items()}
# print(my)



#-------------------------------------------------------------


lis = ['a','b','c','b','d','m','n','n','e','c','f']
ans = [a for a in lis if lis.count(a) > 1 ]
print(ans)