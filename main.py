import openai
import requests
import re

def main():
    # Replace this with your actual OpenAI API key
    openai.api_key = "your_openai_api_key"

    # Retrieve natural language description from OpenAI
    prompt = ("Describe the actions to take for the railway crossing safety control system, "
              "including fence actions, sound actions, and report actions. Use the following format:\n"
              "fence [up|down|pause|break]; sound level [1-10] duration [1-360]; report [description].")

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Assuming the first response is the most relevant
    natural_language_description = response.choices[0].text.strip()

    # Process the natural language description and make API calls
    process_description_and_call_apis(natural_language_description)

def process_description_and_call_apis(description):
    # Detect possible actions in the description
    fence_action = re.search(r"fence (up|down|pause|break)", description)
    sound_action = re.search(r"sound level (\d) duration (\d+)", description)
    report_action = re.search(r"report (.+)", description)

    # Call the appropriate APIs based on the detected actions
    if fence_action:
        action = fence_action.group(1)
        response = requests.get(f"http://10.1.1.12:3000/apis/fence?action={action}")
        print(f"Fence API called with action '{action}'. Response: {response.text}")

    if sound_action:
        level = sound_action.group(1)
        duration = sound_action.group(2)
        response = requests.get(f"http://10.1.1.11:3000/apis/sound?level={level}&duration={duration}")
        print(f"Sound API called with level '{level}' and duration '{duration}'. Response: {response.text}")

    if report_action:
        description = report_action.group(1)
        response = requests.get(f"http://10.1.1.13:3000/apis/report?description={description}")
        print(f"Report API called with description '{description}'. Response: {response.text}")

if __name__ == "__main__":
    main()
