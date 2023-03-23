#---Create Variables---
amount=0 #--->User input value
usd_in_lkr=200 #--->Worth of USD in LKR
w=" " #--->User option 1
c=0 #--->User option 2
output=0 
conversion=" "
need_to_continue=" " 
valid_amount=" "
num_1=0
num_2=0
num_3=0
num_4=0
num_5=0
digits=" "
tens=" "
and_tens=" "
teens=" "
and_teens=" "
hundred=" "
thousand=" "

#--- Process ---
valid_amount="Yes"
    
#--- Get the amount ---
amount=int(input("Please enter the amount less than Rs.100,000 without decimals: Rs.")) #--->User should enter an amount less than 100,000.
    
#--- Check the amount validity ---
if ( amount>100000 ) :
    print("\n\t! ! ! E R R O R ! ! ! \n \nPlease enter amount less than Rs.100,000.")#--->If user enter more than 100,000 ,then user will get an ERROR message.
    valid_amount="No"
elif ( amount == 0 ) :
    print("\n\t! ! ! E R R O R ! ! ! \n \nPlease enter amount greater than Rs.0.")#--->If user enter 0 ,then user will get an ERROR message
    valid_amount="No"
    
#--- Calculate and display output only if values are valid ---
if ( valid_amount == "Yes" ) : #--->If user inputs are valid , then user can continue.
    conversion=input("Choose your option ( to convert to word representation enter 'w' / to convert to USD currency enter 'c' ):") #--->User should choose the output method (in word representation or in USD).
        
    #--- If user choose USD currency,---
    if ( conversion == "c" ) :
        output=round((amount/usd_in_lkr),0)
        print("\nRs.",amount,"convert to USD =","USD",int(output))
            
    #--- If user choose word representation,---
    elif ( conversion == "w" ):
            
        digits=[" ","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        tens=[" ","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        and_tens=[" ","and Ten","and Twenty","and Thirty","and Fourty","and Fifty","and Sixty","and Seventy","and Eighty","and Ninety"]
        teens=[" ","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]
        and_teens=[" ","and Eleven","and Twelve","and Thirteen","and Fourteen","and Fifteen","and Sixteen","and Seventeen","and Eighteen","and Ninteen"]
        hundred=[" ","One Hundred","Two Hundred","Three Hundred","Four Hunded","Five Hundred","Six Hundred","Seven Hundred",
                 "Eight Hundred","Nine Hundred"]
        thousand=[" ","One Thousand","Two Thousand","Three Thousand","Four Thousand","Five Thousand","Six Thousand","Seven Thousand",
                  "Eight Thousand","Nine Thousand"]

        #--- If user amount is  between 0 and 100 ---

        if ( 11 <= amount <= 19 ) :
                
            num_1 = ( amount % 10 )
                
            print("\nRs.",amount,"convert to word representation =",teens[num_1])

        elif ( amount < 100 ) :
                
            num_1 = ( amount // 10 )
            num_2 = ( amount % 10 )
                
            print("\nRs.",amount,"convert to word representation =",tens[num_1],digits[num_2])
                
        #--- If user amount is  between 100 and 1,000 ---
        elif ( 100 <= amount < 1000 ) :
                
            num_1 = ( amount // 100 )
            num_2 = ( ( amount % 100 ) % 10 )
            num_3 = ( ( amount % 100 ) // 10 )
                
            if (10<amount%100<20):
                print("\nRs.",amount,"convert to word representation =",hundred[num_1],and_teens[num_2])
            else:
                print("\nRs.",amount,"convert to word representation =",hundred[num_1],and_tens[num_3],digits[num_2])

        #--- If user amount is  between 1,000 and 10,000 ---
        elif ( 1000 <= amount < 10000 ) :
                
            num_1 = ( amount // 1000 )
            num_2 = ( ( amount % 1000 ) // 100 )
            num_3 = ( ( ( amount % 1000 ) % 100 ) // 10 )
            num_4 = ( ( ( amount % 1000 ) % 100 ) % 10 )
                
            if ( 10 < ( amount % 1000 %100 ) < 20 ) :
                print("\nRs.",amount,"convert to word representation =",thousand[num_1],hundred[num_2],and_teens[num_3])
            else:
                print("\nRs.",amount,"convert to word representation =",thousand[num_1],hundred[num_2],and_tens[num_3],digits[num_4])
                        
        #--- If user amount is between 10,000 and 100,000 ---
        else :
                
            num_1 = ( ( amount // 1000 ) // 10 )
            num_2 = ( ( amount // 1000 ) % 10 )
            num_3 = ( ( amount % 1000 ) // 100 )
            num_4 = ( ( ( amount % 1000 ) % 100 ) // 10 )
            num_5 = ( ( ( amount % 1000 ) % 100 ) % 10 )
                
            if ( 10 < ( amount // 1000 ) < 20 ) :
                if ( 10 < ( amount % 1000 % 100 ) < 20 ) :
                    print("\nRs.",amount,"convert to word representation =",teens[num_2],"Thousand",hundred[num_3],and_teens[num_2])
                else :
                    print("\nRs.",amount,"convert to word representation =",teens[num_2],"Thousand",hundred[num_3],and_tens[num_4],digits[num_5])
            else:
                if ( 10 < ( amount % 1000 % 100 ) < 20 ) :
                    print("\nRs.",amount,"convert to word representation =",tens[num_1],digits[num_2],"Thousand",hundred[num_3],and_teens[num_2])
                else:
                    print("\nRs.",amount,"convert to word representation =",tens[num_1],digits[num_2],"Thousand",hundred[num_3],and_tens[num_4],digits[num_5])
                
            
    #--- If user enter invalid inputs ---
    elif ( conversion!="w" or "c" ) :
        print("\n\t ! ! ! E R R O R ! ! ! \n \nCouldn't calculate due to invalid inputs.\n \nPlease try again with valid inputs.") #--->If user enter invalid inputs.
else:
    print("\nPlease try again with valid amount.") #--->If user enter invalid inputs.
        
#--- END ---
    
