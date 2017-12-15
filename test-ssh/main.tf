#The datacenter to deploy to
variable datacenter {
  default = "che01"
}

# The target operating system for the VSI
variable os {
  default = "UBUNTU_LATEST_64"
}

# The number of cores for the VSI
variable vm_cores {
  default = 4
}

# The amount of memory for the VSI
variable vm_memory {
  default = 4096
}

# The private vlan to deploy the virtual guests on to 
variable priv_vlan { 
  default = 1248
}

# The public vlan to deploy the virtual guests on to 
variable pub_vlan { 
  default = 1248
}

# The domain name for the virtual guests
variable domainname { 
  default = "ibm.com"
}

provider "softlayer" {}
data "softlayer_ssh_key" "sshkey" {
    label = "123457"
}

resource "softlayer_virtual_guest" "node" {
    name = "dedivstest"
    domain = "${var.domainname}"
    os_reference_code = "${var.os}"
    region = "${var.datacenter}"
    network_speed = 1000
    hourly_billing = true
    private_network_only = false 
    cpu = "${var.vm_cores}"
    ram = "${var.vm_memory}"
    disks = [100, 100]
    local_disk = true
    private_vlan_id = "${var.priv_vlan}"
    public_vlan_id = "${var.pub_vlan}"
    ssh_key_ids = ["${data.softlayer_ssh_key.sshkey.id}"]
    dedicated_host_id = 10401
}
