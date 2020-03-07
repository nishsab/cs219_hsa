'''
    <Run reachability test on Stanford network>

    Copyright 2012, Stanford University. This file is licensed under GPL v2 plus
    a special exception, as described in included LICENSE_EXCEPTION.txt.


Created on Aug 14, 2011

@author: Peyman Kazemian
'''
from examples.example_utils.network_loader import load_network
from config_parser.cisco_router_parser import cisco_router
from utils.wildcard import wildcard_create_bit_repeat
from utils.wildcard_utils import set_header_field
from headerspace.hs import headerspace
from time import time
from headerspace.applications import find_reachability,print_paths

settings = {
    "rtr_names":[
        "router0",
        "router1",
        "router2",
        "router3",
    ],
    "input_path":"tf_nishant_backbone",
    "num_layers":3,
    "fwd_engine_layer":2,
    "switch_id_multiplier":cisco_router.SWITCH_ID_MULTIPLIER,
    "port_type_multiplier":cisco_router.PORT_TYPE_MULTIPLIER,
    "out_port_type_const":cisco_router.OUTPUT_PORT_TYPE_CONST,
    "remove_duplicates":True,
}

(ntf,ttf,name_to_id,id_to_name) = load_network(settings)

# create all-x packet as input headerspace.
all_x = wildcard_create_bit_repeat(ntf.length,0x3)
# uncomment to set some field
#set_header_field(cisco_router.HS_FORMAT(), all_x, "field", value, right_mask)
set_header_field(cisco_router.HS_FORMAT(), all_x, "vlan", 10, 0)
test_pkt = headerspace(ntf.length)
test_pkt.add_hs(all_x)

#set some input/output ports
output_port_addition = cisco_router.PORT_TYPE_MULTIPLIER * \
cisco_router.OUTPUT_PORT_TYPE_CONST
src_port_id = name_to_id["router0"]["te2/1"]
dst_port_ids = [name_to_id["router2"]["te2/3"]+output_port_addition]

#start reachability test and print results
st = time()
paths = find_reachability(ntf, ttf, src_port_id, dst_port_ids, test_pkt)
en = time()
print_paths(paths, id_to_name)

print "Found ",len(paths)," paths in ",en-st," seconds."
