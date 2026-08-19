# ============================================================
# CUSTOM EXCEPTION
# ============================================================
# We can create our own exception class by inheriting
# from the built-in Exception class.
# ============================================================


class InvalidAgeError(Exception):
    pass


def check_age(age):

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Age is valid.")


try:
    check_age(15)

except InvalidAgeError as error:
    print(error)