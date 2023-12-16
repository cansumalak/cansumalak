
# THIS FILE FOR CREATING DICTIONARY VARIABLE CALLED MYINFO WHICH INCLUDES MY FIRST-LAST NAME, BIRTY YEAR-MONTH-DAY TO CALCULATE THE NUMBER OF THE SECONDS I AM ALIVE WHEN CALLING THIS SCRIPT
# IT ALSO CREATES TXT FILE CALLED "MALAK_CANSU_myInfo.txt" WHICH INCLUDES CONTENTS OF THE VARIABLE MYINFO

# I am importing time function here to use it later for calculating the number of seconds that I have been alive
import time

# Here, I am creating dictionary called myInfo
myInfo = {}

#  Adding first name, last name, birth (year.month,day) to dictionary -- two strings-three numbers
myInfo['FirstName'] = 'Cansu'
myInfo['LastName'] = 'Malak'
myInfo['BirthYear'] = 1998
myInfo['BirthMonth'] = 12
myInfo['BirthDay'] = 15


# Calculating the time difference between the current moment and date of birth. Epoch is January 1, 1970, at 00:00:00 (midnight) UTC
seconds = time.time()

# I am using time.mktime() function to convert the date of birth into seconds since the epoch. 
# Because it takes a time tuple representing a date and time and converts it to the number of seconds since the epoch.
birth_seconds = time.mktime((myInfo['BirthYear'], myInfo['BirthMonth'], myInfo['BirthDay'], 0, 0, 0, 0, 0, 0))

# NOTE: why there is 000000? : Those zeros in time.mktime() correspond to the time components not provided in the date of birth, and they are set to zero.
# Considering the time of birth as the start of the day at midnight (00:00:00) on the specified date, focusing on the entire day rather than a particular time.
# So, first three elements represent the year, month, day and the rest are set to zero as we are interested in the entire day.

# Now I am calculating age in seconds
age_seconds = seconds - birth_seconds

# Adding age in seconds to myInfo dictionary
myInfo['age_seconds'] = age_seconds  # this will show the number of the seconds that I have been alive


# Displaying age in seconds
print(f"At the time of calling this script, I was {(age_seconds)} seconds old.")

# Opening the file in write mode
f = open("MALAK_CANSU_myInfo.txt", "w")

# Write information to the file
f.write(f"First Name: {myInfo['FirstName']}\n")
f.write(f"Last Name: {myInfo['LastName']}\n")
f.write(f"Date of Birth: {myInfo['BirthYear']} / {myInfo['BirthMonth']} / {myInfo['BirthDay']}\n")
f.write(f"Age in Seconds: {myInfo['age_seconds']} seconds\n")

# Close the file
f.close()


