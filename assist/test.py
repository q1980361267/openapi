import yaml

# with open('test.yaml', 'r') as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(data)
# data['a'] = 2

with open('test.yaml', 'w') as f:

    yaml.dump({'a':1}, f)