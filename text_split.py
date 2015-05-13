from sys import argv

script, filename = argv

output_file_name = filename.split('.')[0] + '_two_column.csv'
lines = []
row_count = 0

# This is where you change it.
line_delimiter = ';'
row_delimiter = ','

txt = open(filename)

file_raw = open(filename)
lines = file_raw.read().split(line_delimiter)

print "Here's your file %r:" % filename
print len(lines)
output_file = open(output_file_name, 'w')

for line in lines:
    row_count += 1
    columns = line.split(row_delimiter)
    for column in columns:
        print >>output_file, "%d,%s" % (row_count, column)


print "Output file is %r" % output_file_name
output_file.close()
