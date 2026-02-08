import matplotlib.pyplot as plt

def show_chart(type_distribution):
    labels = type_distribution.keys()
    values = type_distribution.values()

    plt.bar(labels, values)
    plt.title("Equipment Type Distribution")
    plt.xlabel("Equipment Type")
    plt.ylabel("Count")
    plt.show()
