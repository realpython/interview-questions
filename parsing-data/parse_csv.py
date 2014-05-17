import csv


class ParseCSV(object):

    def __init__(self, data):
        self.data = data

    def read_data(self):
        with open(self.data, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]
        return parsed_data

    def get_min_difference(self, parsed_data, column1, column2):
        column1_list = [x[column1] for x in parsed_data[1:]]
        column2_list = [x[column2]for x in parsed_data[1:]]
        values = [float(x) - float(y) for x, y in zip(column1_list, column2_list)]
        return values.index(min(values))

    def get_team(self, index_value, parsed_data):
        teams = [x[0] for x in parsed_data[1:]]
        return teams[index_value]