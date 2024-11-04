from typing import List
import ifaddr

def get_network_ip() -> List[tuple[str,str]]:
    result = []
    ifs = ifaddr.get_adapters()
    for inter in ifs:
        if len(inter.ips) > 0:
            result.append((inter.name,inter.ips[0].ip))
    return result