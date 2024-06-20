import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [120, 30, 50]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('chart.png')
    plt.close()
