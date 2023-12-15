import openai
import time
import pandas as pd
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

def get_completion(prompt, model="gpt-4-1106-preview"):
    openai.api_key = config.get('API', 'OpenAI_Key')
    messages = [{"role": "system", 
                 "content":"You are a cybersecurity expert with an in-depth knowledge about SSH attacks."},
                {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        seed=42
    )
    return response.choices[0].message["content"]

def extract_commands(file_path):
    commands = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines and "CMD: " in lines[-1]:
            command = lines[-1].split("CMD: ")[1].strip()
            commands.append(command)
    return ' '.join(commands)

def read_num(file_path):
    try:
        with open(file_path, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 1  # Return 1 if the file doesn't exist

def write_num(file_path, num):
    with open(file_path, 'w') as file:
        file.write(str(num))

def prediction(file_path):
    predictions = []
    extracted_commands = extract_commands(file_path)
    print(extracted_commands)
    
    prompt = f"""For the malicious SSH command below, what is the intent of adversaries on my system?

    SSH Command: {extracted_commands}

    Please break down the command into its components and explain the intent of the adversary. Finally, provide the MITRE ATT&CK tactic(s) that the adversary will achieve with this technique.
    """
    while True:
        try:

            print(prompt)
            result = get_completion(prompt)
            print(result,'\n')
            predictions.append(result)
            break
        except (openai.error.RateLimitError, openai.error.APIError, openai.error.Timeout,
                openai.error.OpenAIError, openai.error.ServiceUnavailableError):
            time.sleep(3)
    return predictions

if __name__ == "__main__":
    num_file_path = './Data/last_num.txt'
    num = read_num(num_file_path)
    file_path = f'./Data/cowrie-log.txt'
    
    predictions = prediction(file_path)
    df = pd.DataFrame(predictions)
    print(df)
    df.to_csv(f'./Results/threat_report_{num}.csv', index=False)
    
    num += 1
    write_num(num_file_path, num)