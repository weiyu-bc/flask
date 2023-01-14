import csv


def read_csv_file(file):
    """
    读取csv-file，返回多个文件内容列表。
    :param file: csv-file
        id      discord     nc-id
        123     Haitao      ddd
        983     Tianqing    dd
    :return: tuple list
        (['123','983'], ['Haitao','Tianqing'], ['ddd','dd'])
    """
    in_id_list = []
    discord_list = []
    farm_id_list = []
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        
        # skip the header
        next(csv_reader)
        
        for line in csv_reader:
            in_id_list.append(line[0])
            discord_list.append(line[1])
            farm_id_list.append(line[2])
            #print(line)

        return (in_id_list, discord_list, farm_id_list)


def read_csv_file_get_list(file):
    """
    读取csv-file，返回一个文件内容列表。
    :param file: csv-file
        id      discord     nc-id
        123     Haitao      ddd
        983     Tianqing    dd
    :return: tuple list
        [('Haitao','123','ddd'), ('Tianqing','983','dd')]
    """
    user_list = []
    with open(file, 'r', encoding="utf-8") as f:
        csv_reader = csv.reader(f)

        # skip the header
        next(csv_reader)

        for line in csv_reader:
            user_list.append((line[1], line[0], line[2]))

        return user_list


if __name__ == '__main__':
    x = read_csv_file('test_id.csv')
    print(x)
