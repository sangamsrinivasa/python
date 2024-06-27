import subprocess
import datetime

def create_snapshot(vm_name):
    date = datetime.datetime.now().strftime("%Y%m%d")
    snapshot_name = f"{vm_name}_snapshot_{date}"
    subprocess.run(["virsh", "snapshot-create-as", vm_name, snapshot_name])
    print(f"Snapshot {snapshot_name} created for VM {vm_name}.")


if __name__ == "__main__":
    create_snapshot("test_vm"
