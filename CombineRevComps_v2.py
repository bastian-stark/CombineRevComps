#CombineRevComps V2
#Bastian Stark
#May 31, 2024
#Short script that parses through the hexamer sequence counts from a txt file and combines counts belonging to reverse complement sequences

#function for reverse complementing an input sequence
def revComp(seq):
    nucComps = {"A": "T", "T": "A", "G": "C", "C": "G"}
    newSeq = []
    for nuc in seq:
        for key in nucComps:
            if nuc == key:
                newSeq.append(nucComps[key])
    newSeq.reverse()
    newSeq2 = ''
    for line in newSeq:
        newSeq2 = newSeq2 + line
    return newSeq2

filename = input("Enter file name: ")
infile = open(f"{filename}.txt")
outfile = open(f"{filename}_revCompsCombined.txt", "w")
lines = infile.readlines()
hexamers = {}
#creation of dictionary for sequence counts, addition of hexamers not alreayd in dictionary, and counting of hexamers and their reverse complements
for line in lines:
    line = line.strip('\n')
    line = line.split('\t')
    if line[0] not in hexamers and revComp(line[0]) not in hexamers:
        hexamers[line[0]] = int(line[1])
    elif line[0] in hexamers or revComp(line[0]) in hexamers:
        if line[0] in hexamers:
            hexamers[line[0]] += int(line[1])
        else:
            hexamers[revComp(line[0])] += int(line[1])
    else:
        print('error')
for key in hexamers:
    outfile.write(str(key) + '\t' + str(hexamers[key]) + '\n')