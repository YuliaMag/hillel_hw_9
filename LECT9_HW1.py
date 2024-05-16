import re

rex = r"[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z|0-9]{2,7}"


def val_email(email):
    if re.fullmatch(rex, email):
        print(True)
    else:
        print(False)


email = input("Email Address: ")

val_email(email)

# ================================================ #
# TC "True":
# test@test.com
# t3st@t1st.c0m -- for "symbols except '@' and '.' should be letters and decimal digits"
# 111@qqq.77 -- for "symbols except '@' and '.' should be letters and decimal digits"

# TCs "False":
# test.test@com
# test@@test@com
# test.test.com
# test.test..com
# testtestcom
# ^%&!#$%^&*()_+><?
# ^%&test
# &*^@(*&.%$
# @test.
# @test
# test.
# test.@test
# test@.test
