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

#  Red Team Phase — Attacks Performed

1. **Reconnaissance** – Nmap scan of the target to identify open ports and running services
2. **SQL Injection (SQLi)** – Exploited DVWA's SQLi module to extract database information
3. **Cross-Site Scripting (XSS)** – Injected malicious scripts via DVWA's XSS modules (Reflected/Stored)

#  Blue Team Phase — Detection & Defense

1. **UFW Logging** – Enabled and monitored UFW logs to detect incoming connection attempts and scan activity
2. **Log Analysis** – Reviewed Apache/UFW logs to correlate attack timestamps with Red Team activity
   
# Log Monitoring Script (log_monitor.py)
# What it does
This script performs real-time monitoring of the Apache access log 
(/var/log/apache2/access.log) on the target machine. It works like 
a simplified "tail -f" combined with basic pattern matching, acting 
as a lightweight custom IDS (Intrusion Detection System) for the lab.

# How it works
1. Opens the Apache access log file and seeks to the end (so it only 
   reads NEW lines, not old ones already in the file)
2. Continuously loops, reading one new line at a time as requests come in
3. If no new line is available, it waits 1 second and checks again
4. Checks each new log line (case-insensitive) for suspicious keywords:
   - "union"   -> indicates possible UNION-based SQL injection
   - "select"  -> indicates possible SQL query injection attempt
   - "1=1"     -> classic SQLi boolean bypass pattern
   - "script"  -> indicates possible XSS payload (<script> tag)
5. If a match is found, it prints an ALERT with the full log line

# Why these keywords
These four strings map directly to the Red Team attacks performed in 
this lab (SQLi and XSS on DVWA), so the script demonstrates detection 
of the exact attack traffic generated during the exercise.

# How to run
On the target (Ubuntu/Blue Team) machine:

    python3 log_monitor.py

Leave it running in a terminal while the attacker (Kali/Red Team) 
performs SQLi/XSS requests against DVWA. Matching requests will 
print immediately to the terminal as ALERT lines.

# Limitations (known, for future improvement)
- Keyword matching is case-insensitive but very basic — no regex, so 
  it can miss obfuscated payloads (e.g. URL-encoded %27, or SeLeCt)
- No logging to file — alerts only print to console and are lost 
  when the script stop
- Hardcoded log path and keyword list (not configurable via CLI args)

#  Key Learnings

- Practical understanding of how common web vulnerabilities (SQLi, XSS) are exploited
- Hands-on experience configuring a firewall for logging and detection
- Basics of setting up an isolated lab network for safe security testing

#  Disclaimer

This project was built strictly in an isolated, offline lab environment for educational purposes as part of an internship. All techniques were performed only against intentionally vulnerable systems (DVWA) owned and controlled by the author. None of these techniques should be used against systems without explicit authorization.

#  Author
Rekhanjali koya
HACKTECH Internship Project


