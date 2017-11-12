import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# check if service is enabled and running
def test_srv_running_and_enabled(host):
    srv = host.service('gotty')
    assert srv.is_running
    assert srv.is_enabled

# check if configuration file exists
def test_srv_config_file(host):
    f = host.file('/etc/hosts')
    assert f.exists

# # check if service is listening on localhost (netstat must be installed)
# def test_srv_is_listening(host):
#     port = host.socket('tcp://127.0.0.1:80')
#     assert port.is_listening
