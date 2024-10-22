
import logging
from pyats import aetest
log = logging.getLogger(__name__)
from network_devices import Router, Switch


###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

class common_setup(aetest.CommonSetup):
    @aetest.subsection
    def create_devices(self):
        router = Router("MyRouter", "192.168.1.1")
        switch = Switch("MySwitch", "192.168.1.2")
        self.parent.parameters.update(router=router, switch=switch)

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class test_router_configuration(aetest.Testcase):
    @aetest.test
    def test_add_route(self, router):
        router.add_route("10.0.0.0/24", "192.168.1.10")
        assert "10.0.0.0/24" in router.routing_table, "Route has not been created"

class test_switch_vlan_configuration(aetest.Testcase):
    @aetest.test
    def test_create_vlan(self, switch):
        switch.create_vlan(10)
        assert switch.vlan == 10, "VLAN has not been created"

#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):

    @aetest.subsection
    def test_remove_route(self, router):
        router.remove_route("10.0.0.0/24")
        assert "10.0.0.0/24" not in router.routing_table, "Route has not been deleted"

    @aetest.subsection
    def test_delete_vlan(self, switch):
        switch.delete_vlan()
        assert switch.vlan is None, "VLAN has not been deleted "

    @aetest.subsection
    def clean_everything(self):
        log.info("Aetest Common Cleanup ")

if __name__ == '__main__':
    result = aetest.main()
    aetest.exit_cli_code(result)
