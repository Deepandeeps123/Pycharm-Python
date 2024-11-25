'''
RegularEx
'''

# s='hello'
# for aeiouAEIOU in s[0]:
#     print(s)

# s='Bannana'
# for aeiouAEIOU in s[1]:
#       if True:
#        print('start with vowel')
#       else:
#          print('Not start with vowel')




# import re
# s='Hello'
# print(re.findall('.',s))




# import re
# s='Hello every one guys ........'
# print(re.findall('.',s))


# import re
# s='Hello good morning'
# print(re.findall('.',s))



# import re
# s='hello \n good \n morning'
# print(re.findall('.',s))



# import re
# s='Hello...'
# # print(re.findall('.',s))
# print(re.findall(r'\.',s))



# import re
# s='Hello***'
# print(re.findall(r'\*',s))


# import re
# s='Hello&&&'
# print(re.findall(r'\&',s))


# import  re
# s='aello'
# res=re.findall('[aeiou]',s[0])
# if res:
#     print('Yes')
# else:
#     print('Not')

#
# import re
# s='apple'
# res=re.findall('[aeiouAEIOU]',s[0])
# if res:
#     print('Vowel')
# else:
#     print('Not')




# import re
# s='GrapeS'
# res=re.findall('[aeiouAEIOU]',s[-1])
# if res:
#     print('end with consonent')
# else:
#     print('Not')



# import re
# s='GrapeS'
# res=re.findall('[^aeiou]',s[-1])
# if res:
#     print('end with consonent')
# else:
#     print('Not')


# import re
# s='hElLo12345@'
# print(re.findall('[a-zA-Z]',s))


# import re
# s='hElLo12345@'
# print(re.findall('[^a-zA-Z]',s))


# import re
# s='hElLo12345@'
# print(re.findall('[0-9]',s))


# import re
# s='hElLo12345@'
# print(re.findall('[^0-9]',s))


# import re
# s='hElLo12345@'
# print(re.findall('[a-zA-Z0-9]',s))



# import re
# s='hElLo12345@'
# print(re.findall('[^a-zA-Z0-9b]',s))


#
# import re
# s='hello12345@#$%^^^'
# print(re.findall('[0123456789]',s))

# import re
# s='hElLo12345@'
# print(re.findall(r'\w',s))
#
#
# import re
# s='hElLo12345@'
# print(re.findall('[a-zA-Z0-9]',s))



# import re
# s='hElLo12345___@'
# print(re.findall(r'\W',s))


#
# import re
# s='hElLo12345__@#$'
# print(re.findall(r'\d',s))



# import re
# s='hElLo123___@#$$'
# print(re.findall(r'\D',s))

# import re
# s='hello'
# print(re.findall('^h',s))



# import re
# sub=input()
# res=re.findall('^py',sub)
# if res:
#     print('Student')


# else:
#     # print('Not')

# import re
# s='grapes'
# print(re.findall('s$',s))


# import re
# s='Hello'
# print(re.findall('^h*.o$',s))