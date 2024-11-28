def search_trusted(self, Q):
    for host, cert in self.trusted_certs.items():
        if Q == cert['public_key']:
            return True, host
    return False, None

def sign_point(self, g, d):
    return g * d

def connection_host(self, packet):
    d = packet['private_key']
    if abs(d) == 1:
        return "Private key is insecure, certificate rejected."
    packet_host = packet['host']
    curve = packet['curve']
    g = Point(*packet['generator'])
    Q = self.sign_point(g, d)
    cached, host = self.search_trusted(Q)
    if cached:
        return host
    else:
        self.trusted_certs[packet_host] = {
            "public_key": Q,
            "curve": "secp256r1",
            "generator": G
        }
        return "Site added to trusted connections"
...
def challenge(self, your_input):
    host = self.connection_host(your_input)
    if host == "www.bing.com":
        return self.bing_it(FLAG)
    else:
        return self.bing_it(host)