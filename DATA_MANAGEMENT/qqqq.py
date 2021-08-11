import xlrd

readbook = xlrd.open_workbook(r'file/4.xls')
sheet = readbook.sheet_by_index(1)

nrows = sheet.nrows  # 行
print(nrows)
ncols = sheet.ncols  # 列
print(ncols)
file_01 = open(r"file/代理点卡库存.txt", 'a+')
file_02 = open(r"file/自营点卡库存.txt", 'a+')
file_03 = open(r"file/大客户卡库存.txt", 'a+')

for i in range(1, ncols):
    if i % 2 == 0:
        continue
    pos = sheet.cell(0, i).value.split('/')[1]
    print(pos)
    for j in range(1, nrows):
        cardno = sheet.cell(j, i).value
        # print(cardno)
        if len(cardno) != 8:
            print(cardno)
        if not cardno:
            break
        # print(sheet.cell(j, i).value)
        sql = f"INSERT INTO [dbo].[T_FRSTORECARDDIC]([CARDID], [CARDSN], [CARDSTATUS], [CARDPOSITION], [CARDPOSORG], [STOCKWASTESN], [ISSUEORGCODE], [ISSUEOPER], [ISSUESAMID], [ISSUETIME], [UPDATETIME], [SPARE1], [SPARE2], [SPARE3], [SPARE4]) VALUES (N'00000000{cardno}', '1', 0, 2, N'{pos}', N'20210428145440', N'V001', N'300801', N'1', '2021-04-27 14:52:30.000', '2021-05-24 13:51:14.650', NULL, NULL, NULL, NULL);"
        # print(sql)
        file_02.write(f"{sql}\n")
