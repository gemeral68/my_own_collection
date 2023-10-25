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
            with open(path+'file.txt', 'w') as fp:
                fp.write(content)
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
