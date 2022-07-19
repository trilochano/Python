# The assert Statement
# Syntax : assert Expression[, Arguments]

# def ageValidation(age):
#     assert (age >= 18), "Not eligible to vote"
#     return age


# print(ageValidation(18))
# print(ageValidation(5))


def ageValidation(age):
    try:
        assert (age >= 18), "Not eligible to vote"
    except AssertionError as e:
        print(e.args)
    return age


# print(ageValidation(18))
print(ageValidation(5))

