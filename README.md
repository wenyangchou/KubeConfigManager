# Kubenaters Config Manager

Sometimes we need manage more than one kubernatee cluster at the same time. 

Switch cluster configs is a dangerous and troublesome operation. This util is designed to 
deal with this scenario. Similar to pyenv, it can support multiple configs at the same time.

## Install

- `git clone https://github.com/wenyangchou/KubeConfigManager.git`

- add the KubeConfigManager/bin into $PATH

## Usage

cm [-options] [args...]

Options include:

    add <name> <path>             Add kubeconfig into manager.
    apply <name>                  Apply a kubeconfig into local environment. Note: it could overwrite the origin
                                   environment config. Please ensure your origin config has been backuped.
    remove <name>                 Remove a kubeconfig which has been add into the manager.
    list                          List kubeconfigs has been added.

