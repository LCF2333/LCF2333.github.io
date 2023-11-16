#CSD=1133-01
#Assignment 5
#Desmond Timperley
#Oct 19, 2023


print('Programming Exercies-------------------------------------------------------------------')

print()

print('1. Bug Collector-----------------------------------------------------------------------')
#Named constants
BUG_TOTAL = 0
BUG_DAY = 0


#while loop
while BUG_DAY < 5:
    BUG_DAY += 1
    bug_caught = int(input('Enter the amount of bugs caught on day ' + str(BUG_DAY) + ': ' ))
    BUG_TOTAL = bug_caught + BUG_TOTAL 

#print statements 
print('The total amount of bugs caught in 5 days is:',BUG_TOTAL)

print()

print('5. Average Rainfall--------------------------------------------------------------------')

#named constants 
NUM_YEAR = 0
MONTH = 12
RAIN_TOTAL = 0
RAIN_AVG = 0

#user input
NUM_YEAR = int(input('Please enter the amount of years you would like to caculate the AVG rainfall: '))

#for loop
for year in range(1, NUM_YEAR + 1):
    for month in range(1, 13):
        rain_fall = int(input('Enter the amount of rain in inches per month ' + str(month) + ':'))
        RAIN_TOTAL = rain_fall + RAIN_TOTAL

#caculations/print statement 
total_months = NUM_YEAR * 12 
RAIN_AVG = RAIN_TOTAL / total_months
print('AVG Rainfall:', format(RAIN_AVG, '.2f' ), 'Inches')

print()

print('6. Celsius to Fahrenheit Table----------------------------------------------------------')

#named constant 
CELSIUS = 1

#while loop/print statement
while CELSIUS < 21:
    fahrenheit = 9/5*CELSIUS + 32
    print('-------------------------')
    print(CELSIUS,'C = ', format(fahrenheit, '.2f'), 'F', sep='')
    CELSIUS += 1 

