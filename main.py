import pandas
# with open('weather_data.csv', mode='r') as weather_data:
#     data = weather_data.readlines()
    
# import csv

# with open('weather_data.csv', mode='r') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv('Squirrel_Data.csv')
fur_color = data['Primary Fur Color']
fur_list = fur_color.to_list()
black = fur_list.count('Black')
cinnamon = fur_list.count('Cinnamon')
gray = fur_list.count('Gray')

fur_table = {
    'Color': ['Black', 'Cinnamon', 'Gray'],
    'Number': [black, cinnamon, gray]
}

df = pandas.DataFrame(fur_table)
df.to_csv('Squirrel_Count.csv')