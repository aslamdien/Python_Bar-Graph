import matplotlib.pyplot as plt

sizes = [25, 20, 45, 10]
labels = ["Cats", "Dogs", "Tigers", "Goats"]

plt.pie(sizes, labels = labels, autopct= "%.2f") # float and persentagevalue
plt.show()
