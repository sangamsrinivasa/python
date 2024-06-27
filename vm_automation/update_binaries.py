import subprocess

def update_vms(vm_list):
    for vm in vm_list:
        subprocess.run(["ssh", f"root@{vm}", "apt-get update && apt-get upgrade -y"])
        print(f"Updates applied to {vm}.")


if __name__ == "__main__":
    vms = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
    update_vms(vms)
