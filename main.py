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
        seed=1106
    )
    return response.choices[0].message["content"]


def prediction(csv_path):
    predictions = []
    df = pd.read_csv(csv_file)
    for command in df['Commands']:

        prompt = f"""For the malicious SSH command below, what is the intent of adversaries on my system?

        SSH Command: {command}

        Please break down the command into its components and explain the intent of the adversary. Finally, provide the MITRE ATT&CK tactic(s) that the adversary will achieve with this technique.
        """
        while True:
            try:

                print(question)
                result = get_completion(prompt)
                print(result,'\n')
                predictions.append(result)
                break
            except (openai.error.RateLimitError, openai.error.APIError, openai.error.Timeout,
                    openai.error.OpenAIError, openai.error.ServiceUnavailableError):
                time.sleep(10)
    return predictions

if __name__ == "__main__":
    list_of_questions = load_questions_from_csv('./Data/commands.csv')
    predictions = prediction(csv_path='./Data/commands.csv')
    df = pd.DataFrame(predictions)    
    df.to_csv('./preds_gpt-4-turbo_prompt_only.csv', index=False)