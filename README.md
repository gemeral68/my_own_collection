
## Шаг 3
```python
#!/usr/bin/python3.11

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module

version_added: "1.0.0"

author:
    - Khabibullin Bulat (@gemeral68)
'''
import os
from ansible.module_utils.basic import AnsibleModule

def create_file(path, content):
    if not os.path.lexists(path):
        os.makedirs(path)
    if os.path.lexists(path+'file.txt'):
        return "exsist"
    else:
        try:
            with open(path+'file.txt', 'w') as f:
                f.write(content)
        except:
            raise
        return "created"

def main():
    module_args = {
        "path": {"type": 'str', "required": True},
        "content":{"type": 'str', "required": True}
    }

    result = {"changed": False}

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']

    res = create_file(path, content)

    if module.check_mode:
        module.exit_json(**result)

    if res == "created":
        result['original_message'] = f'file.txt created to path: {path} with content: {content}'
        result['message'] = 'goodbye'
        result['changed'] = True

    module.exit_json(**result)

if __name__ == '__main__':
    main()
```
## Шаг 4
```yml
(venv) [root@localhost ansible]# ansible localhost -m my_own_module -a "path=./ content=123"
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under development. This is a rapidly changing source of code and can become unstable at any point.
localhost | CHANGED => {
    "changed": true,
    "message": "goodbye",
    "original_message": "file.txt created to path: ./ with content: 123"
}
```
## Шаг 5
```yml
---
    - name: Test module
      hosts: localhost
      become: true
      tasks:
        - name: Create file
          my_own_module:
            path: '/home/netology/ansible_module/ansible/'
            content: 'test message'
```
## Шаг 6
### Первый прогон
```yml
(venv) [root@localhost ansible]# ansible-playbook test.yml
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under development. This is a rapidly changing source of code and can become unstable at any point.
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test module] *********************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [Create file] *********************************************************************************************************************************************************************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP *****************************************************************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
### Второй прогон
```yml
(venv) [root@localhost ansible]# ansible-playbook test.yml
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible engine, or trying out features under development. This is a rapidly changing source of code and can become unstable at any point.
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Test module] *********************************************************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************************************************************************************************************************************************************
ok: [localhost]

TASK [Create file] *********************************************************************************************************************************************************************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP *****************************************************************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
