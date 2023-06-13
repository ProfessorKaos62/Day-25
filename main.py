import pandas

# data = pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data['temp'].to_list()
# print(data['temp'].max())

# Monday = data[data.day == 'Monday']
# print((Monday.temp * 9/5) + 32)

# day_of_max = data[data.temp == data.temp.max()]
# print(day_of_max)

data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 89, 69]
}

data = pandas.DataFrame(data_dict)

data.to_csv('student_scores.csv')
