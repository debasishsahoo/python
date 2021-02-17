##list =[1,2,3,4]  
##count = 1;  
##for i in list:  
##    if i == 4:  
##        print("item matched")  
##        count = count + 1;  
##        break  
##print("found at",count,"location");  




##str = "python"  
##for i in str:  
##    if i == 'o':  
##        break  
##    print(i);



##i = 0;  
##while 1:  
##    print(i," ",end=""),  
##    i=i+1;  
##    if i == 10:  
##        break;  
##print("came out of while loop");




n=2  
while 1:  
    i=1;  
    while i<=10:  
        print("%d X %d = %d\n"%(n,i,n*i));  
        i = i+1;  
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
    if choice == 0:  
        break;      
    n=n+1  
