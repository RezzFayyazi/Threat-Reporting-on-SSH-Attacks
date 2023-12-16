# Threat-Reporting-on-SSH-Attacks-with-LLMs

The goal of this project is to utilize Large Language Models (LLMs) for real-time threat analysis of SSH attacks. This project utilizes the configuration of a Linux VM containing an SSH Cowrie honeypot to record attack commands entered into an example SSH server. Next, we create a compilation of malicious SSH commands and categorize them according to the tactics and techniques outlined in the MITRE ATT&CK framework. Following this, these commands are inputted into the LLM, which is then tasked with interpreting and providing insights into the intentions behind each command. Finally, we compared the LLM responses with our own interpretation of the commands to verify the accuracy of the results.

The proof of concept for this project was constructed within a Ubuntu virtual machine. This machine served as the host of the SSH server. We chose a Cowrie Honeypot as an SSH endpoint to sandbox the SSH environment and log all input commands for intake by the LLM.

The LLM prompt script was also hosted on the virtual machine. In the "Data" folder, there is the "cowrie-log.txt," file which includes commands entered into the SSH server, recorded by Cowrie. This log's CMD section is extracted and input into the LLM in the "main.py" file.

The "SSH CMDS.pdf" contains the commands we generated and categorized them into MITRE ATT&CK's tactics and techniques to further validate the responses from the LLMs.
