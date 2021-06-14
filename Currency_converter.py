#currency converter of 10 different countries as per current current exchange rate (6/14/2021)

print('===============================================Currency converter=====================================')

def converter(currency_value,currency_name):
    
    if currency<=1:
        print('\t','>',str(currency_value),currency_name[0:len(currency_name)-1],'in Indian rupees =',end=" ")
    else:
        print('\t','>',str(currency_value),currency_name,'in Indian rupees =',end=" ")

    if currency_name=='Dollars':
        inr_currency=round(currency*73.26,2)
    elif currency_name=='Pounds':
        inr_currency=round(currency*103.24,2)
    elif currency_name=='Canadian dollars':
        inr_currency=round(currency*60.26,2)
    elif currency_name=='Yens':
        inr_currency=round(currency*0.67,2)
    elif currency_name=='Yuans':
        inr_currency=round(currency*11.45,2)
    elif currency_name=='Euros':
        inr_currency=round(currency*88.78,2)
    elif currency_name=='Autralian dollars':
        inr_currency=round(currency*56.53,2)
    elif currency_name=='African Rands':
        inr_currency=round(currency*73.26,2)
    elif currency_name=='Dems':
        inr_currency=round(currency*45.3304,2)
    elif currency_name=='Rials':
        inr_currency=round(currency*0.0017,2)
    
    print(inr_currency, 'rupees')


    
coutries={'UK':'Pounds','USA':"Dollars",'Canada':"Canadian dollars",'Iran':'Rials','Japan':"Yens",'China':"Yuans",'Europe':"Euros",'Australia':"Autralian dollars",'South Africa':"African Rands",'Germany':"Dems"}
count=1
print('Available countries:-')
for k in coutries:
    x=str(count)+'.'+')'
    print('\t',x,k)
    count+=1

ans='Y'
while (ans!='N'):
    print()
    country_name= input('Enter country name from above whose currency you want to convert to Indian Currency :- ')
    print('\t','> Enter currency in ',coutries[country_name],end=" ")
    currency=int(input(' '))
    converter(currency,coutries[country_name])
    print()
    response=str(input("Do you want to check for other countries or other values [Y/N]:- "))
    ans=response


print('===============================================Thank You===================================================')

    
    
