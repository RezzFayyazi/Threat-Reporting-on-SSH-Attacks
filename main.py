import openai
import time
import pandas as pd


def get_completion(prompt, model="gpt-4-1106-preview"):
    openai.api_key = "YOUR_API_KEY"
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


def prediction(csv_path):
    predictions = []
    df = pd.read_csv(csv_path)
    timestamp_command_list = []
    for timestamp, command in zip(df['timestamp'], df['commands']):
        timestamp_command_list.append((timestamp, command))

    prompt = f"""For the malicious SSH command below, what is the intent of adversaries on my system?

    SSH Command: {timestamp_command_list}

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
            time.sleep(10)
    return predictions

if __name__ == "__main__":
    predictions = prediction(csv_path='./Data/commands.csv')
    df = pd.DataFrame(predictions)    
    df.to_csv('./preds_gpt-4-turbo_prompt_only.csv', index=False)