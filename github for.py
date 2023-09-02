import matplotlib.pyplot as mt
import math as m
import numpy as np
import time as t
print('BY MOKSH')
#ifeet = 2.5 cm
#60 sec = 1 min 
#dollar to rs
#ENTER THE amount cgst and sgstamount = price+cgst+sgst
#DISCOUNT
w= str.upper(input('''which mode you wnna choose following are the optinons:
                   1. Physical conversion 
                   2. Mahematical conversions (or MC)
                   3. Economic Conversions
                   4. Health Related issue
                    *for more info about each topic write Info(topic name)* 
                    Which one you want to choose:'''))

if w=="MATHEMATICAL CONVERSIONS" or "MC":
    x= str.upper(input('''ENTER WHAT YOU WANNA GO FOR, WE HAVE FOLLOWING OPTIONS AVAILABLE CURRENTLY;
                       1. DISTANCE BETWEEN TWO COORDINATES (or DBTC)
                       Which one you want to choose:'''))
    if x== "DISTANCE BETWEEN TWO COORDINATES" or "DBTC":
        v= int(input("so what is the x coordinate of first point:"))
        c= int(input("Okk so what is the y coordinate of first point:"))
        k= int(input("so what is the x coordinate of second point:"))
        l= int(input("Okk so what is the y coordinate of second point:"))
        g= int( k-v)
        f= int(l-c)
        d= int(g+f)
        v= str.upper(input("hmm so you really wanna to find distance between them:"))
        if v== "YES":
            print ( m.sqrt(d) )
            l= str(type(d))
        
        if l != "<class 'int'>":
                print("sorry the distance is not real and we dont deal with imaginory stuff here")
        
        else:
            
            x= str.upper(input("YOU WANT TO SEE IT IN A GRAPH?"))
            if x== "YES":
                d= [v,k]
                f= [c,l]
                mt.plot(d, f)
                mt.show()
                
            else :
                print("ok")
            
            
elif w== 'PHYSICAL CONVERSION':
    x = str.upper(input("from what to what you wanna convert and to what"))
            
    if x=="FEET TO CENTIMETERS":
        v= bool(input("so you really wanna convert"))
        if v==1 :
            n= int(input("so how much FEET you wanna convert to CENTIMETERS"))
            m= bool(input("so you really wanna convert"))
            if m==1 :
                print(n*2.5)
    elif x=="FROM CENTIMETERS TO INCHES":
        v= bool(input("so you really wanna convert"))
        if v==1 :
            n= float(input("so how much RUPEES you wanna convert to DOLLAR"))
            m= bool(input("so you really wanna convert"))
            if m==1 :
                print(n/2.5)
    elif x=="FROM SECOND TO MINUTES":
        v= bool(input("so you really wanna convert"))
        if v==1 :
            n= int(input("so how much SECONDS you wanna convert to MINUTES"))
            m= bool(input("so you really wanna convert"))
            if m==1 :
                print(n/60)
    elif x=="FROM MINUTE TO SECOND":
        v= bool(input("so you really wanna convert"))
        if v==1 :
            n= int(input("so how much MINUTES you wanna convert to SECONDS"))
            m= bool(input("so you really wanna convert"))
            if m==1 :
                print(n*60)
    elif x== "F TO C":
        v= int(input("how much ferenhite you want to convert to celcius"))
        t.sleep(2)
        print("it will have ", -17.222222*v , '\N{DEGREE SIGN}')
        
                
elif w== "ECONOMIC CONVERSIONS":
    print('''HERE YOU HAVE FOLLOWING CONVERSION OPTIONS:
          1. CALCULATE CGST AND SGST
          2. FROM DOLLAR TO RUPEES
          3. FROM RUPEES TO DOLLAR
          4. SIMPLE AND COMPOUND INTREST
          5. MORE COMMING SOON......''')
    r= str.upper(int("SO WAHT YOU WANT TO FIND (YOU CAN ENTER NUMBERS"))
    if r=='CALCULATE CGST AND SGST' or "1":
        l= float(input("over what amount you wnat to find you cgst and sgst tax"))
        m=bool(input("so you really wanna see your final amount"))
        if m==True:
            print("sorry my period is over i will try to complete this program tomorrow ")
    if x=="FROM DOLLAR TO RUPEES" or "2":
        v= bool(input("so you really wanna convert"))
        if v==1 :
            n= int(input("so how much dollars you wanna convert to rupees"))
            m= bool(input("so you really wanna convert"))
            if m==1 :
                print(n*87)
    elif x=="FROM RUPEES TO DOLLAR" or "3":
        v= bool(input("so you really wanna convert"))
        if v==1 :
            n= int(input("so how much RUPEES you wanna convert to DOLLAR"))
            m= bool(input("so you really wanna convert"))
            if m==1 :
                print(n/87)
    elif x== 'SIMPLE AND COMPOUND INTREST' or "4":        #simple compound intrest    
        print("here you can find compound and simple intrest:")
        l= float(input("SO WHAT IS THE PRINCIPLE AMOUNT ON YOUR INTREST:"))
        k= list(input('''OKK SO WHATS THE TIME FOR WHICH THE INTREST IS TO BE FOUND
                       ** PLEASE WRITW IT IN THE FORM OF MAGNITUDE <UNIT>'''))
        j= float('''and whats the rate: 
                    ** write without % sign''')
        h= str.upper('''SO WHICH INTREST YOU WANNA FIND:
                        1. SIMPLE INTREST
                        2. COMPOUND INTREST
                         *** YOU CAN WRITE NUMBERS''')
        if h== "COMPOUND INTREST":
            

elif w== "HEALTH RELATED ISSUE" or "HRI" or "4":
    print("Here you can check if your temprature is healthy or not")
    k= input("enter your temprature (it will be appriciaated if you write in format magnitude<space>unit)")
    l= k.split()
elif w=="INFO(MATHEMATICAL CONVERSION)":                    #information
    print('''SURE HERE ARE THE INFO
          WE HAVE FOLLOWING OPTIONS AVAILABLE CURRENTLY;
                             1. DISTANCE BETWEEN TWO COORDINATES (or DBTC)''')
