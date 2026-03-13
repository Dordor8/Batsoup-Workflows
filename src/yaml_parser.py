from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString
import os

TEMPLATE_PATH = './resources/template-template.yaml'
TASK_PATH = './resources/task-template.yaml'
WORKFLOW_PATH = './resources/workflow-template.yaml'

yaml = YAML()

def get_template(input_artifacts: dict[str, str],
                 name: str,
                 image: str,
                 command: str,
                 args: str,
                 env_variables: dict[str, str],
                 output_artifacts: dict[str, str]) -> dict:

    with open(TEMPLATE_PATH, "r") as template_file:
        content = yaml.load(template_file)

    print(content)

    content['inputs']['artifacts'] = [{'name': key, 'path': value} for key, value in input_artifacts.items()]
    content['name'] = name
    content['container']['image'] = image
    content['container']['command'] = [command]
    content['container']['args'] = [DoubleQuotedScalarString(args)]
    content['container']['env'] = [{'name': key, 'value': DoubleQuotedScalarString(value)} for key, value in env_variables.items()]
    content['outputs']['artifacts'] = [{'name': key, 'path': value} for key, value in output_artifacts.items()]

    with open("./test/test-template.yaml", "w") as test:
        yaml.dump(content, test)

    return content