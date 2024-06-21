import read_csv as rc


def get_country(Country, path):
  data = rc.read_csv(path)
  filtered_data = list(filter(lambda iter:iter['Country/Territory'] == Country , data))
  return filtered_data

def data():
  path = '/home/joseph/home/Documentos/Programación/Entornos_PIP/charts/csv/data.csv'
  data = rc.read_csv(path)
  return data
  
def get_age_population(filtered_data):
  if not filtered_data:
      return {}
  population_dict = {key[0:4]: int(value) for key, value in filtered_data[0].items()if key.endswith(' Population')}
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def get_column(data):
  filter_column_ = {item['Country/Territory']: float(item['World Population Percentage']) for item in data}
  labels = filter_column_.keys()
  values = filter_column_.values()
  return labels, values

  
if __name__ == '__main__':
  path = '/home/joseph/home/Documentos/Programación/Entornos_PIP/charts/csv/data.csv'
  data_ = data()
  get_column_ = get_column(data_)
  print(get_column_)

