import glob
import re
import os
from os.path import basename

inputfolderpath = os.path.abspath(os.getcwd()) + '/'
print('Directory for which script is being run: ' + inputfolderpath)
outputFile = inputfolderpath + 'insertScripts.txt'
outfile = open(outputFile, "w+")
txt_files = glob.glob(inputfolderpath + "*.txt") #all files in a directory
filesCount = len(txt_files)

insertStructure = 'insert into appsec(KEY,VALUE) VALUES("dlp|$fileName",{"_type": "info_type","case_insensitive": true,"multiline": true,"category": "pii","keywords": $appsecKeywords,"name": $fileName,"tenantId": ""})'
keywordPattern = '$appsecKeywords'
filePattern = '$fileName'

print('Processing...')
for file in txt_files:
    if file != outputFile:
        #fetch unique lines
        lines_seen = set()
        for line in open(file, "r"):
            if line.strip() not in lines_seen:
                lines_seen.add(line.strip())

        #formatting to ["insertFile1", "insertFile2", ....]
        encloseChar = '"'
        keywords = '[' + ','.join(map(str, [encloseChar + i + encloseChar for i in lines_seen])) + ']'

        #replacing pattern in statement
        rep = {keywordPattern: keywords, filePattern : os.path.splitext(basename(file))[0]}
        rep = dict((re.escape(k), v) for k, v in rep.items())
        pattern = re.compile("|".join(rep.keys()))
        finalInsert = pattern.sub(lambda m: rep[re.escape(m.group(0))], insertStructure)

        # since we skipped insertScripts.txt file; handling ','
        if filesCount == 2:
            outfile.write(finalInsert)
            break
        outfile.write(finalInsert+','+"\n")
        filesCount = filesCount - 1

outfile.close()
print('Finished....Results are stored in: ' + outputFile)