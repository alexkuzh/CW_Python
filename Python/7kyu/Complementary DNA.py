# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
def DNA_strand(dna):
    # code here
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([d[x] for x in dna])

print(DNA_strand('GTAT'))