def verifyAge(age):
    try:
        assert (age >= 18), "Not eligible to vote"
        return int(age)
    except(TypeError, AssertionError) as e:
        print(e.args)


verifyAge(12)
verifyAge("123")
