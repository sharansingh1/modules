import pyjokes

joke = pyjokes.get_joke('en','neutral')
print(joke)
# from random import randint
# import sys
# #generate num
# answer = randint(int(sys.argv[1],sys.argv[2]))
# #inut use
#
# # check if input is 1-10
# while True:
#    try:
#     guess = int(input('Guess num from 1-10: '))
#
#     if 0 < guess < 11:
#         if guess == answer:
#             print('u are genius')
#             break
#     else:
#         print('hey bozo i said 1-10')
#    except ValueError:
#        print('please enter valid number')
#        continue
#
# #check if num is right guess, otherwise ask again
