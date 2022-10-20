#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
successful = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

# loop over the file
    for line in kfile:

        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
        elif "-] Authorization failed" in line:  # can ONLY be true if the "if" was false!
            successful += 1 # this is the total number of times we see this pattern


print("The number of failed log in attempts is", loginfail)

print("The number of successful log ins is", successful)

