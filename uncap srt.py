import os

def srt_edit(file_name):
    file = open(file_name+".srt", "r")
    lines = file.readlines()
    file.close()
    file2 = open(file_name+".srt", "w")
    for i in range(len(lines)):
        try:
            line = lines[i]
            if line[13:16] == "-->" or int(lines[i]):
                pass
        except:
            lines[i] = lines[i]
            lines[i] = lines[i].lower().capitalize()
    
        file2.write(lines[i])
    file2.close()
srt_edit(str(input("Please Enter the file name without .srt: ")))
print("Done")

