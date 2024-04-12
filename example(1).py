def quantitative_method(data):

    #Calculate the mean (average) of a list of data.
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def covariance(x, y):
    #Calculate the covariance
    if len(x) != len(y):
        #Exceptions-Created my own error to suit the theorem that the variables 'x' and 'y' must have the same length
        raise ValueError("Lists x and y must have the same length.")

    #Defining variables and assigning functions unto them
    n = len(x)
    x_mean = quantitative_method(x)
    y_mean = quantitative_method(y)

    #Formula for calculating covariance
    covariance = sum((x[int] - x_mean) * (y[int] - y_mean) for int in range(n)) / (n - 1)

    return covariance

# My Own Example using :
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

covariance_result = covariance(x, y)
print(f"Covariance between x and y: {covariance_result}")
