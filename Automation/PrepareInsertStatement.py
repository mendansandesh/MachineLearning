import glob
lines_seen = set()
outputfile      = '/home/inct-sandeshmendan/sandesh/ML/anaDump/temp/noDup.txt'
inputfolderpath = '/home/inct-sandeshmendan/sandesh/ML/anaDump/temp/'
def mergeAllFilesWithUniqueLines(outputfile, inputfolderpath):
    txt_files = glob.glob(inputfolderpath + "*.txt")
    outfile = open(outputfile, "w")
    for file in txt_files:
        for line in open(file, "r"):
            if line.strip() not in lines_seen:
                outfile.write(line)
                lines_seen.add(line.strip())
    outfile.close()

mergeAllFilesWithUniqueLines(outputfile, inputfolderpath)
print("------lines seen---")
print(lines_seen)


insertStatementFile = '/home/inct-sandeshmendan/sandesh/ML/anaDump/insertStmt.txt'
searchPattern = '$appsecKeywords'

encloseChar = '"'
data = [encloseChar + i + encloseChar for i in lines_seen]
data = ','.join(map(str, data))
data = '[' + data + ']'
print("------replace string---")
print(data)

def prepareInsertStatements(insertStatementFile):
    lines = []
    with open(insertStatementFile) as infile:
        for line in infile:
            line = line.replace(searchPattern, data)
            lines.append(line)

    with open(insertStatementFile, 'w') as outfile:
        for line in lines:
            outfile.write(line)

prepareInsertStatements(insertStatementFile)
print('----finished creating insert stmt----')