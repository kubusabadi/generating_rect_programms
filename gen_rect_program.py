
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--params", type=int, nargs=2)
args = parser.parse_args()

params = args.params

a = params[0]
b = params[1]

program_text = '''
a = {0}
b = {1}

for i in range(0,a):
    for j in range(0,b):
        print('x', end='')
    print()
'''.format(a,b)

file_name = "rect_{0}_{1}.py".format(a,b)

print(f'Generating: {file_name}')

f = open(file_name, "w")
f.write(program_text)
f.close()
