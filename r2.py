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

def convert(lines):
	newlines=[]
	allen_word_count=0
	allen_sticker_count=0
	allen_image_count=0
	viki_word_count=0
	viki_sticker_count=0
	viki_image_count=0
	for line in lines:
		s = line.strip().split(' ')
		time=s[0]
		name=s[1]
		if name=='Allen':
			if s[2]=='貼圖':
				allen_sticker_count += 1
			elif s[2]=='圖片':
				allen_image_count += 1
			else:	
				for m in s[2:]:
					allen_word_count += len(m)
		elif name=='Viki':
			if s[2]=='貼圖':
				viki_sticker_count += 1
			elif s[2]=='圖片':
				viki_image_count += 1
			else:	
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen說了',allen_word_count,'個字, 傳了',allen_sticker_count,'個貼圖, ',allen_image_count,'個圖片')
	print('Viki說了',viki_word_count,'個字, 傳了',viki_sticker_count,'個貼圖, ',viki_image_count,'個圖片')
    # 清單取值 s[0:2] -> s[0],s[1] 含起始值,不含結尾值
	#         s[:3]  -> s[0],s[1],s[2]
	#         s[2:]  -> s[2],s[3],s[4]...後面的值全部取

	return newlines

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt',lines)

main()