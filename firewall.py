from pox.core import core
from pox.openflow import ConnectionUp, PacketIn
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.addresses import EthAddr
import pox.lib.packet as pkt

log = core.getLogger()

# MAC addresses pairs for blocking traffic between them
rules = [
    ["00:00:00:00:00:01", "00:00:00:00:00:02"],
    # ["00:00:00:00:00:02", "00:00:00:00:00:04"],
    # ["00:00:00:00:00:08", "00:00:00:00:00:03"],
    # ["00:00:00:00:00:07", "00:00:00:00:00:02"],
]


class SDNFirewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)

    def _handle_ConnectionUp(self, event):
        packet = event.source
        log.debug(packet)
        log.debug(event)

        for rule in rules:
            block = of.ofp_match()
            block.dl_src = EthAddr(rule[0])
            block.dl_dst = EthAddr(rule[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)

    def _handle_PacketIn(self, event):
        packet = pkt.udp(event.data)
        if packet is not None:
            log.debug(packet.srcport)
            log.debug(packet.dstport)


def launch():
    core.registerNew(SDNFirewall)
