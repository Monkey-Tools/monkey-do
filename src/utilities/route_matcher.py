"""Route parsing for parameterized routes"""


def routes_match(config_route: str, request_route: str) -> bool:
    """checks if the routs match, ignores parameterized portions of the route"""
    config_route_chunks = config_route.split('/')
    request_route_chunks = request_route.split('/')
    crc_len = len(config_route_chunks)
    rrc_len = len(request_route_chunks)
    if crc_len != rrc_len:
        return False
    for i in range(crc_len):
        if '{' not in config_route_chunks[i] and \
           '}' not in config_route_chunks[i] and \
           config_route_chunks[i] != request_route_chunks[i]:
            return False
    return True
