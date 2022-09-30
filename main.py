import requests

your_currency = input("What is your base currency? Please input currency code only e.g usd, "
                      "eur, gbp, cad, etc \n")

# get currency rates from www.floatrates.com
url = 'https://www.floatrates.com/daily/' + str(your_currency) + '.json'
get_web = requests.get(url)
json_obj = get_web.json()

# cache popular currencies for faster conversion
cache_list = ['usd', 'eur', 'gbp']
cache_curr = {}


# Create add cache function
def add_cache():
    for curr in cache_list:
        if curr != your_currency.lower():
            cache_curr[curr] = json_obj[curr]['rate']


add_cache()

# Convert currency
ask = True
while ask:
    your_exchange_curr = input("What currency would you like to convert to? Please input currency code only e.g usd, "
                               "eur, gbp, cad, etc\n").upper()
    if len(your_exchange_curr) < 2:
        ask = False
        break
    your_amount = float(input('How much do you want to convert? \n'))
    your_exchange_curr = your_exchange_curr.lower()

    if your_exchange_curr in cache_curr.keys():
        calc = your_amount * cache_curr[your_exchange_curr]
        print('You will receive {} {}.'.format(round(calc, 2), your_exchange_curr.upper()))
    else:
        cache_list.append(your_exchange_curr)
        add_cache()
        calc = your_amount * float(json_obj[your_exchange_curr]['rate'])
        print('You will receive {} {}.'.format(round(calc, 2), your_exchange_curr.upper()))

    check_more = input(f"Would you like to check more conversions for {your_currency.upper()}? Yes/No \n").lower()

    if check_more == "yes":
        continue
    elif check_more == "no":
        print("Thank you for using this currency converter, bye now!")
        ask = False
    else:
        print("oops you enter an unexpected input. Bye now!")
        ask = False
