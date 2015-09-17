import csv

# save the json output as tweets.json
jsfile = file('tweets.json', 'w')
jsfile.write('[\r\n')

with open('sampletweet.txt','r') as f:
    next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')

    # get the total number of rows excluded the heading
    row_count = len(list(reader))
    ite = 0

    # back to first position
    f.seek(0)
    next(f) # skip headings

    for time,user,words in reader:

        ite+= 1

        jsfile.write('\t{\r\n')

        t = '\t\t"time": \"' + time + '\",\r\n'
        u = '\t\t"user": \"' + user + '\",\r\n'
        w = '\t\t"words": \"' + words + '\",\r\n'

        jsfile.write(t)
        jsfile.write(u)
        jsfile.write(w)

        jsfile.write('\t}')

        # omit comma for last row item
        if ite < row_count:
            jsfile.write(',\r\n')

        jsfile.write('\r\n')

jsfile.write(']')
jsfile.close()
