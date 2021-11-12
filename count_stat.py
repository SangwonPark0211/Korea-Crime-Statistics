import csv
'''
년도별 소계, 살인, 강도, 절도, 폭력 통계 합산치 print
'''
read_file = open('output.csv', 'r', encoding='utf-8')
read_data = csv.reader(read_file)

year_dict = {'2014':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}, 
        '2015':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}, 
        '2016':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}, 
        '2017':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}, 
        '2018':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}, 
        '2019':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}, 
        '2020':{'total':0, 'm':0, 'r':0, 't':0, 'v':0}}
for i, line in enumerate(read_data):
    if i==0:    continue
    year, po, total, m, r, t, v = line
    year_dict[year]['total'] += int(total)
    year_dict[year]['m'] += int(m)
    year_dict[year]['r'] += int(r)
    year_dict[year]['t'] += int(t)
    year_dict[year]['v'] += int(v)

for k in year_dict:
    print(k, year_dict[k])
read_file.close()  
