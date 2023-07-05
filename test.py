# import openai
# #%%
# import yaml
# with open('openapi.yml','r',encoding='utf8') as f:
#     openai_config = yaml.safe_load(f)
# openai.organization = openai_config['ORG_KEY']
# openai.api_key = openai_config['API_KEY'] # 회사꺼
# #%%
# string = '\n'.join(list(map(lambda x: f'"{x[2]}"', train_data[:1])))
# #%%
# string
# #%%
# res = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo', messages = [
#         { 'role': 'system', 'content': 'you are helpful korean to english translate assistant' },
#         { 
#             'role': 'user', 
#             'content' : f'각 문장에서 ""안의 문장만 영어로 번역해줘\n{string}'
#         },
#     ]
# )
# # %%
# res.choices[0].message.content.split('\n')
# # %%
#%%
import json

# data loader
with open('./KorQuAD_v1.0_train.json') as f:
    train = json.load(f)

with open('./KorQuAD_v1.0_dev.json') as f:
    valid = json.load(f)

## data preproc
train_data = []

for data in train['data']:
    for idx, parag in enumerate(data['paragraphs']):
        train_data.append((data['title'], parag['context'], [qas['question'] for qas in parag['qas']]))

valid_data = []

for data in valid['data']:
    for idx, parag in enumerate(data['paragraphs']):
        valid_data.append((data['title'], parag['context'], [qas['question'] for qas in parag['qas']]))
#%%
wikis = list(set(map(lambda x: x[0], train_data)))
# %%
wikis[0]
# %%
import wikipediaapi
from time import sleep
from tqdm import tqdm
import random
# %%
wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'ko')
# %%
docs = []
for idx, doc in tqdm(enumerate(wikis), total=len(wikis)):
    docs.append(wiki.page(doc).text)
    if idx % 100 == 0:
        sleep(random.random())
# %%
