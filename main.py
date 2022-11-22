#EXTINF:-1 tvg-logo="https://i.imgur.com/IuIBfqD.jpg?1" group-title="Local",INDOSIAR
#http://210.210.155.35/qwr9ew/s/s04/index.m3u8
with open ('output.txt','w') as test:
	test.write('#EXTM3U'+'\n')
	
	
with open('logo.txt') as a_file, open('judul.txt') as b_file,open('movie.txt') as c_file,open('output.txt','a') as output:
    for a_line, b_line, c_line in zip(a_file.readlines(), b_file.readlines(), c_file.readlines()):
        print("#EXTINF:-1 tvg-logo="+'"'
        +a_line.strip()+'"'
        ,('group-title=')
        +b_line.strip(),'\n'+
        c_line.strip())
        
        output.write("#EXTINF:-1 tvg-logo="+'"'
        +a_line.strip()+'"'
        +' '+('group-title=')
        +b_line.strip()+'\n'+
        c_line.strip()+'\n')
        
#with open('/storage/emulated/0/output.txt' 'w') as output:

