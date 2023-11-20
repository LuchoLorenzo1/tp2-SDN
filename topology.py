from mininet.topo import Topo


class MyTopo(Topo):
    def build(self, nSwitches=2):
        leftHost1 = self.addHost("lh1")
        leftHost2 = self.addHost("lh2")
        rightHost1 = self.addHost("rh1")
        rightHost2 = self.addHost("rh2")
        leftSwitch = self.addSwitch("s1")
        rightSwitch = self.addSwitch(f"s{nSwitches}")

        self.addLink(leftHost1, leftSwitch)
        self.addLink(leftHost2, leftSwitch)
        self.addLink(rightSwitch, rightHost1)
        self.addLink(rightSwitch, rightHost2)

        lastSwitch = leftSwitch
        for i in range(nSwitches - 2):
            newSwitch = self.addSwitch(f"s{i+2}")
            self.addLink(lastSwitch, newSwitch)
            lastSwitch = newSwitch
        self.addLink(lastSwitch, rightSwitch)


topos = {"mytopo": MyTopo}
