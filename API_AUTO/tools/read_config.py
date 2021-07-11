import configparser

class ReadConfig:
    def read_config(self,file_name,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='UTF-8')
        print(cf.get(section.option))

if __name__ == '__main__':

    res = ReadConfig().read_config('case.config','Mode','mode')
    print(res)