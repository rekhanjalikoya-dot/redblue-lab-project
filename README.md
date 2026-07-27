# Red Team vs Blue Team – Cybersecurity Lab

A hands-on offensive/defensive security lab built using VirtualBox, simulating a real-world attack-and-defense scenario between an attacker machine and a target web application server.

# Objective

To simulate a controlled cyber attack on a vulnerable web application (DVWA) and demonstrate detection/defense mechanisms using firewall logging and intrusion prevention — showcasing both offensive (Red Team) and defensive (Blue Team) security skills.

# Lab Architecture

| Component        | Role              | OS / Tool                  |
|-------------------|-------------------|-----------------------------|
| Attacker Machine  | Red Team          | Kali Linux                 |
| Target Machine    | Blue Team         | Ubuntu Server + DVWA        |
| Network           | Isolated Network  | VirtualBox Internal Network (`redblue-lab`) |


Both VMs are connected on an isolated internal network (`redblue-lab`) so the lab is self-contained and does not expose the attack traffic to the host machine or the internet.

# 🛠️ Tools Used

- **Kali Linux** – Attacker OS, pre-loaded with pentesting tools
- **Nmap** – Network scanning and service/version enumeration
- **DVWA (Damn Vulnerable Web Application)** – Intentionally vulnerable web app used as the attack target
- **Burp Suite / Browser** – For manual SQLi and XSS exploitation
- **UFW (Uncomplicated Firewall)** – Logging and monitoring incoming traffic on the target
- **Fail2Ban** – Intrusion prevention, auto-banning IPs based on suspicious activity in logs

#  Red Team Phase — Attacks Performed

1. **Reconnaissance** – Nmap scan of the target to identify open ports and running services
2. **SQL Injection (SQLi)** – Exploited DVWA's SQLi module to extract database information
3. **Cross-Site Scripting (XSS)** – Injected malicious scripts via DVWA's XSS modules (Reflected/Stored)

#  Blue Team Phase — Detection & Defense

1. **UFW Logging** – Enabled and monitored UFW logs to detect incoming connection attempts and scan activity
2. **Fail2Ban** – Configured to monitor logs and automatically block IPs showing repeated malicious behavior
3. **Log Analysis** – Reviewed Apache/UFW logs to correlate attack timestamps with Red Team activity


#  Key Learnings

- Practical understanding of how common web vulnerabilities (SQLi, XSS) are exploited
- Hands-on experience configuring a firewall for logging and detection
- Understanding of how IPS tools like Fail2Ban use log patterns to block attackers
- Basics of setting up an isolated lab network for safe security testing

#  Disclaimer

This project was built strictly in an isolated, offline lab environment for educational purposes as part of an internship. All techniques were performed only against intentionally vulnerable systems (DVWA) owned and controlled by the author. None of these techniques should be used against systems without explicit authorization.

#  Author
Rekhanjali koya
HACKTECH Internship Project


