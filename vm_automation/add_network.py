import subprocess

def configure_network(vm_name, bridge_name):
    subprocess.run(["virsh", "net-update", "default", "add", "bridge", f"@{bridge_name}", "--live", "--config"])
    subprocess.run(["virsh", "attach-interface", vm_name, "bridge", bridge_name, "--config", "--live"])
    print(f"Network {bridge_name} configured and attached to VM {vm_name}.")


if __name__ == "__main__":
    configure_network("test_vm", "br0")

