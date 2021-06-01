import numpy as np
import matplotlib.pyplot as plt

test_scores = np.array([12, 99, 65, 85, 42])
test_names = np.array(["Andy", "Martin", "Zahara", "Vuyo", "Ziyaad"])
plt.bar(test_names, test_scores)

x_pos = [i for i, _ in enumerate(test_names)] #labels on the x-axis
#labeling and visuals
plt.bar(x_pos, test_scores, color='green')
plt.xlabel("Names of Students")
plt.ylabel("Scores in Tests(%)")
plt.title("Bar Graph Exercise")
plt.xticks(x_pos, test_names)
plt.show()
