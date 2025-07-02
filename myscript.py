import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

for key, value in config.items():
    new_value = input(f"{key} [{value}]: ")  
    if new_value.strip():  
        if isinstance(value, int):
            try:
                new_value = int(new_value)
            except ValueError:
                print("Invalid input, keeping old value.")
                new_value = value
        config[key] = new_value

with open('config.yaml', 'w') as f:
    yaml.dump(config, f)

print("Updated config saved!")
