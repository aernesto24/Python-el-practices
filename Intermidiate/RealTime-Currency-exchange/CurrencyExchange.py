"""This is a simple small currency converter from MXN to USD
Changes By: Ernesto Lopez
Base code from: https://www.geeksforgeeks.org/python-get-the-real-time-currency-exchange-rate/"""

#To obtain the currency value
def CurrencyExchangeRate(from_currency, to_currency, api_key):
    import requests 
    import json
    
    global currency_exchange_rate
    # base_url variable store base url  
    
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    
    # main_url variable store complete url 
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key
    
    #return the response object
    requested_object = requests.get(main_url)
    
    #returned object in json format, we need to parse to dictionary
    result = requested_object.json()
    #print(result)
    
    print("\n After parsing : \n Realtime Currency Exchange Rate for", 
          result["Realtime Currency Exchange Rate"] 
                ["2. From_Currency Name"], "TO", 
          result["Realtime Currency Exchange Rate"] 
                ["4. To_Currency Name"], "is", 
          result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'], to_currency,
                "last refreshed", 
                result["Realtime Currency Exchange Rate"] 
                ["6. Last Refreshed"], "UTC")
    
    currency_exchange_rate = result["Realtime Currency Exchange Rate"]["8. Bid Price"]
    
#mexican_pesos = float(input("Enter the amount of pesos to convert: "))

#usdollars = mexican_pesos * change_value
#print("You can buy ", usdollars, "for ", mexican_pesos, " MXN")

if __name__ == "__main__" :
    from_currency = 'MXN'
    to_currency = 'USD'
    api_key = 'Please claim your free API key on (https://www.alphavantage.co/support/#api-key)'
    CurrencyExchangeRate(from_currency, to_currency, api_key)
    
    print("")
    print("")
    print("***********Calculation*************")
    
    #The while loop os for keep calculating pesos to USD until you answer No
    question = True
    while question:
        
        amount_from = float(input("Enter the amount of pesos: "))
        #calculate the amount of USD and rounds to 5 decimals
        amount_to = round(amount_from * float(currency_exchange_rate), 5)
        
        #print the result
        print(amount_from, "Mexican pesos are ",amount_to, " USD")
        
        answer = input(str("Do you want to calculate another amount?: "))
    
        if answer == 'yes' or answer == 'y':
            question = True
        elif answer == 'no' or answer == 'n':
            question = False
        else:
            print("That option is not defined")
            question = False