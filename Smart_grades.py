# This is a system made to take user inputs of grades and output average (% + Letter grade)
# We need to be able to strip input of any stuff we do not want

#Plan: Get input from user, strip of jargon using regex, put numbers obtained into a dictionary [English: 98%]
#Add values in dictionary together and calculate (find number of values based on for loop)
# Correlate average % to letter grade using if statements. 
# output in string format

#Declare any libraries needed (regex)
import re
# create function that does the following:
def grade_analysis(): 
    # declare input
    user_grades = input("Please input the grades you recieved")
    # use regex to clean input to get respect grades
    db_grades = re.findall("[0-9][0-9]", user_grades)
    s_grades = re.findall("(?<!\d)\d(?=%)", user_grades) # "[0-9]"= X, ?![a-zA-Z0-9])[0-9]% = X. 
    hundred_grades = re.findall("100", user_grades)
    # use numbers in list, add them up, and calculate the average "for num in list, total_num + num" and then calculate by dividing by amount of numbers
    #Also find highest and lowest using min() and max() function

    #Associate calculated average with letter grades

    #output grades with letter
    print(hundred_grades)
    print(db_grades)
    print(s_grades)
grade_analysis()


