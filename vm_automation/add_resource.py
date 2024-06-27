import libvirt
import xml.etree.ElementTree as ET

def set_vm_resources(vm_name, vcpus, memory):
    conn = libvirt.open('qemu:///system')
    dom = conn.lookupByName(vm_name)
    xml = dom.XMLDesc()
    tree = ET.fromstring(xml)

    tree.find('./vcpu').text = str(vcpus)
    tree.find('./memory').text = str(memory * 1024)
    tree.find('./currentMemory').text = str(memory * 1024)

    dom.defineXML(ET.tostring(tree).decode('utf-8'))
    print(f"Resources updated for VM {vm_name}: {vcpus} vCPUs, {memory} MB RAM")


if __name__ == "__main__":
    set_vm_resoures("test_vm", 4, 8192)
