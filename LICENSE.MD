
---

# 📂 Project 1 README.md (`Project1_Device_Version_Interface/README.md`)  

```markdown
# Project 1 - Device Version & Interface Status 🔍

## 🎯 Goal
The purpose of this project is to:
1. Retrieve the **software version** of each device.  
2. Gather the **operational state of interfaces**.  

---

## ⚙️ How It Works

- The script uses **Netmiko** to establish SSH connections.  
- Runs `show version` and filters output to extract only the relevant version string.  
- Runs `show ip int brief` (or `show interface ip brief` for ASA) to check interface states.  
- Handles different command outputs with conditional logic.  

---

## 📂 File Structure

