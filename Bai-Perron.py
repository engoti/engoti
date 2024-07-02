import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt

data = np.array([
    [1990, 1.2, 0.5],
    [1991, 1.5, 0.7],
    [1992, 1.8, 0.8],
    [1993, 2.0, 1.0],
    [1994, 2.2, 1.1],
    [1995, 2.5, 1.3],
    [1996, 2.7, 1.4],
    [1997, 3.0, 1.6],
    [1998, 3.2, 1.8],
    [1999, 3.5, 2.0],
    [2000, 3.7, 2.2],
    [2001, 4.0, 2.4],
    [2002, 4.2, 2.5]
])

years = data[:,0]
y = data[:, 1]
x = data[:, 2]

plt.figure(figsize=(10, 6))
plt.plot(years, y, marker='o', label = 'y')
plt.plot(years, x, marker='x', label = 'x')
plt.title('Time Series Data')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.show()



# Define the Model

model = "l2"
algo = rpt.Binseg(model=model).fit(y)
result = algo.predict(n_bkps=2)

rpt.display(y, result)
plt.title("Detected Breakpoints in y")
plt.xlabel("Time")
plt.ylabel("y")
plt.show()


print("Detected breakpoints:", result[:-1])
