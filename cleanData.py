
import re

'''
Go over <in_filename> and take all samples that fit known pattern of <cat> : <review>
Translate the class to a number and write to <out_filename>
'''

in_filename = 'data.out'

out_filename = 'clean_data.out'

cat_dict = {'positive movie review' : 1, 'negative movie review' : 2}

to_write = []

with open(out_filename,'w') as out_f:

    for line in open(in_filename):
        m = re.search(r'(positive movie review|negative movie review) : (.*)',line)
        if m:
            to_write.append((str(cat_dict[m.group(1)]) + '\t' + m.group(2) + '\n'))

        if (line[:3] == '###'): # the ### symbol marks the end of generation. We remove the last generated sample since it could be cut off by the token limit. 
            to_write = to_write[:-1]

    for s in to_write:
        out_f.write(s)
            
    
