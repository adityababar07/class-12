import re

def dates(date):
    month = re.compile(r'\d\d\d\d\d\d\d\d')
    mo = month.search(str(date))
    # print(mo.group())
    a = mo.group()
    month = a[:2]
    day = a[2:4]
    year = a[4:]
    # print(month, day, year)
    Month = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July", "08":"August", "09":"september", "10":"October", "11":"November", "12":"December"}   
    
    print(f"{Month[month]},{day},{year}")

date = input("Enter date :\t ")
dates(date)
