import time
import os
List = []
Number = int(input("what number would you like to divide?: "))
Limit= int(input("how many times would you like to Brute force it?"))
#rint("By the way we are skipping the number 1")
start = time.time()
for x in range(1,Limit+1):
    if Number % x == 0:
        print"Found the Number! "+str(Number)+" is divisible by "+ str(x)
        List.append(x)
        continue
    else:
        Not_int = []
        Not_int.append(x)
        #print(str(x)+" Doesn't work")
        time.sleep(.0005)#so the computer Doesn't work super hard
        continue

print("All Divisible Whole numbers of "+str(Number)+" is "+str(List))
finish = time.time()
total_time = finish - start
print("time taken: "+str(total_time))


#os.system("say All Divisible Whole numbers of "+str(Number)+" is "+str(List))
