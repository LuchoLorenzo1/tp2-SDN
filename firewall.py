from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventMixin
import json

log = core.getLogger()


class Firewall(EventMixin):
    def __init__(self, config):
        self.setUpFromConfig(config)
        self.listenTo(core.openflow)

    def setUpFromConfig(self, config):
        with open(config) as config_file:
            config_data = json.load(config_file)
            self.firewall_dpid = int(config_data["firewall_dpid"])
            self.host1_ip = str(config_data["host1_ip"])
            self.banned_ip1 = str(config_data["banned_ip1"])
            self.banned_ip2 = str(config_data["banned_ip2"])

    def _handle_ConnectionUp(self, event):
        if event.dpid != self.firewall_dpid:
            return

        log.debug("El switch " + str(event.dpid) + " es el firewall")
        multiple_match = of.ofp_match(
            nw_src=self.host1_ip, tp_dst=5001, nw_proto=17, dl_type=0x800
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

        match_port = of.ofp_match(tp_dst=80, nw_proto=17, dl_type=0x800)
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = match_port
        event.connection.send(flow_mod)

        match_port = of.ofp_match(tp_dst=80, nw_proto=6, dl_type=0x800)
        flow_mod = of.ofp_flow_mod()
        flow_mod.match = match_port
        event.connection.send(flow_mod)


def launch(config="config.json"):
    core.registerNew(Firewall, config)
