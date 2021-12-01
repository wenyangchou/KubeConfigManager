import os


def list_config():
    resource_dir = os.path.join(os.path.dirname(__file__), "resource")
    config_names = []
    for config in os.listdir(resource_dir):
        if config.startswith("config"):
            config_name = config.split(".")[1]
            config_names.append(config_name)
    return config_names


def current():
    resource_dir = os.path.join(os.path.dirname(__file__), "resource")
    cm_path = os.path.join(resource_dir, "cm.txt")
    with open(cm_path, 'r') as f:
        return f.read()


def remove_current():
    resource_dir = os.path.join(os.path.dirname(__file__), "resource")
    cm_path = os.path.join(resource_dir, "cm.txt")
    with open(cm_path, 'w') as f:
        f.write('')


def remove_config(name):
    resource_dir = os.path.join(os.path.dirname(__file__), "resource")
    config_path = os.path.join(resource_dir, 'config.%s' % name)
    os.remove(config_path)

def update_cm(name):
    resource_dir = os.path.join(os.path.dirname(__file__), "resource")
    cm_path = os.path.join(resource_dir, "cm.txt")
    with open(cm_path, 'w') as f:
        f.write(name)
