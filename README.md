# Ansible Role: Gotty
[![Build Status](https://img.shields.io/travis/cndies/ansible-role-gotty.svg)](https://travis-ci.org/cndies/ansible-role-gotty)
[![Galaxy](http://img.shields.io/badge/galaxy-cndies.role-gotty-blue.svg)](https://galaxy.ansible.com/cndies/role-gotty)
[![GitHub Tags](https://img.shields.io/github/tag/cndies/ansible-role-gotty.svg)](https://github.com/cndies/ansible-role-gotty)
[![GitHub Stars](https://img.shields.io/github/stars/cndies/ansible-role-gotty.svg)](https://github.com/cndies/ansible-role-gotty)

Install and configure Gotty

Requirements
------------

None

Role Variables
--------------

* gotty_version: '1.0.1'
* gotty_type: 'linux_amd64'
* gotty_baseurl: "https://github.com/yudai/gotty/releases/download/v"
* gotty_force_dwn: yes
* gotty_path: '/usr/local/bin'
* gotty_logs: '/var/log'
* gotty_cmd: 'top'
* gotty_port: '80'
* gotty_permit_write: 'false'
* gotty_enable_tls: 'false'
* gotty_enable_basic_auth: 'false'
* gotty_basic_credential: 'test:test'
* gotty_enable_reconnect: 'true'

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - cndies.gotty

License
-------

BSD

Author Information
------------------

https://github.com/cndies
