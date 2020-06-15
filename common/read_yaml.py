import yaml
import os


def readyml(filepath):
    # 读取yaml文件
    f = open(filepath, "r", encoding="utf-8")
    y = f.read()
    data = yaml.load(y)
    print("读取yaml文件转字典：%s" % data)
    return data

if __name__ == '__main__':
    # read_yaml.py和yml文件在同一个文件夹可以直接读取到
    # 不在同一个文件夹用绝对路径
    a = readyml('data_test.yml')
    print(a['test_add_articleclassify_param'])

    # 不在同一个文件夹，读取当前脚本的路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(os.path.dirname(cur_path), "case", 'data_test2.yml')
    print(yaml_path)
    b = readyml(yaml_path)
    print(b['test_add_articleclassify_param2'])


