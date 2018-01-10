#!/usr/bin/python
# -*- coding: UTF-8 -*-
def grep_pattern_line(file_path,pattern) :
    try:
        document=open(file_path)
    except FileNotFoundError :
        return "File not found"
    except PermissionError :
        return "No permission"
		strings=str(document.read())
		lines=strings.split('\n')
		result=""
		document.close()
		for num in range(0,len(lines)) :
			if lines[num].find(pattern) != -1 :
				result=result+str(num+1)+','
				continue
		return result

if __name__ == '__main__':
    print(grep_pattern_line("test.txt", "alp" ))