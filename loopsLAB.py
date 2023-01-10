for firstRange in range (45,210) :
    print (firstRange)
    if firstRange == 100 :
        continue
    elif firstRange == 205 :
        print (firstRange)
        break 



product = int(input("what is the product of 7 *24 ? "))
while product != -1 :
 if product== 168 :
    print ("You answered this Question correctly")
    break
 else  :
    print ("Your Answer is wrong try again..")
 product = int(input("what is the product of 7 *24 ? "))
print("end")