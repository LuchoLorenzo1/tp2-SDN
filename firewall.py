from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventMixin
import json

log = core.getLogger()
UDP_CODE = 17
TCP_CODE = 6

class Firewall(EventMixin):
    def __init__(self, config):
        self.setUpFromConfig(config)
        self.listenTo(core.openflow)

    def setUpFromConfig(self, config):
        with open(config) as config_file:
            config_data = json.load(config_file)
            self.firewall_dpid = int(config_data["firewall_dpid"])
            self.multirule_port = int(config_data["multirule_port"])
            self.multirule_proto = int(config_data["multirule_proto"])
            self.multirule_host_ip = str(config_data["multirule_host_ip"])
            self.banned_ip1 = str(config_data["banned_ip1"])
            self.banned_ip2 = str(config_data["banned_ip2"])
            self.banned_port = int(config_data["banned_port"])

    def _handle_ConnectionUp(self, event):
        if event.dpid != self.firewall_dpid:
            return

        log.debug("El switch " + str(event.dpid) + " es el firewall")
        multiple_match = of.ofp_match(
            nw_src=self.multirule_host_ip, tp_dst=self.multirule_port, nw_proto=self.multirule_proto, dl_type=0x800
        )
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = multiple_match
        event.connection.send(flow_mod)

        match_ip = of.ofp_match(
            nw_src=self.banned_ip2, nw_dst=self.banned_ip1, dl_type=0x800
        )
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = match_ip
        event.connection.send(flow_mod)

        match_ip = of.ofp_match(
            nw_src=self.banned_ip1, nw_dst=self.banned_ip2, dl_type=0x800
        )
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = match_ip
        event.connection.send(flow_mod)

        match_port = of.ofp_match(tp_dst=self.banned_port, nw_proto=UDP_CODE, dl_type=0x800)
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = match_port
        event.connection.send(flow_mod)

        match_port = of.ofp_match(tp_dst=self.banned_port, nw_proto=TCP_CODE, dl_type=0x800)
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = match_port
        event.connection.send(flow_mod)


def launch(config="config.json"):
    core.registerNew(Firewall, config)
