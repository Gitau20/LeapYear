def leapyear():
    yr = int(input('Enter the year: '))

### Divide the year by 100
    if yr % 400 == 0:
        print ('Year is a Leap Year')
    elif yr % 4 and yr % 100 != 0:
        print ('Year is a Leap Year')
    else:
        print ('Year is not a Leap Year')
leapyear()