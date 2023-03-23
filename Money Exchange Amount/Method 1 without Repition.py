#--- Create Variables ---
amount=0 #--->User input value
usd_in_lkr=200 #--->Worth of USD in LKR
w=" " #--->User option 1
c=0 #--->User option 2
output=" " 
conversion=" "
valid_amount=" "
k=0 
l=0 
a=" "

valid_amount="Yes"
    
#--- Get the amount ---
amount=int(input("Please enter your amount less than Rs.100,000 without decimals: Rs.")) #--->User should enter an amount less than 100,000 and has no decimals.
    
#--- Check the amount validity ---
if ( amount>=100000 ):
    print("\n\t! ! ! E R R O R ! ! ! \n \nPlease enter amount less than Rs.100,000.")#--->If user enter more than 100,000 ,then user will get an ERROR message.
    valid_amount="No"
elif ( amount == 0 ):
    print("\n\t! ! ! E R R O R ! ! ! \n \nPlease enter amount greater than Rs.0\n.")#--->If user enter 0 ,then user will get an ERROR message
    valid_amount="No"
    
# --- Calculate and display output only if values are valid ---
if ( valid_amount == "Yes" ): #--->If user inputs are valid , then user can continue.
    conversion=input("Please enter your option ( to convert to word representation enter 'w' / to convert to USD currency enter 'c' ):") #--->User should choose the output method (in word representation or in USD).
        
    #--- If user choose USD currency,---
    if ( conversion == "c" ):
        output=round((amount/usd_in_lkr),0)
        print("\nRs.",amount,"convert to USD = USD",int(output))
            
    #--- If user choose word representation,---
    elif ( conversion == "w" ):
        def amount_to_word(amount):
            a = { 0 : 'zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', \
                  6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten', \
                  11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen', \
                  15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen', \
                  19 : 'Ninteen', 20 : 'Twenty', \
                  30 : 'Thirty', 40 : 'Fourth', 50 : 'Fifty', 60 : 'Sixty', \
                  70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninty' }
            k= 1000
            l = k * 100

            if ( amount < 20 ): #--->If user amount is less than 20.
                return (a[amount])

            elif ( amount < 100 ): #--->If user amount is less than 100.
                if ( amount % 10 == 0 ): #--->If remainder is "0" when amount divide by 10.
                    return (a[amount])
                else:
                    return (a[amount // 10 * 10] + ' ' + a[amount % 10]) #--->If remainder is not "0" when amount divide by 10.

            elif ( amount < k ): #--->If user amount is less than 1000.
                if ( amount % 100 == 0 ):
                    return a[amount // 100] + " Hundred" #--->If remainder is "0" when amount divide by 100.
                else:
                    return (a[amount // 100] + " Hundred " + "and " +amount_to_word(amount % 100)) #--->If remainder is not "0" when amount divide by 100.
            elif ( amount < l ): #--->If user amount less than 100,000.
                if ( amount % k == 0 ):
                    return amount_to_word(amount // k) + " Thousand" #--->If remainder is "0" when amount divide by 1000.
                else:
                    return amount_to_word(amount // k) + " Thousand, " + amount_to_word(amount % k) #--->If remainder is not "0" when amount divide by 1000.

        output=(amount_to_word(amount))
        print("\nRs.",amount,"convert to word representation=",output)
            
#--- If user enter invalid inputs ---
    elif ( conversion!="w" or "c" ):
        print("\n\t ! ! ! E R R O R ! ! ! \n \nCouldn't calculate due to invalid inputs.\n \nPlease try again with valid inputs.") #--->If user enter invalid inputs.
else:
    print("\nPlease try again with valid amount.") #--->If user enter invalid inputs.
        
#--- End ---

    
