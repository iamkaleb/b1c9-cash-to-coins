dollarAmount = 8.69

piggyBank = {
    'pennies': 0,
    'nickels': 0,
    'dimes': 0,
    'quarters': 0
}

def cash_to_coins(total):

    piggyBank['quarters'] += total // .25
    total = total % .25
    total = round(total, 2)
    piggyBank['dimes'] += total // .10
    total = total % .10
    total = round(total, 2)
    piggyBank['nickels'] += total // .05
    total = total % .05
    total = round(total, 2)
    piggyBank['pennies'] += total // .01
    total = total % .01
    total = round(total, 2)

    print(piggyBank)

cash_to_coins(8.69)



