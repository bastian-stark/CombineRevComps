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