def test_wazuh_manager_service_running(host):
#	with host.sudo():
	service = host.service('wazuh-manager')
	assert service.is_running
	assert service.is_enabled
