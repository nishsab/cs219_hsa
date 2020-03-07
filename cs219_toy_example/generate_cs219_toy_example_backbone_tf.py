'''
    <Generates all transfer functions for Stanford backbone network>

    Copyright 2012, Stanford University. This file is licensed under GPL v2 plus
    a special exception, as described in included LICENSE_EXCEPTION.txt.

Created on Aug 10, 2011

@author: Peyman Kazemian
'''

from examples.example_utils.cisco_tf_generator import generate_transfer_functions

settings = {
    "rtr_names":[
        "router0",
        "router1",
        "router2",
        "router3",
    ],
    "input_path":"cs219_toy_example_backbone",
    "output_path":"tf_cs219_toy_example_backbone",
    "topology":[
        ("router0", "te2/2", "router1", "te2/2"),
        ("router0", "te2/3", "router2", "te2/2"),
        ("router1", "te2/3", "router3", "te2/2"),
        ("router2", "te2/3", "router3", "te2/3"),
    ],
    #"replace_vlans":[None,None,None,None,(83,580),(83,580),None,None,None,None,None,None,(83,580),(83,580),None,None],
}
generate_transfer_functions(settings)
