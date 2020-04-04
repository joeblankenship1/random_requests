query = open('/tmp/enwiki-latest-category.sql', 'rb')

with open('/tmp/test.txt', 'w') as file:
    for line in query.readlines():
        file.write(str(line))

