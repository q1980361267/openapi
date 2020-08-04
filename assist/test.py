import yaml

with open('../assist_config.yaml', 'r') as f:

    data = yaml.load(f)
    print(data)