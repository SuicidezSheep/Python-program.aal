""" Problem: Create a program that ask the user to enter their name and age and calculate and print how many seconds,
    minutes, hours, days, weeks, months and years that person is alive"""

# 365 + 1 = 366 days if we include the leap yr

# Global variables and its value 
seconds_per_yr = 31622400       #total seconds per yr
minutes_per_yr = 527040         # total minutes per yr
hours_per_yr = 8784             # total hours per yr
days_per_yr = 366               # total days per yr
weeks_per_yr = 52.285714285714  #total weeks per yr
months_per_yr = 52.286          #total months per yr
years_per_yr = 1                # total year per yr

def main(): # main function of the program 

    user_name = str(input("Enter user name: ")) # ask the user to input their name
    user_age = int(input("Enter user age: "))   # ask the user to input their age
    calculate(user_name, user_age)              #call the function 

def calculate(user_name, user_age): # this function responsible of calculating the exact old of the user

    """from the seconds_alive variable to years_alive variable, you all need to do is to create a vara
        minutes_alive = minutes_per_yr * user_age
    """ 
    seconds_alive = seconds_per_yr * user_age
    minutes_alive = minutes_per_yr * user_age
    hours_alive = hours_per_yr * user_age
    days_alive = days_per_yr * user_age
    weeks_alive = weeks_per_yr * user_age
    months_alive = months_per_yr * user_age
    years_alive = years_per_yr * user_age
    result(seconds_alive, minutes_alive, hours_alive, days_alive, weeks_alive, months_alive, years_alive, user_name)
    
def result(seconds_alive, minutes_alive, hours_alive, days_alive, weeks_alive, months_alive, years_alive, user_name): # funtion for displaying the result

    # just print all the variable that are used to stored the value of those two variables
    print("-----Hi,",user_name,"you lived a total of",seconds_alive,"seconds,",minutes_alive,"minutes alive,",hours_alive,"hours,",
          days_alive,"days,",weeks_alive,"weeks,",months_alive,"months,",years_alive,"years old.-----")

main()