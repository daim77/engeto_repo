def bmi(weight, height):
    bmi = round(weight / height ** 2, 1)
    if bmi >= 35:
        return 'extremly obese'
    elif bmi >= 30:
        return 'obese'
    elif bmi >= 25:
        return 'overweight'
    elif bmi >= 18.5:
        return 'normal'
    else:
        return 'underweight'


if __name__ == '__main__':
    print(bmi(80, 1.80))
