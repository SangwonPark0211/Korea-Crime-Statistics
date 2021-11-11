import csv

# data preprocessing
read_file = open('경찰청_전국 경찰서별 강력범죄 발생 현황.csv', 'r', encoding='euc-kr')
read_data = csv.reader(read_file)
write_file = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(write_file)
wr.writerow(['Year', 'PoliceOffice', 'Total', 'Murder', 'Robber', 'Theft', 'Violence'])
po_dict = {}
for i, line in enumerate(read_data):
    if i==0:    continue
    year, po, total, m, r, t, v = line
    if po not in po_dict:
        po_dict[po] = len(po_dict)
    po = po_dict[po]
    wr.writerow([year, po, total, m, r, t, v])
read_file.close()  
write_file.close()

# police office look-up table save
po_file = open('police_office_table.txt', 'w', encoding='euc-kr')
for key in po_dict:
    po_file.write(str(po_dict[key]) + ' ' + key + '\n')
po_file.close()

# 2018~2019 data processing
