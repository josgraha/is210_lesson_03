#!/usr/bin/env python

"""task_01.py: Homework Task 1."""

__author__      = "Joe Graham"

QUESTION_01 = ""

print "Please enter your name:"
#Capture the value from Question 01.
QUESTION_01 = raw_input()

keepAskingForInput = True
QUESTION_02 = 0
while keepAskingForInput:
    print "Please enter your age (in years):"
    s = raw_input();
    try:
        QUESTION_02 = int(s)
        keepAskingForInput = False
    except ValueError:
        #Invalid input.
        print "Sorry that does not look like a valid number."

print "Thanks {}, your age is: {}".format(QUESTION_01, QUESTION_02)