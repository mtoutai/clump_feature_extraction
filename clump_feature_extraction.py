import os
import glob
import re

imagej_root='G:\\Users\\mtoutai\\Downloads\\ImageJ'
imagej_jar=imagej_root_dos+'\\ij.jar'

batch_filename='clump_feature_extraction.BAT'
batch = open(batch_filename, 'w')
for index in range(1, 12):
    dirname='nuclear-%02d' % index
    srcdir=os.path.join('D2_Additional_file_3_SupDataS1', dirname)
    outfile_fullpath='%s.LPX.txt' % dirname
    macro_filename='%s.jim' % dirname
    macro_path='macro'
    if not os.path.exists(macro_path):
        os.makedirs(macro_path)
    macro_fullpath=os.path.join(macro_path, macro_filename)
    macro = open(macro_fullpath, 'w')
    rowname_filename='%s.rowname.txt' % dirname
    rowname_path='.'
    rowname_fullpath=os.path.join(rowname_path, rowname_filename)
    rowname = open(rowname_fullpath, 'w')
    for tif in glob.glob(os.path.join(srcdir, '*.tif')):
        path, tif_filename = os.path.split(tif)
        tif_slash = re.sub('\\\\', '/', tif)
        rowname.write("%s\n" % tif_slash)
        macro.write("print(\"%s\");\n" % tif_slash)
        macro.write("open(\"%s\");\n" % tif_slash)
        if tif_filename == 'CP09232018001E07_ICA09242018EXP001_C10000_FLD014_EX-Brightfield_EM-dsRed_590_734.tif':
            # only this image raises an error saying "image not power of 2 size or not square"
            # So I crop it 1 pixel width to avoid the error
            macro.write("makeRectangle(0, 0, 62, 31);\n")
            macro.write("run(\"Crop\");\n")
        macro.write("run(\"Lpx Features\", \"feature=Lpx296 mode=eachSliceToTable sizex=16 sizey=16 stepx=16 stepy=16\");\n");
        macro.write("close();\n\n")
    macro.write("saveAs(\"Text\", \"%s\");\n" % outfile_fullpath)
    macro.close()
    rowname.close()
    batch.write("java -Xmx1024m -jar %s -ijpath %s -batch %s\n" % (imagej_jar, imagej_root, macro_fullpath))
batch.close()

