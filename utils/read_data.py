import yaml


# 读取yaml文件内容
def read_yaml(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        # print(data)
        # print(data['hero'])
        # print(data['mobile_params'])
    return data


print(read_yaml("D:/py_projects/py_01/config/data.yaml"))
