# Ansible Role: Gotty
[![Build Status](https://img.shields.io/travis/cndies/ansible-role-gotty.svg)](https://travis-ci.org/cndies/ansible-role-gotty)
[![Galaxy](https://img.shields.io/badge/galaxy-cndies.gotty-blue.svg)](https://galaxy.ansible.com/cndies/gotty)
[![GitHub Tags](https://img.shields.io/github/tag/cndies/ansible-role-gotty.svg)](https://github.com/cndies/ansible-role-gotty)
[![GitHub Stars](https://img.shields.io/github/stars/cndies/ansible-role-gotty.svg)](https://github.com/cndies/ansible-role-gotty)

Install and configure Gotty, https://github.com/yudai/gotty

* GoTTY is a simple command line tool that turns your CLI tools into web applications.
* With default settings this role installs gotty as a service and run `top` command listening on port 80.
* You can setup web shell by changing vars to: gotty_cmd: 'login', gotty_permit_write: 'true' and apply this role.
* You can also enable basic auth, gotty_enable_basic_auth: 'true' and set gotty_basic_credential.

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

Simple playbook to test:

    - hosts: all
      roles:
         - cndies.gotty

Testing
------------

* This role uses molecule v2.x with docker driver to test functionality. All platforms for test are described in `molecule/default/molecule.yml`. Testinfra tests in `molecule/default/tests/test_default.py`.
* TravisCI is used to run tests. For local test you need to install `ansible, molecule, docker-py` and run `molecule test`.

License
-------

MIT

Author Information
------------------

https://github.com/cndies
