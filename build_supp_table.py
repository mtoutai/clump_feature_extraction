import os, sys

header=['image', 'target_gene']
f = open('header.txt', 'r')
for line in f.readlines():
    header.append(line[:-1])
f.close()

target={}
f = open('tif2target.txt', 'r')
for line in f.readlines():
    tif, target_gene = line[:-1].split('\t')
    target[tif]=target_gene
f.close()


srcdir='.'
dstdir='.'
output_filename = 'D2_Additional_file_5_SupDataS3.txt'
output_fullpath = os.path.join(dstdir, output_filename)
datahash = {}
for i in range(1, 12):
    basename = 'nuclear-%02d' % i
    rowname_filename = '%s.rowname.txt' % basename
    feature_filename = '%s.LPX.txt' % basename
    rowname_fullpath = os.path.join(srcdir, rowname_filename)
    feature_fullpath = os.path.join(dstdir, feature_filename)
    rowname = []
    f = open(rowname_fullpath, 'r')
    for line in f.readlines():
        block = line.split('\s')
        path, filename = os.path.split(block[0])
        rowname.append(filename[:-1])
    f.close()
    feature = []
    f = open(feature_fullpath, 'r')
    f.readline()
    for line in f.readlines():
        block = line.split('\t')
        block.pop(0)
        feature.append(block)
    f.close()
    for i in range(len(rowname)):
        # print(rowname[i])
        datahash[rowname[i]]=feature[i]
f = open(output_fullpath, 'w')
f.write('\t'.join(header)+'\n')
for tif in rowname:
    row = [tif, target[tif]]
    for x in datahash[tif]:
        row.append('%s' % x)
    f.write('\t'.join(row))
f.close()

