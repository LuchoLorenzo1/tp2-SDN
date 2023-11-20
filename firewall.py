from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventMixin
from pox.lib.addresses import IPAddr
import pox.lib.packet.packet_utils as pkt_ut

log = core.getLogger()


class Firewall(EventMixin):
    def __init__(self, config):
        self.setUpFromConfig(config)
        self.listenTo(core.openflow)

    def setUpFromConfig(self, config):
        self.firewall_dpid = 0
        self.banned_ip1 = 0
        self.banned_ip2 = 0
        self.host1_ip = 0

        with open(config) as config_file:
            for line in config_file:
                tokens = line.split("=")
                key, value = tokens[0], tokens[1].rstrip()
                if key == "firewall_dpid":
                    self.firewall_dpid = int(value)
                elif key == "banned_ip1":
                    self.banned_ip1 = value
                elif key == "banned_ip2":
                    self.banned_ip2 = value
                elif key == "host1_ip":
                    self.host1_ip = value

    def _handle_ConnectionUp(self, event):
        if event.dpid != self.firewall_dpid:
            log.debug("ESTE NO FUE ASIGNADO FIREWALL " + str(event.dpid))
            return
        log.debug("ESTE SI FUE ASIGNADO FIREWALL " + str(event.dpid))

        # match_ip = of.ofp_match()
        # match_ip.nw_src = (IPAddr(self.host1_ip), 32)
        # match_ip.nw_proto = 17
        # match_ip.tp_dst = 5001
        # flow_mod = of.ofp_flow_mod()
        # flow_mod.match = match_ip
        # event.connection.send(flow_mod)

        # match_ip = of.ofp_match()
        # match_ip.nw_src = (IPAddr(self.banned_ip2), 32)
        # match_ip.nw_dst = (IPAddr(self.banned_ip1), 32)
        # flow_mod = of.ofp_flow_mod()
        # flow_mod.match = match_ip
        # event.connection.send(flow_mod)

        # match_ip = of.ofp_match()
        # match_ip.nw_src = (IPAddr(self.banned_ip1), 32)
        # match_ip.nw_dst = (IPAddr(self.banned_ip2), 32)
        # flow_mod = of.ofp_flow_mod()
        # flow_mod.match = match_ip
        # event.connection.send(flow_mod)

        # match_port = of.ofp_match()
        # match_port.tp_dst = 80
        # flow_mod = of.ofp_flow_mod()
        # flow_mod.match = match_port
        # event.connection.send(flow_mod)


def launch(config="config.txt"):
    core.registerNew(Firewall, config)
