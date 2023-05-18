
# my_string = "Progra21Sremm3"
# s = 6
# e = 12


# new_string=[]
# new_string.append(my_string[: s - 1])
# new_string.append(reversed(my_string[s:e]))
# new_string.append(my_string[e + 1 :])
# print(new_string)




# reversed_str=list(reversed(my_string[s:e]))
# print(list(reversed(my_string[s:e])))




# a=my_string[:s]
# b="".join(reversed(my_string[s:e+1]))
# c=my_string[e+1:]


# print(a+b+c)

# str_list = [a,b,c]

# print("".join(str_list))





# .과 x를 k배한 새로운 리스트

picture	= [".xx...xx.", 
           "x..x.x..x", 
           "x...x...x", 
           ".x.....x.", 
           "..x...x..", 
           "...x.x...", 
           "....x...."]	
k = 2	
# result = ["..xxxx......xxxx..", 
#           "..xxxx......xxxx..", 
#           "xx....xx..xx....xx", 
#           "xx....xx..xx....xx", 
#           "xx......xx......xx", 
#           "xx......xx......xx",   
#           "..xx..........xx..",
#           "..xx..........xx..",
#           "....xx......xx....",
#           "....xx......xx....", 
#           "......xx..xx......", 
#           "......xx..xx......",
#           "........xx........",
#           "........xx........"]



answer = []

# for i,j in picture:
#     answer.append(i.replace(".", "."*k))
#     answer.append(j.replace("x", "x"*k))
# # ValueError: too many values to unpack (expected 2)

# for i in picture:
#     answer.append(i.replace({".":"."*k, "x":"x"*k}))
# TypeError: replace expected at least 2 arguments, got 1

# for i in picture:
#     answer.append(i.replace([".", "x"], ["."*k, "x"*k]))
# TypeError: replace() argument 1 must be str, not list

# for i in picture:
#     answer.append(i.replace(".", "."*k).replace("x", "x"*k))
# 결과값 몇개 다름


for j in picture:
    for i in range(k):
        answer.append(j.replace(".", "."*k).replace("x", "x"*k))


print(answer)

