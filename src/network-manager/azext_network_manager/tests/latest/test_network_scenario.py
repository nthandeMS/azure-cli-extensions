# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer

from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Test class for Scenario
class NetworkScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(NetworkScenarioTest, self).__init__(*args, **kwargs)

    @ResourceGroupPreparer(name_prefix='test_network_manager_crud', location='eastus2euap')
    def test_network_manager_crud(self, resource_group):
        self.kwargs.update({
            'name': 'TestNetworkManager',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id())
        })

        self.cmd('network manager create --name {name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "Connectivity" '
                 '--network-manager-scopes '
                 'subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')
        
        self.cmd('network manager show --resource-group {rg} --name {name}')

        # Update is not allowed for NM.
        # self.cmd('network manager update --resource-group {rg} --name {name} --tags key1=value1')

        self.cmd('network manager list --resource-group {rg}')

        self.cmd('network manager delete --resource-group {rg} --name {name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_group', location='eastus2euap')
    def test_network_manager_group_crud(self, resource_group):

        self.kwargs.update({
            'name': 'TestNetworkGroup',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample group"',
            'display_name': 'MyNetworkGroup',
            'member_type': 'Microsoft.Network/virtualNetworks',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id())
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {name} --network-manager-name {manager_name} '
                 '--description {description} --display-name {display_name} --member-type {member_type} -g {rg} ')

        self.cmd('network manager group update -g {rg} --name {name} --network-manager-name {manager_name} --description "Desc changed."')
        self.cmd('network manager group show -g {rg} --name {name} --network-manager-name {manager_name}')
        self.cmd('network manager group list -g {rg} --network-manager-name {manager_name}')
        self.cmd('network manager group delete -g {rg} --name {name} --network-manager-name {manager_name} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_static_member', location='eastus2euap')
    @VirtualNetworkPreparer()
    def test_network_manager_static_member_crud(self, virtual_network, resource_group):
        self.kwargs.update({
            'name': 'TestStaticMember',
            'group_name': 'TestNetworkGroup',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample group"',
            'display_name': 'MyNetworkGroup',
            'member_type': 'Microsoft.Network/virtualNetworks',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network
        })
        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--display-name {display_name} --member-type {member_type} -g {rg} ')

        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}" -g {rg}')

        # self.cmd('network manager group static-member update -g {rg} --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
        #          '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"')
        self.cmd('network manager group static-member show -g {rg} --name {name} --network-group-name {group_name} --network-manager-name {manager_name}')
        self.cmd('network manager group static-member list -g {rg} --network-group-name {group_name} --network-manager-name {manager_name}')
        self.cmd('network manager group static-member delete -g {rg} --name {name} --network-group-name {group_name} --network-manager-name {manager_name} --yes')

        self.cmd('network manager group delete -g {rg} --name {group_name} --network-manager-name {manager_name} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='test_network_manager_security_user_config', location='eastus2euap')
    def test_network_manager_security_user_config_crud(self, resource_group):

        self.kwargs.update({
            'name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityUser" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager security-user-config create --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig')

        self.cmd('network manager security-user-config update --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description "test_description"')
        self.cmd('network manager security-user-config list --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-user-config show --configuration-name {name} --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-user-config delete --configuration-name {name} --network-manager-name {manager_name} -g {rg} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_security_admin_config', location='eastus2euap')
    def test_network_manager_security_admin_config_crud(self, resource_group):

        self.kwargs.update({
            'name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager security-admin-config create --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig')

        self.cmd('network manager security-admin-config update --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description "test_description"')
        self.cmd('network manager security-admin-config list --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-admin-config show --configuration-name {name} --network-manager-name {manager_name} -g {rg}')

        # test nm commit
        # self.cmd('network manager post-commit --network-manager-name {manager_name} --commit-type "SecurityAdmin" --target-locations "eastus2euap" -g {rg} '
        #          '--configuration-ids {sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/securityAdminConfigurations/{name}')

        # test nm uncommit
        # self.cmd('network manager post-commit --network-manager-name {manager_name} --commit-type "SecurityAdmin" --target-locations "eastus2euap" -g {rg} ')

        self.cmd('network manager security-admin-config delete --configuration-name {name} --network-manager-name {manager_name} -g {rg} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_admin_rule_crud', location='eastus2euap')
    @VirtualNetworkPreparer()
    def test_network_manager_admin_rule_crud(self, virtual_network, resource_group):

        self.kwargs.update({
            'rule_name': 'myRule',
            'collection_name': 'myTestCollection',
            'config_name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network,
            'name': 'TestStaticMember'
        })


        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 ' --display-name ASampleGroup --member-type "Microsoft.Network/virtualNetworks" -g {rg} ')

        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"  -g {rg} ')

        self.cmd('network manager security-admin-config create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig')

        self.cmd('network manager security-admin-config rule-collection create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--rule-collection-name {collection_name} --description {description} --display-name ASampleCollection '
                 '--applies-to-groups  network-group-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/networkGroups/{group_name}')


        self.cmd('network manager security-admin-config rule-collection rule create -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} '
                 '--rule-name {rule_name} --kind "Custom" --protocol "Tcp" --access "Allow" --priority 32 --direction "Inbound"')
        self.cmd('network manager security-admin-config rule-collection rule show -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} --rule-name {rule_name}')
        self.cmd('network manager security-admin-config rule-collection rule update -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} --rule-name {rule_name} '
                 '--access "Deny"')
        self.cmd('network manager security-admin-config rule-collection rule list -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name}')
        self.cmd('network manager security-admin-config rule-collection rule delete -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} --rule-name {rule_name} --yes')

        self.cmd('network manager security-admin-config delete --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} --force --yes')
        self.cmd('network manager group delete -g {rg} --name {group_name} --network-manager-name {manager_name} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')


    @ResourceGroupPreparer(name_prefix='test_network_manager_admin_rule_collection_crud', location='eastus2euap')
    @VirtualNetworkPreparer()
    def test_network_manager_admin_rule_collection_crud(self, virtual_network, resource_group):

        self.kwargs.update({
            'collection_name': 'myTestCollection',
            'config_name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network,
            'name': 'TestStaticMember'
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--display-name ASampleGroup --member-type "Microsoft.Network/virtualNetworks" -g {rg} ')

        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"  -g {rg} ')

        self.cmd('network manager security-admin-config create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig')

        self.cmd('network manager security-admin-config rule-collection create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--rule-collection-name {collection_name} --description {description} --display-name ASampleCollection '
                 '--applies-to-groups  network-group-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/networkGroups/{group_name}')
        
        self.cmd('network manager security-admin-config rule-collection show -g {rg} --configuration-name {config_name} --network-manager-name {manager_name} --rule-collection-name {collection_name}')

        self.cmd('network manager security-admin-config rule-collection update -g {rg} --configuration-name {config_name} --network-manager-name {manager_name} --rule-collection-name {collection_name} '
                 '--display-name ASampleCollection2')

        self.cmd('network manager security-admin-config rule-collection list -g {rg} --configuration-name {config_name} --network-manager-name {manager_name}')

        self.cmd('network manager security-admin-config rule-collection delete -g {rg} --configuration-name {config_name} --network-manager-name {manager_name} --rule-collection-name {collection_name} --yes')
        self.cmd('network manager security-admin-config delete --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} --force --yes')
        self.cmd('network manager group delete -g {rg} --name {group_name} --network-manager-name {manager_name} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='test_network_manager_user_rule_crud', location='eastus2euap')
    @VirtualNetworkPreparer()
    def test_network_manager_user_rule_crud(self, virtual_network, resource_group):
        self.kwargs.update({
            'rule_name': 'myRule',
            'collection_name': 'myTestCollection',
            'config_name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityUser" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--display-name ASampleGroup --member-type "Microsoft.Network/virtualNetworks" -g {rg} ')

        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"  -g {rg} ')

        self.cmd('network manager security-user-config create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig')

        self.cmd('network manager security-user-config rule-collection create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--rule-collection-name {collection_name} --description {description} --display-name ASampleCollection '
                 '--applies-to-groups  network-group-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/networkGroups/{group_name}')

        self.cmd('network manager security-user-config rule-collection rule create -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} '
                 '--rule-name {rule_name} --kind "Custom" --protocol "Tcp" --direction "Inbound"')
        self.cmd('network manager security-user-config rule-collection rule show -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} --rule-name {rule_name}')
        self.cmd('network manager security-user-config rule-collection rule update -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} --rule-name {rule_name} '
                 '--protocol "Udp"')
        self.cmd('network manager security-user-config rule-collection rule list -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name}')
        self.cmd('network manager security-user-config rule-collection rule delete -g {rg} --network-manager-name {manager_name} --configuration-name {config_name} --rule-collection-name {collection_name} --rule-name {rule_name} --yes')

    @unittest.skip('skip')
    @ResourceGroupPreparer(name_prefix='test_network_manager_user_rule_collection_crud', location='eastus2')
    @VirtualNetworkPreparer()
    def test_network_manager_user_rule_collection_crud(self, virtual_network, resource_group):

        self.kwargs.update({
            'collection_name': 'myTestCollection',
            'config_name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityUser" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--display-name ASampleGroup --member-type "Microsoft.Network/virtualNetworks" -g {rg} ')
        
        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"  -g {rg} ')

        self.cmd('network manager security-user-config create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig')

        self.cmd('network manager security-user-config rule-collection create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--rule-collection-name {collection_name} --description {description} --display-name ASampleCollection '
                 '--applies-to-groups  network-group-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/networkGroups/{group_name}')
        
        self.cmd('network manager security-user-config rule-collection show -g {rg} --configuration-name {config_name} --network-manager-name {manager_name} --rule-collection-name {collection_name}')
        self.cmd('network manager security-user-config rule-collection update -g {rg} --configuration-name {config_name} --network-manager-name {manager_name} --rule-collection-name {collection_name} '
                 '--display-name ASampleCollection2')
        self.cmd('network manager security-user-config rule-collection list -g {rg} --configuration-name {config_name} --network-manager-name {manager_name}')
        self.cmd('network manager security-user-config rule-collection delete -g {rg} --configuration-name {config_name} --network-manager-name {manager_name} --rule-collection-name {collection_name} --yes')
        self.cmd('network manager security-user-config delete --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} --yes')
        self.cmd('network manager group delete -g {rg} --name {group_name} --network-manager-name {manager_name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_connect_config_crud', location='eastus2euap')
    @VirtualNetworkPreparer()
    def test_network_manager_connect_config_crud(self, virtual_network, resource_group):
        self.kwargs.update({
            'config_name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network,
            'name': 'TestStaticMember'
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--display-name ASampleGroup --member-type "Microsoft.Network/virtualNetworks" -g {rg} ')
        
        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"  -g {rg} ')

        self.cmd('network manager connect-config create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--applies-to-groups group-connectivity="None" network-group-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/networkGroups/{group_name} '
                 'is-global=false use-hub-gateway=true --connectivity-topology "HubAndSpoke" --delete-existing-peering true --hub '
                 'resource-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network} '
                 'resource-type="Microsoft.Network/virtualNetworks" --description "Sample Configuration" --is-global true')
        self.cmd('network manager connect-config show --configuration-name {config_name} --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager connect-config update --configuration-name {config_name} --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager connect-config list --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager connect-config delete --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} --yes')
 
        self.cmd('network manager group delete -g {rg} --name {group_name} --network-manager-name {manager_name} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')


    @ResourceGroupPreparer(name_prefix='test_network_manager_list_queries', location='eastus2euap')
    @VirtualNetworkPreparer()
    def test_network_manager_list_queries(self, virtual_network, resource_group):

        self.kwargs.update({
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network,
            'name': 'TestStaticMember'
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--display-name ASampleGroup --member-type "Microsoft.Network/virtualNetworks" -g {rg} ')

        self.cmd('network manager group static-member create --name {name} --network-group-name {group_name} --network-manager-name {manager_name} '
                 '--resource-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}"  -g {rg} ')

        self.cmd('network manager list-deploy-status --network-manager-name {manager_name} --deployment-types "Connectivity" --regions "eastus2euap" --resource-group {rg}')
        self.cmd('network manager group list-effect-vnet --network-group-name {group_name} --network-manager-name {manager_name} --resource-group {rg}')
        # self.cmd('network manager list-effect-vnet --network-manager-name {manager_name} --resource-group {rg}')
        self.cmd('network manager list-active-connectivity-config --network-manager-name {manager_name} --resource-group {rg} --regions eastus westus')
        self.cmd('network manager list-effective-connectivity-config --virtual-network-name {virtual_network} -g {rg}')
        self.cmd('network manager list-effective-security-admin-rule --virtual-network-name {virtual_network} -g {rg}')
        self.cmd('network manager list-active-security-admin-rule --network-manager-name {manager_name} -g {rg} --regions eastus2euap')
        # Internal Server Error
        # self.cmd('network manager list-active-security-user-rule --network-manager-name {manager_name} -g {rg} --region eastus2euap')

        self.cmd('network manager group delete -g {rg} --name {group_name} --network-manager-name {manager_name} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')


    @ResourceGroupPreparer(name_prefix='test_network_manager_scope_connection', location='eastus2euap')
    def test_network_manager_scope_connection(self, resource_group):
        tenant_id = self.cmd('account list --query "[?isDefault].tenantId" -o tsv').output.strip()
        self.kwargs.update({
            'connection_name': 'myTestScopeConnection',
            'manager_name': 'TestNetworkManager',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'tenant_id': tenant_id
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager scope-connection create --resource-group {rg} --network-manager-name {manager_name} '
                 '--name {connection_name} --description "My Test Network Manager Scope Connection" '
                 '--tenant-id {tenant_id} --resource-id {sub}')

        self.cmd('network manager scope-connection show -g {rg} --network-manager-name {manager_name} --name {connection_name}')

        self.cmd('network manager scope-connection update -g {rg} --network-manager-name {manager_name} '
                 '--name {connection_name} --description "My Test Network Manager Scope Connection Updated Description"')

        self.cmd('network manager scope-connection list -g {rg} --network-manager-name {manager_name} ')

        self.cmd('network manager scope-connection delete -g {rg} --network-manager-name {manager_name} --name {connection_name} --yes')

        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_connection_subscription', location='eastus2euap')
    def test_network_manager_connection_subscription(self, resource_group):

        self.kwargs.update({
            'subId': self.get_subscription_id(),
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'manager_name': 'TestNetworkManager',
            'connection_name': 'myTestNetworkManagerConnection'
        })

        network_manager = self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                                   '--scope-accesses "SecurityAdmin" "Connectivity" '
                                   '--network-manager-scopes '
                                   ' subscriptions={sub} '
                                   '-l eastus2euap '
                                   '--resource-group {rg}').get_output_in_json()
        self.kwargs['manager_id'] = network_manager['id']
        self.cmd('network manager connection subscription create --connection-name {connection_name} --description "My Test Network Manager Connection" --network-manager-id {manager_id}')

        self.cmd('network manager connection subscription show --connection-name {connection_name} ')

        self.cmd('network manager connection subscription update --connection-name {connection_name} --description "My Test Network Manager Connection Updated Description"')

        self.cmd('network manager connection subscription list')

        self.cmd('network manager connection subscription delete --connection-name {connection_name} --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_security_admin_config_v2', location='eastus2euap')
    def test_network_manager_security_admin_config_v2(self, resource_group):

        self.kwargs.update({
            'name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l eastus2euap '
                 '--resource-group {rg}')

        self.cmd('network manager security-admin-config create --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --display-name MyTestConfig --apply-on None',
                 checks=self.check('applyOnNetworkIntentPolicyBasedServices', '[\'None\']'))

        self.cmd('network manager security-admin-config update --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description "test_description" --apply-on None',
                 checks=self.check('applyOnNetworkIntentPolicyBasedServices', '[\'None\']'))
        self.cmd('network manager security-admin-config list --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-admin-config show --configuration-name {name} --network-manager-name {manager_name} -g {rg}')

        self.cmd('network manager security-admin-config delete --configuration-name {name} --network-manager-name {manager_name} -g {rg} --force --yes')
        self.cmd('network manager delete --resource-group {rg} --name {manager_name} --yes')
#     @ResourceGroupPreparer(name_prefix='test_network_manager_connection_crud', location='eastus2euap')
#     def test_network_manager_scope_connection(self, resource_group):
#
#         self.kwargs.update({
#             'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
#             'manager_id': '/subscriptions/{}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{connection_name}'.format(self.get_subscription_id()),
#             'manager_name': 'TestNetworkManager',
#             'connection_name': 'myTestNetworkManagerConnection',
#             'mgId': 'testManagementGroupId'
#         })
#
#         self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
#              '--scope-accesses "SecurityAdmin" "Connectivity" '
#              '--network-manager-scopes '
#              ' subscriptions={sub} '
#              '-l eastus2euap '
#              '--resource-group {rg}')
#
#         self.cmd('network manager connection create --management-group-id {mgId} --connection-name {connection_name} '
#                  '--description "My Test Network Manager Connection"'
#                  '--network-manager-id {manager_id}')
#
#         self.cmd('network manager connection show --management-group-id {mgId} --connection-name {connection_name} ')
#
#         self.cmd('network manager scope-connection update --management-group-id {mgId} --connection-name {connection_name} '
#                  '--description "My Test Network Manager Connection Updated Description"')
#
#         self.cmd('network manager scope-connection list --management-group-id {mgId} ')
#
#         self.cmd('network manager scope-connection delete --management-group-id {mgId} --connection-name {connection_name} ')