#!/usr/bin/env python

"""task_02.py: Homework Task 2."""

__author__      = "Joe Graham"


keepAskingForInput = True
BP_STATUS = ""
bpNum = 0
while keepAskingForInput:
    print "Please enter your blood pressure:"
    s = raw_input()
    try:
        bpNum = int(s)
        keepAskingForInput = False
    except ValueError:
        #Invalid input.
        print "Sorry that does not look like a valid number."
        continue
    if bpNum <= 90:
        BP_STATUS = "Low"
    elif (bpNum > 90) and (bpNum <= 119):
        BP_STATUS = "Ideal"
    elif (bpNum >= 120) and (bpNum <= 139):
        BP_STATUS = "Warning"
    elif (bpNum >= 140) and (bpNum <= 160):
        BP_STATUS = "High"
    elif bpNum > 160:
        BP_STATUS = "Emergency"
    else:
        keepAskingForInput = True
        print "Invalid blood pressure range."

print "Thanks, your blood pressure is: {}".format(BP_STATUS)