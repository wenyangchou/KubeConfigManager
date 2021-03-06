import os
import sys

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)

import utils

resource_dir = os.path.join(root_path, "resource")

def add(name, path):
    config_name = "config.%s" % name
    print(resource_dir)
    target_path = os.path.join(resource_dir, config_name)
    os.system("cp %s %s" % (path, target_path))
    print("add config %s successful!" % name)


def _list():
    current = utils.current()
    for config in os.listdir(resource_dir):
        if config.startswith("config"):
            config_name = config.split(".")[1]
            if current != "" and current == config_name:
                print("* %s" % config_name)
            else:
                print(config_name)


def remove(name):
    current = utils.current()
    if current == name:
        utils.remove_current()
        os.remove('~/.kube/config')
    else:
        utils.remove_config(name)


def apply(name):
    config_list = utils.list_config()
    if config_list.__contains__(name):
        if not os.path.exists("~/.kube"):
            os.makedirs("~/.kube")

        if os.path.exists("~/.kube/config"):
            os.system('rm -rf ~/.kube/config')

        os.system("cp %s ~/.kube/config" % os.path.join(resource_dir, "config.%s" % name))
        utils.update_cm(name)
        print('apply successful!')
    else:
        print("config name is not exist!")


def _help():
    help_msg = '''
    km controls multipart kubernates configs.

    Find more information at: https://github.com/wenyangchou/KubeConfigManager

    Usage: cm [-options] [args...]

    Options include:

        add <name> <path>             Add kubeconfig into manager.
        apply <name>                  Apply a kubeconfig into local environment. Note: it could overwrite the origin
                                       environment config. Please ensure your origin config has been backuped.
        remove <name>                 Remove a kubeconfig which has been add into the manager.
        list                          List kubeconfigs has been added.
    '''
    print(help_msg)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        _help()
    else:
        option = sys.argv[1]

        if option == 'add':
            name = sys.argv[2]
            path = sys.argv[3]
            add(name, path)
        elif option == 'list':
            _list()
        elif option == 'help':
            _help()
        elif option == 'apply':
            name = sys.argv[2]
            apply(name)
        elif option == 'remove':
            name = sys.argv[2]
            remove(name)
        else:
            _help()
