# 🧩 Lab 1 — Initial Ansible Setup and Network Inventory

## 🎯 Objective
This lab sets up the foundational automation environment using **Ansible** to manage Cisco network devices (routers, switches, and firewalls).  
The goal is to create an inventory, validate SSH connectivity, and run the first network command remotely.
![Lab Topology](https://github.com/user-attachments/assets/36e89821-ea19-4e52-8852-77fdf1c059f3)

🌐 Medium link: https://medium.com/@mickaelsoares/network-automation-with-ansible-lab1-basic-inventory-b12deb73cc03
---

## 🧰 Requirements
- **Ubuntu 22.04+** or compatible Linux system  
- **Python 3.9+**
- **Ansible 2.14+**
- SSH access to Cisco devices (IOS / ASA)
- Python virtual environment

---

## ⚙️ Setup Steps

### 1️⃣ Create a virtual environment
```bash
python3 -m venv automation-env
source automation-env/bin/activate
```

2️⃣ Install dependencies
```bash
pip install ansible paramiko netmiko ansible-pylibssh
```

3️⃣ Directory structure
```bash
ansible-lab/
├── inventory/
│   └── hosts.ini
├── playbooks/
│   └── test_connectivity.yml
└── README.md
```

4️⃣ Define the inventory
File: inventory/hosts.ini

5️⃣ Create the test playbook
File: playbooks/test_connectivity.yml

6️⃣ Run the playbook
```bash
ansible-playbook -i inventory/hosts.ini playbooks/test_connectivity.yml
```

✅ Expected Result
Ansible should connect to all network devices and return the show version output for each.

📷 Test result: Recap Table
<img width="941" height="132" alt="lab1_test_result_4" src="https://github.com/user-attachments/assets/a67925d5-9d15-4178-851a-f11cb3735b75" />


🧠 Key Concepts
Inventory file: defines groups of devices and connection variables.

- cli_command module: used to send CLI commands to network devices.
- network_cli connection: uses SSH with privilege elevation (enable mode).

🚀 Next Steps
- Lab 2: Gathering Facts using Ansible.
- Lab 3: Configure NTP and Logging using Ansible.
- Lab 4: Configure VLANS and Trunks on Cisco Switches.

📚 References
- Ansible Network Getting Started Guide - https://docs.ansible.com/ansible/latest/network/getting_started/index.html
- Cisco DevNet — Network Automation - https://developer.cisco.com/learning/
