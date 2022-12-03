import json
import subprocess
f = open('params.json')

data = json.load(f)

f.close()

print(data)

for param_set in data['params']:
    params = " ".join(str(item) for item in param_set)
    command_str = f'python gen_rect_program.py --params {params}'
    print(f'running: {command_str}')
    subprocess.Popen(command_str,shell=True)
