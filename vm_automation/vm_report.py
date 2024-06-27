import subprocess
import json

def generate_vm_report():
    vms = subprocess.check_output(["virsh", "list", "--all", "--name"]).decode().split()
    report = {}
    for vm in vms:
        if vm:
            info = subprocess.check_output(["virsh", "dominfo", vm]).decode().split('\n')
            vm_info = {line.split(':')[0].strip(): line.split(':')[1].strip() for line in info if ':' in line}
            report[vm] = vm_info
    with open('vm_report.json', 'w') as report_file:
        json.dump(report, report_file, indent=4)
    print("VM report generated.")

if __name__ == "__main__":
    generate_vm_report()

