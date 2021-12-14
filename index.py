# while True:
#     num = int(input('Enter prime number: '))
#     try:
#         for factor in range(2,num):
#             if num % factor == 0: raise ValueError('Your number is not prime')
#         else: break
#     except ValueError as ve:
#         print(ve)

# while True:
#     password = input('Enter password: ')
#     try:
#         if len(password) < 8: raise ValueError('Your password should contain more than 8 letters.')
#         else: break
#     except ValueError as ve:
#         print(ve)


# while True:
#     try:
#         numOfTerms = int(input('Enter num of terms: '))
#         if numOfTerms < 2: raise ValueError('number of numOfTerms must be more than 2')
#         else: break
#     except ValueError as ve:
#         print(ve)
# while True:
#     acc = 0
#     for i in range(1, numOfTerms + 1):
#         num = int(input(f'Enter {i} term: '))
#         acc += num
#     try:
#         if acc < 100: raise ValueError('Sum is less than 100')
#         else:
#             print(acc)
#             break
#     except ValueError as ve:
#         print(f'sum should be more than 100. Try to enter {numOfTerms} again.')



# while True:
#     try:
#         numOfFactors = int(input('Enter the factors: '))
#         if numOfFactors < 2: raise ValueError('number of Factors must be more than 2')
#         else: break
#     except ValueError as ve:
#         print(ve)
# while True:
#     prod = 1
#     for i in range(1, numOfFactors + 1):
#         while True:
#             try:
#                 num = int(input(f'Enter {i} term: '))
#                 if num == 0: raise ValueError('Term should be nin-zero')
#                 else: break
#             except ValueError as ve:
#                 print(ve)
#         prod *= num

#     print(prod)




while True:
    try:
        numOfTerms = int(input('Enter num of terms: '))
        if numOfTerms < 2: raise ValueError('number of numOfTerms must be more than 2')
        else: break
    except ValueError as ve:
        print(ve)
list = []
for i in range(1, numOfTerms + 1):
    num = int(input(f'Enter {i} term: '))
    list.append(num)
acc = 0
for num in list:
    acc += num
sumOfEdges = list[1] + list[-1]
mean = acc
while True:  
    try:
        if mean < sumOfEdges: raise ValueError('Sum is less than mean')
        else:
            print(acc)
        break
    except ValueError as ve:
        print(ve)
        
