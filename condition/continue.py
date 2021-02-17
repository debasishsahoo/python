##i = 0;  
##while i!=10:  
##    print("%d"%i);  
##    continue;  
##    i=i+1;  


##i=1; #initializing a local variable  
###starting a loop from 1 to 10  
##for i in range(1,11):  
##    if i==5:  
##        continue;  
##    print("%d"%i);  


list = [1,2,3,4,5]  
flag = 0  
for i in list:  
    print("Current element:",i,end=" ");  
    if i==3:  
        pass;  
        print("\nWe are inside pass block\n");  
        flag = 1;  
    if flag==1:  
        print("\nCame out of pass\n");  
        flag=0;






for i in [1,2,3,4,5]:  
    if i==3:  
        pass  
        print ("Pass when value is",i)  
    print (i),  
