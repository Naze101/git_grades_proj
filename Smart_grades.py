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

    grades = [] # variable that will contain all grades
    # declare input
    user_grades = input("Please input the grades you recieved")
    # use regex to clean input to get respect grades
    db_grades = re.findall("[0-9][0-9]", grades)
    s_grades = re.findall("(?<!\d)\d(?=%)", grades) # "[0-9]"= X, ?![a-zA-Z0-9])[0-9]% = X. 
    hundred_grades = re.findall("100", grades)
    # use numbers in list, add them up, and calculate the average "for num in list, total_num + num" and then calculate by dividing by amount of numbers
    #Also find highest and lowest using min() and max() function
    #variable that numbers are collected into
    total_num = 0
    subj_num = len(grades)
    
    for num in grades:
        total_num += int(num)
    average = total_num/subj_num

    # highest numbers 
    highest_grade = max(grades)
    lowest_grades = min(grades)

    #Associate calculated average with letter grades

    #output grades with letter
    print(hundred_grades)
    print(db_grades)
    print(s_grades)
grade_analysis()


