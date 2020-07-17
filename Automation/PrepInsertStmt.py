import glob

inputfolderpath = '/home/inct-sandeshmendan/sandesh/ML/anaDump/temp/'
data = 'insert into appsec(KEY,VALUE) VALUES("dlp|people",{"_type": "info_type","case_insensitive": true,"multiline": true,"category": "pii","keywords": $appsecKeywords,"name": "PEOPLE","tenantId": ""}) '
nFile = '/home/inct-sandeshmendan/sandesh/ML/anaDump/dlp|people.txt'

def createInsertStatement(inputfolderpath, data=data, nFile=nFile):
    lines_seen = set()
    txt_files = glob.glob(inputfolderpath + "*.txt")
    for file in txt_files:
        for line in open(file, "r"):
            if line.strip() not in lines_seen:
                lines_seen.add(line.strip())
    encloseChar = '"'
    keywords = '[' + ','.join(map(str, [encloseChar + i + encloseChar for i in lines_seen])) + ']'
    searchPattern = '$appsecKeywords'
    data = data.replace(searchPattern, keywords)
    outfile = open(nFile, "w")
    outfile.write(data)
    outfile.close()

createInsertStatement(inputfolderpath)
