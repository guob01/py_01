import yaml


# 读取yaml文件内容
def get_data():
    with open("D:/py_projects/config/data.yaml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        # print(data)
        # print(data['hero'])
        # print(data['mobile_params'])
        return data


print(get_data()['mobile_params'])
