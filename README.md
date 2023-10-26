# Ansible Collection - my_own_namespace.yandex_cloud_elk
## my_own_namespace.yandex_cloud_elk ansible collection structure:
```yml
├── docs
├── galaxy.yml
├── meta
│   └── runtime.yml
├── plugins
│   ├── modules
│   │   └── my_own_module.py
│   └── README.md
├── README.md
└── roles
    └── create_file
        ├── defaults
        │   └── main.yml
        ├── files
        ├── handlers
        │   └── main.yml
        ├── meta
        │   └── main.yml
        ├── README.md
        ├── tasks
        │   └── main.yml
        ├── templates
        ├── tests
        │   ├── inventory
        │   └── test.yml
        └── vars
            └── main.yml
```
## Installation
1. Download tar.gz from repo: 
https://github.com/gemeral68/devops_netology/blob/main/mnt-homeworks/08-ansible-06-module/my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
2. Install with:
```
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## DOCUMENTATION
```yml
---
module: my_own_module.py

short_description: Module for creating a file with some text

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining how my module works.

options:
    path:
        description: destination directory.
        required: true
        type: str
    content:
        description: some text
        required: True
        type: str

author:
    - Khabibullin Bulat (@gemeral68)
```

## EXAMPLES 
```yml
---
- name: Module role
  hosts: localhost
  collections:
    - my_own_namespace.yandex_cloud_elk
  tasks:
    - name: Import createfile role
      ansible.builtin.import_role:
        name: create_file
---
- name: Module role
  hosts: localhost
  collections:
    - my_own_namespace.yandex_cloud_elk
  tasks:
    - name: Run a module
      my_own_module:
        path: value
        content: value
```
