# 📘 Lab 2 — Gathering and Saving Cisco Device Facts (IOS + ASA)

## 🎯 Objective
This lab demonstrates how to use **Ansible** to automatically **collect Cisco device facts** (such as hostname, version, model, and interfaces) from **Cisco IOS and ASA** devices, and save the results to structured files for documentation or auditing purposes.

---

Medium Link: https://medium.com/@mickaelsoares/network-automation-with-ansible-collecting-cisco-device-facts-c7954990a2d1


---


## 🧰 Requirements
- Completion of **Lab 1** (Ansible environment configured)
- SSH access to Cisco IOS and ASA devices
- Inventory file (`inventory/hosts.ini`) already configured
- Python virtual environment activated (`source automation-env/bin/activate`)


---

## 📂 Directory Structure

```bash
ansible-lab/
├── inventory/
│   └── hosts.ini
├── playbooks/
│   └── gather_facts.yml
├── outputs/
│   ├── ios.json
│   └── asa.json
└── README.md
```

---

## ⚙️ Playbook: gather_facts.yml



---

## 🧩 Explanation

- Gather IOS device facts	Executes show version on IOS devices
- Save IOS facts to file	Saves the collected information to /outputs
- Gather ASA device facts	Executes show version on ASA firewalls
- Save ASA facts to file	Saves the collected information to /outputs

Each device produces a separate json file containing the full version details.


---

## ▶️ Run the Playbook

```bash
ansible-playbook -i inventory/hosts.ini playbooks/gather_facts.yml
```

---

## ✅ Expected Output

Example console output:




---

## 📁 Sample Output Files






---

## 🧠 Key Concepts

Conditional tasks (when) → differentiate commands for IOS and ASA

- cli_command module → runs any show or exec command on network devices
- copy module → saves command output to local files
- Facts storage → enables version tracking and device documentation


---

## 🚀 Next Steps

Lab 3 — Configuring NTP and Logging on Cisco IOS and ASA devices using Ansible.
