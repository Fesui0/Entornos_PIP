import matplotlib.pyplot as mt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [120,30,50]
    fig, ax = mt.subplots()
    ax.pie(values, labels)
    mt.savefig('chart.png')
    mt.close()
