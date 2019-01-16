F1 = open(r'C:\nitsmagic\log\server_log.txt')
F2 = open('out3.tsv', 'w')
F3 = open('out4.csv', 'w')
F2.writelines(['IP\t', 'Date\t', 'Image\t', 'Web Site\n'])
print('IP', 'Date', 'Image', 'Web Site', sep=',', file=F3)
lines = F1.readlines()
for line in lines:
    if line[0].isdigit():
        sp = line.split()
        #print(sp)
        ip = sp[0]
        date = sp[3].split(':')[0].strip('[')
        if sp[6].startswith('/pics'):
                image = sp[6].split('/')[-1]
        else:
            image = 'No Image'
        website = sp[10].strip('"')
        website = website[0:website.index('com')+3]
        print(ip, date, image, website)
        F2.writelines([ip+'\t' , date+'\t', image+'\t', website+'\n'])
        print(ip, date, image, website, sep=',', file=F3, flush=True)
F1.close()
F2.close()
F3.close()