import matplotlib.pyplot as mp
import modulos as ms

def pie_plot(labels,values):
  fig, ax = mp.subplots()
  ax.pie(values, labels=labels )
  ax.axis('equal')
  mp.savefig("pie.png")
  mp.close()


if __name__ == '__main__':
  #age, population = ms.get_age_population(ms.data)
  labels, values = ms.get_column(ms.data())
  pie_plot(labels, values)


