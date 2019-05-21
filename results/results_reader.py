import csv
import json


class ResultReader():
    def __init__(self, experiment_folder):
        self.experiment_folder = experiment_folder

    def create_average_validation_result_csv(self):
        file_path = \
            self.experiment_folder + '/average_validation_result_log.csv'

        table_rows = []
        with open(file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter='|')

            header_column = None

            for row in reader:
                if header_column is None:
                    header_column = ['date']
                    for hyp_title in json.loads(row[1]):
                        header_column.append(hyp_title)
                    header_column.append('f1_micro')
                    header_column.append('f1_macro')

                    table_rows.append(header_column)
                else:
                    table_row = []
                    table_row.append(row[0])
                    hyp_value_dict = json.loads(row[1])

                    for hyp_value in hyp_value_dict:
                        table_row.append(hyp_value_dict[hyp_value])

                    print round(float(row[2])*100, 2)

                    table_row.append(round(float(row[2])*100, 2))
                    table_row.append(round(float(row[3])*100, 2))
                    table_rows.append(table_row)

        file_path = \
            self.experiment_folder + '/average_validation_result_table.csv'
        with open(file_path, mode='w') as csv_file:
            writer = csv.writer(csv_file)

            writer.writerows(table_rows)


result_reader = ResultReader('./artist-genre/experiment_2019-05-19-02-05')
result_reader.create_average_validation_result_csv()

