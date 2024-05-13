import re

rex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


def val_email(email=input("Email Address: ")):
    if re.fullmatch(rex, email):
        print(True)
    else:
        print(False)


val_email()

# ================================================ #
# TC "True":
# test@test.com

# TCs "False":
# test.test@com
# test@@test@com
# test.test.com
# testtestcom
# ^%&!#$%^&*()_+><?
# ^%&test
# &*^@(*&.%$
# @test.
# @test
# test.
# test.@test
# test@.test
