import os

def convert_to_iso_8859_1(oldfile):
    '''\
    Encoding translation from UTF-8 to ISO-8859-1
    oldfile: file encoded in UTF-8
    Note:
    - codecs class is obsolete in 3.x, since open() gains an encoding argument
    '''
    
    sourceFile = open(oldfile, "r", encoding="utf_8")
    targetFile = open("tempfile", "w", encoding="iso-8859-1", errors='ignore')
    contents = sourceFile.read()
    targetFile.write(contents) 
    
    sourceFile.close()
    targetFile.close()
    
    return "tempfile"
    
        
def convert_time_representation(oldfile, newfile):
    '''\
    Replace dot by comma as a separator in time representation.
    oldfile expresses time as:     hh:mm:ss.sss
    newfile shall express time as: hh:mm:ss,sss
    Note:
    - https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
    - Typically time is represented as "timeStart --> timeStop" so that it 
      makes sense to use "-->" as delimiter in the split method
    '''
    
    sourceFile = open(oldfile, "r", encoding="iso-8859-1")
    targetFile = open(newfile, "w", encoding="iso-8859-1")
    
    for line in sourceFile:
        if "-->" in line:
            timeStart, timeStop = line.split('-->')
            timeStart = timeStart.replace('.',',')
            timeStop = timeStop.replace('.',',')
            targetFile.write(timeStart + '-->' + timeStop)
        else:
            targetFile.write(line)
    
    sourceFile.close()
    targetFile.close()

def truncate_last_lines_in_file(tempfile):
    '''\
    Truncate last lines in file by slicing
    Note:
    - Cutting and Slicing: https://www.pythoncentral.io/cutting-and-slicing-strings-in-python/
    '''
    
    sourceFile = open(tempfile, "r", encoding="iso-8859-1")
    lines = sourceFile.readlines()
    lines = lines[:-6]
    sourceFile.close()
    os.remove(tempfile)
    
    targetFile = open(tempfile, "w", encoding="iso-8859-1")
    targetFile.writelines(lines)
    targetFile.close()
    
    return tempfile
    
    
oldfile = input('Name of a origin file: ')
newfile = input('Name of a destination file: ')
tempfile = convert_to_iso_8859_1(oldfile)
tempfile = truncate_last_lines_in_file(tempfile)
newfile = convert_time_representation(tempfile, newfile)
os.remove(tempfile)