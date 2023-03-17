import os
import openai
import pdb


MODEL='gpt-3.5-turbo'

# Although the library contains the same code as below, we have
# kept it here for easy reference.
openai.api_key = os.getenv("OPENAI_API_KEY")

# read spec
with open('spec.md', 'r') as f:
    spec = f.read()

# I reckon that if we employ gpt-4, there would be no need
# to furnish coordinates. Nevertheless, there remains a degree
# of uncertainty. The response may include unforeseen explanations
# that could influence the parsing of the api endpoint. It all
# hinges on how well the model grasps your intent. I surmise that
# this aspect should see significant enhancement in forthcoming models.
objects = '''
現在輸入的資料如下，請產生對應的 Api 呼叫，注意僅回傳 api 不需要補充說明

(0, 10), (1024, 120), 鐵軌
(0, 60), (60, 190), 柵欄
(1000, 600), (1050, 650), 車子
'''

resp = openai.ChatCompletion.create(model=MODEL,
        temperature = 0, # deterministic answer
        messages=[{"role": "user", "content": spec+objects}])

content = resp['choices'][0]['message']['content']

# Parse the content and ensure that there are no blank entries.
# This assumes that the returned content only contains HTTP 
# endpoint information.
apis = list(filter(lambda x: x!='', content.split('\n')))

# well, the following api will be expected to call directly
for api in apis:
    print(api)
