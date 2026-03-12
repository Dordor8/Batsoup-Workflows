from src.yaml_parser import get_template


print(get_template({'test': 't/test.txt', 'test2': 't/test2.txt'},'my-temp','image:version','python','main.py',{'v': 'rr', 'v2': 'tt'},{'test3': 't/test3.txt'}))