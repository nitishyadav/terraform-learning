provider "softlayer" {}

data "softlayer_ssh_key" "test2" {
    label = "test_ssh_key"
}

resource "softlayer_virtual_guest" "es-vm" {
    count                = "${var.node_count}"
    hostname                 = "es-vms123"
    domain               = "ibm.com"
    os_reference_code    = "UBUNTU_14_64"
    datacenter           = "${var.datacenter}"
    hourly_billing       = true
    cores                = 1
    memory               = 1024
    disks                = [25]
    local_disk           = true
    network_speed = 10
    ssh_key_ids  = ["${data.softlayer_ssh_key.test2.id}"]
    provisioner "remote-exec" {
        script = "es.sh"
    }
}

