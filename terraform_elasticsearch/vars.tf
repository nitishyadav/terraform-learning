variable node_count {
    default = 1
}

variable port {
    default = 9200
}

variable backend_subnet {
    default = "10.162.75.64/26"
}

variable backend_vlan_number {
    default = 1248
}

variable backend_primary_router_hostname {
    default = "bcr01a.che01"
}

variable ssh_key_label {
    default = "test_ssh_key_name"
}

variable datacenter {
    default = "che01"
}
