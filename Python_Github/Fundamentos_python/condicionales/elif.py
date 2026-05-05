monthly_income = 72000
monthly_expense = 8000
# if aninados y else if (elif)
if monthly_income > 12500:
    if monthly_income - monthly_expense < 0:
        print('Estas en deficit')
    elif monthly_income - monthly_expense > 8000:
        print('Estas bien')
    else:
        print('Hay que ver si te alcanza')   
elif monthly_income > 5000:
    print('Eres millonario')
elif monthly_income > 3000:
    print('Eres un ciudadano promedio')
else:
    print('Eres pobre')