#! python3


# %%
def get_sql_data(file_name):
    """"""
    sql_data = open(file_name, 'rb')
    return sql_data


# %%
def data_to_text(data, output):
    """"""
    with open(output, 'w') as file:
        for line in data.readlines():
            file.write(str(line))
