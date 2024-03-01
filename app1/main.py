import utils
## Graficando la población mundial en pie_chart

import read_csv 

import charts


def run():

  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda x: x['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)
  print(result)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


## Para manejar dualidad escrito de terminal o ejecutado desde otro archivo, 
## agregar if:
if __name__ == '__main__':
  run()