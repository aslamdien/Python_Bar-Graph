import numpy as np
import matplotlib.pyplot as plt

marks = [70, 45, 90, 12]
names = ["Memphis", "Godwin", "Thando", "Thabo"]

mark = np.array([70, 45, 90, 12, 53, 60, 72])
name = np.array(["Memphis", "Godwin", "Thando", "Thabo", "Abdul-Malik","Uthmaan", "Ayyoob"])
plt.bar(name, mark)

x_pos = [i for i, _ in enumerate(name)] #labels on the x-axis
#labeling and visuals
plt.bar(x_pos, mark, color='green')
plt.xlabel("Names of Students")
plt.ylabel("Marks in (%)")
plt.title("Parentage of Marks in Class")
plt.xticks(x_pos, name)
plt.show()
