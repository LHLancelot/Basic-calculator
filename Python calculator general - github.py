
from datetime import datetime, date

def calculate():
    option = input('''
1 Percentage of value
2 Percentage Change
3 Age Calculator
4 Frenheit to Celcius
5 Celcius to Farenheit
6 Half-Life: Mass amount of the original isotope
''')

    if option == '1':
        va1 = int(input("Total > "))
        va2 = int(input("Amount > "))
        i2 = (va2/va1)*100
        print(round(i2), "%")

    elif option == '2':
        v1 = int(input("Original Value > "))
        v2 = int(input("New Value > "))
        i = ((v2-v1)/v1)*100
        print(round(i), "%")

    elif option == '3':
        print("What is your date of birth (dd mm yyyy)? > ")
        date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")
        age = calculate_age(date_of_birth)

        if age < 18:
            print("Candidate is not old enough to work with us yet - they are", age)
        elif age > 17:
            print("The candidate is", age)

    elif option == '4':
        f1 = int(input("Degrees in Celcius > "))
        f2 = f1 * 1.8 + 32
        print (round(f2,2), "°F")

    elif option == '5':
        c1 = int(input("Degrees in Celcius > "))
        c2 = (5/9) * (c1-32)
        print (round(c2,2), "°F")

    elif option == '6':
        hl1 = int(input("Amount fo material(g) > "))
        hl2 = float(input("Time (hrs) > "))
        hl3 = (1/pow(2,hl2))*hl1
        print ("Amount of material left after", hl2,"hours, is ", round(hl3,2), "g")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Another calculation? Y / N
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Ciao!')
    else:
        again()

calculate()

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))