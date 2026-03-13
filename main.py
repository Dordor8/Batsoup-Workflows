from src.yaml_parser import get_template, get_task, get_workflow, dump_yaml
from ruamel.yaml import YAML

yaml = YAML()
data = get_template({'tests': 't/tests.txt', 'test2': 't/test2.txt'},'my-temp','image:version','python','main.py',{'v': 'rr', 'v2': 'tt'},{'test3': 't/test3.txt'})
data2 = get_task('task1', 'kafka-reader', ['task0', 'taska'], '{{tasks.task0.outputs.results}} == true')
data3 = get_task('task2', 'kafka-reader', ['task0', 'taska'], '{{tasks.task0.outputs.results}} == true')

workflow = get_workflow('my-workflow', [data2, data3], [data])

dump_yaml(workflow, './tests/test-workflow.yaml')