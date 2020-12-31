#配置文件
#properties  config  inni  log4j
#configparser  可以去读取配置信息

import configparser
#section option value   key：value

cf = configparser.ConfigParser()
cf.read('case.config',encoding='UTF-8')

#读取配置文件的数据
print(cf.sections())   #拿到所有片区（标签）
print(cf.items('PYTHON11'))  #拿到指定片区的键值对
res_1 = cf.get('MODE','mode')
print(res_1)

res_2 = cf['MODE']['mode']
print(res_2)

#数据类型讨论的问题--》都是字符串 ---》eval（）转换我们的字符串
print(type(cf.get('PYTHON11','num')))
