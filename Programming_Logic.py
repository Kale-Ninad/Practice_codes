#### Write a program to reverse the input number
##inp = int(input("Enter the number: "))
##rev=0
##while(inp>0):
##    digit = inp%10
##    rev=rev*10+digit #rev=rev+digit #in case of total of the number
##    inp = inp//10
##
##print(rev)

#### What is the output of the program
##names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
##names2 = names1
##names3 = names1[:]
##
##names2[0] = 'Alice'
##names3[1] = 'Bob'
##
##print(names1, names2, names3)
##su = 0
##for ls in (names1, names2, names3):
##    if ls[0] == 'Alice':
##        su += 1
##    if ls[1] == 'Bob':
##        su += 10
##
##print(su)

####Python Program to Check if a Number is a Prime Number:


#### To check if string is palindrome or not

##def isPalindrome(str):
##    check = 0
## 
##    # Run loop from 0 to len/2
##    for i in range(0, int(len(str)/2)):
##        if str[i] != str[len(str)-i-1]:
##            check = 0
##        else:
##            check = 1
##
##    if check:
##        print("pal")
##    else:
##        print("Not Pal")
## 
### main function
##s = "millm"
##isPalindrome(s)

#### To check if a number is armstrong of not
##inp = int(input("Enter the number: "))
##check = inp
##divider = 0
##addition = 0
##while(inp>0):
##    divider = inp % 10
##    addition = addition + (divider**3)
##    inp = inp // 10
##
##if check == addition:
##    print("No is Armstrong")
##else:
##    print("No is not Armstrong")

#### To check if number is perfect or not
##inp = int(input("Enter the number: "))
##addi = 0
##for itr in range(1,inp):
##    if (inp % itr ==0):
##        addi += itr
##        print(itr)
##
##if inp==addi:
##    print("Number is Perfect")
##else:
##    print("Number is not Perfect")

#### Find the factorial of a no.
##inp = int(input("Enter the number: "))
##Fac = 1
##for itr in range(1,inp+1):
##    Fac=Fac*itr
##print(Fac)

#### Find out the no. is strong or not
##value = int(input("Enter the number: "))
##check = value
##Fac = 1
##divider = 0
##tmp = 0
##while(value>0):
##    divider = value%10
##    Fac = 1
##    for itr in range(1,divider+1):
##        Fac=Fac*itr
##    tmp += Fac
##    value = value//10
##if tmp == check:
##    print("Yes")
##else:
##    print("No")

#### To count the no. of word in a string is repeating how many times
##inp = input("Enter the string here: ")
##res= {}
##words = inp.split() ## words = [x for x in inp] # to split into character
##for word in words:
##    if word in res:
##        res[word] += 1
##    else:
##        res[word] = 1
##
##print(res)

####Write a Python Program to Check Common Letters in Two Input Strings
##s1=input("Enter first string:")
##s2=input("Enter second string:")
##a=list(set(s1)&set(s2))
##print("The common letters are: ",a)

#### Prime Numbers Array
##n = int(input("Enter the number to find out upto prime"))
##
##prime_nums = []
##for num in range(2,n):
##    for i in range(2, num):
##        if (num % i) == 0: # if the modulus == 0 is means that the number can be divided by a number preceding it
##            break
##    else:
##        prime_nums.append(num)
##print(prime_nums)


