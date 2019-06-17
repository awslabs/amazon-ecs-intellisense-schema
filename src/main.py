import sys
print(sys.path)

from src.api_2_reader import get_task_def, write_task_def

construct = get_task_def('shapes', 'RegisterTaskDefinitionRequest')
write_task_def(construct)

