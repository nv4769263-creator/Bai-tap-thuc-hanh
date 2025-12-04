# Vương Giang Nam, mssv 245752021610085

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('test.txt,2')