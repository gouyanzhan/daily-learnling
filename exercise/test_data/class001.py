import pandas as pd

df = pd.read_excel('test_data.xlsx',sheet_name='recharge')
# print(df.values)   #读嵌套列表
# print(df.ix[1].value)
# print(df.ix[1,['url','data','title','case_id','http_,ethod']].to_dict())
test_data = []
for i in df.index.values:
    row_data = df.ix[i,['url','data','title','case_id','http_,ethod']].to_dict()
    test_data.append(row_data)

print(test_data)


