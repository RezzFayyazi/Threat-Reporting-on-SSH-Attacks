# Threat-Reporting-on-SSH-Attacks-with-LLMs

The goal of this project is to utilize Large Language Models (LLMs) for real-time threat analysis of SSH attacks. Initially, we configure the Cowrie honeypot to record commands entered into the SSH server. Next, we create a compilation of malicious SSH commands and categorize them according to the tactics and techniques outlined in the MITRE ATT&CK framework. Following this, these commands are inputted into the LLM, which is then tasked with interpreting and providing insights into the intentions behind each command. Finally, we compared the LLM responses with our own interpretation of the commands to verify the accuracy of the results.

In the "Data" folder, there is the "cowrie-log.txt," file which includes commands entered into the SSH server, recorded by Cowrie. This log's CMD section is extracted and input into the LLM in the "main.py" file.

The "SSH CMDS.pdf" contains the commands we generated and categorized them into MITRE ATT&CK's tactics and techniques to further validate the responses from the LLMs.
