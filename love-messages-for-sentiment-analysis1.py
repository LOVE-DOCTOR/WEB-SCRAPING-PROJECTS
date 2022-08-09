from bs4 import BeautifulSoup
import requests
import pandas as pd
import neattext.functions as nfx

res = requests.get('https://parade.com/1045555/marynliles/romantic-love-messages-him-her/')
soup = BeautifulSoup(res.text, 'html.parser')

new_list = [soup.select('p')[i].text for i in range(3, 157)]

df = pd.DataFrame(columns=['text', 'label'])
df['text'] = new_list
df['label'] = ['love' for i in range(0, 154)]
df['text'] = df['text'].apply(nfx.remove_numbers)
df['text'] = df['text'].apply(nfx.remove_punctuations)
df['text'] = df['text'].replace('\xa0', '')

love_messages = [i for i in df['text']]
the_update = [i for i in love_messages if '“' not in i]
sweet_update = [i.split('—', 1)[0].split('―', 1)[0] for i in the_update]
final_update = [i.replace('\xa0', '') for i in sweet_update]
final_update1 = [i.rstrip() for i in final_update] 

for i in the_update:
    if i in new_list:
        love_messages.remove(i)

        
new_list1 = [i.replace('“', '').replace('”', '') for i in love_messages]
new_list2 = [i.split('—', 1)[0].split('–', 1)[0].split('―', 1)[0] for i in new_list1]
new_list3 = [i.rstrip() for i in new_list2]
new_list3

for i in final_update1:
    new_list3.append(i)
    
with open('love.txt', 'w', encoding='utf-8') as f:
    for x in new_list3:
        f.write(x+';love')
        f.write('\n')
