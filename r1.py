def read_file(filename):
	lines=[]
	with open( filename,'r',encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def write_file(filename,newlines):
	with open(filename,'w',encoding='utf-8-sig') as f:
		for line in newlines:
			f.write(line)

def convert(filename,lines):
	person=''
	newlines=[]
	for line in lines:
		line = line.strip()
		if (line =='Allen') or (line=='Tom'):
			person = line
			continue
		else:
			newlines.append(person+': ' +  line + '\n')
	write_file(filename,newlines)

def main():
	lines = read_file('input.txt')
	convert('output.txt',lines)
	#print(lines)	

main()