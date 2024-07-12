from bs4 import BeautifulSoup
import requests
import json

def parse_html():
    url = 'https://www.bbc.com/sport'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    data = []

    blocks = soup.find_all(class_='ssrcss-rs7w2i-ListItem e1gp961v0')

    for block in blocks[:5]:
        title = block.find(class_='ssrcss-1if1g9v-MetadataText e4wm5bw1').text.strip()
        url = block.find('a').get('href').strip()
        url = f'https://www.bbc.com{url}'

        print(f'Link: {url}, Topics: {title}')

        data.append({'Link': url, 'Topics': title})

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    parse_html()