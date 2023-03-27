import requests
import openai

# 請將以下 API_KEY 替換為您的 OpenAI API 密鑰
openai.api_key = "your_openai_api_key"

def call_api(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"API called successfully: {response.url}")
    else:
        print(f"API call failed with status code: {response.status_code}")

def generate_description(image_data):
    prompt = f"描述以下影像輸入數據：\n{image_data}\n描述："
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    if response.choices:
        return response.choices[0].text.strip()
    return "無法生成描述"

def main():
    # 資料模擬，需替換為實際影像輸入數據
    image_data = [((100, 200), (300, 400), "car")]

    description = generate_description(image_data)

    # 柵欄放下
    fence_action_down = "http://10.1.1.12:3000/apis/fence?action=down"
    call_api(fence_action_down)

    # 鳴笛
    sound_params = {"level": 10, "duration": 5}
    sound_api = "http://10.1.1.11:3000/apis/sound"
    call_api(sound_api, params=sound_params)

    # 通報交通管制中心
    report_params = {"description": description}
    report_api = "http://10.1.1.13:3000/apis/report"
    call_api(report_api, params=report_params)

if __name__ == "__main__":
    main()
