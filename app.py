
import matplotlib.pyplot as plt
import numpy as np

# x_list = [1, 2, 3, 4, 5, 6, 7]
# y_list = [50.0, 49.8, 49.5, 49.6, 49.0, 49.7, 49.5]

# plt.title("Weight change chart for the last 7 days", fontsize=14, fontweight="bold", color="blue")
# plt.xlabel('time', fontsize=12, color="black")
# plt.ylabel('kg', fontsize=12, color="black")
# plt.plot(x_list, y_list, label="kg")
# plt.legend()
# plt.grid
# plt.show()

# Data for plotting
t = ["25.10", "26.10", "27.10", "28.10", "29.10", "30.10", "01.11"]
s = [49.0, 49.3, 49.5, 49.6, 49.1, 49.7, 49.5]

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (d)', ylabel='weight (kg)',
       title='Weight change chart for 7 days')
ax.grid()

fig.savefig("test.png")
plt.show()