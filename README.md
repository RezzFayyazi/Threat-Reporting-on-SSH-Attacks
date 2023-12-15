# Threat-Reporting-on-SSH-Attacks-with-LLMs

The goal of this project is to utilize Large Language Models (LLMs) for real-time threat analysis of SSH attacks. Initially, we configure the Cowrie honeypot to record commands entered into the SSH server. Next, we create a compilation of malicious SSH commands and categorize them according to the tactics and techniques outlined in the MITRE ATT&CK framework. Following this, these commands are inputted into the LLM, which is then tasked with interpreting and providing insights into the intentions behind each command. Finally, we compared the LLM responses with our own interpretation of the commands to verify the accuracy of the results.

In the "Data" folder, there is the "cowrie-log.txt" file, which is the command that is put into the SSH server and Cowrie logged it. We then extract the CMD part of that log and feed it into the LLM in the "main.py" file.

