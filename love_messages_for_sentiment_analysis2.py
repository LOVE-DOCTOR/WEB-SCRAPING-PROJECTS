res = requests.get('https://www.southernliving.com/culture/romantic-love-messages-for-him-and-her')
soup = BeautifulSoup(res.text, 'html.parser')
new_list = [soup.select('li')[i].text for i in range(114, 239)]

df = pd.DataFrame(columns=['text'])
df['text'] = new_list
df['text'] = df['text'].apply(nfx.remove_numbers)
df['text'] = df['text'].apply(nfx.remove_emojis)
df['text'] = df['text'].replace('\xa0', '')

list__ = [i.split('–', 1)[0].split('—', 1)[0] for i in df['text']]
list___ = [i.replace('"', '') for i in list__]
list_list = [i.rstrip() for i in list___]

with open('love.txt', 'w', encoding='utf-8') as f:
    for x in list_list:
        f.write(x+';love')
        f.write('\n')
