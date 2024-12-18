def get_name(prompt):
    return input(prompt).strip()


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print('Error. Please enter a positive number.')
        except ValueError:
            print('Error. Please enter a real number.')

def get_age():
    while True:
        age = get_positive_int('\nAge: ')
        if age < 100:
            return age
        print('Invalid Age. Please try again')


def get_birthdate():
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    while True:
        birthdate_input = input('\nBirthdate (MM, dd, YY): ')
        try:
            month, day, year = map(str.strip, birthdate_input.split(','))
            day, year = int(day), int(year)
            if month in month and 1 <= day <= 31:
                return month, day, year
            print('Invalid Date. Please try again')
        except ValueError:
            print('Error. Please enter in format.')


def get_gender():
    while True:
        gender = input('\nGender: ').strip().upper()
        if gender in ['M','F']:
            return gender
        print('Invalid Gender. Please try again')


def get_height():
    while True:
        height = get_positive_int('\nHeight: ')
        unit = input('Cm / Feet: ').strip().upper()
        if unit == 'CM':
            height_in_feet = height / 30.48
            return f'Your height in Feet: {height_in_feet:.2f} feet'
        elif unit == 'FEET':
            height_in_cm = height * 30.48
            return f'Your height in Cm: {height_in_cm:.2f} cm'


def get_weight(): 
    while True:
        weight = get_positive_int('\nWeight: ')
        unit = input('Kg / Lbs: ').strip().upper()
        if unit == 'KG':
            weight_in_lbs = weight * 2.205
            return f'Your weight in Lbs: {weight_in_lbs:.2f} lbs'
        elif unit == 'LBS':
            weight_in_kg = weight / 2.205
            return f'Your weight in Kg: {weight_in_kg:.2f} kg'


def main():
    print('Personal Data:')

    first_name = get_name('\nFirst Name: ')
    second_name = get_name('Middle Initial: ')
    third_name = get_name('Last Name: ')

    age = get_age()
    month, day, year = get_birthdate()
    gender = get_gender()
    height = get_height()
    weight = get_weight()

    print('\nData Result:')
    print(f'Name: {first_name} {second_name} {third_name}')
    print(f'Age: {age}')
    print(f'Birthdate: {month} {day} {year}')
    print(f'Gender: {gender}')
    print(f'Height: {height}')
    print(f'Weight: {weight}')

if __name__ == '__main__':
    main()