# # TUPLE
# # creations
# t1=(1,2,3,4,5,6,7,8,9,1)
# print(type(t1))
# print(t1[0])
# l1=[1,2,3,4,5,6,7]
# t2=tuple(l1)
# print(type(t2),t2)
# s1='python'
# t3=tuple(s1)
# print(type(t3),t3)
# t4=()
# print(type(t4),t4)
# t5=(3,)
# print(type(t5))
# a=1,2,3,4,5,6,7
# print(type(a),a)


# # indexing and slicling
# print(t1[-2])


# print(t1[ ::-1])

# x1=t1[1:7:1]
# print(type(x1),x1)

# traverls
# t1=(1,2,3,4,5,6,7,8,9,0)
# for i in t1:
#     print(i)

# for i in range(len(t1)):
#     print(t1[i])


# #concatination and repetation
# t2=(2,3,4,5)
# t3=(6,7,8,9)
# t4=t2+t3 
# print(type(t4),t4)
# # repetations
# print(t2*4)

# nested tuples
# t1=((1,2,3),(4,5,6),(7,8,9))
# t2=((9,8,7),(6,5,4),(3,2,1))
# x1=t1[1][1]+t2[0][1]
# print(x1)

# packing & unpacking
# t1=(1,2,3,4,5,6,7,8,9)
# # a,b,c,d,e,f,g,h,i=t1
# # print(a,b,c,d,e,f,g,h,i)

# a,*b,c=t1
# print(a)
# print(b)
# print(c)

# tuple cpmprahension

# t1=(*(x**2 for x in range(1,5)),)
# print(t1)
