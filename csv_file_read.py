import csv

# read
f = open('경찰청_전국 경찰서별 강력범죄 발생 현황_20201231.csv', 'r', encoding='euc-kr')
rdr = csv.reader(f)
for line in rdr:
    print(line)
    break
f.close()  

# write
f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "김정수", False])
wr.writerow([2, "박상미", True])
f.close()