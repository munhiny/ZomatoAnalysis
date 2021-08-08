from os import name
from bs4 import BeautifulSoup
import re

with open('page_source.html', 'r') as file:
    html = file.read()


def get_divs(html):
    divs = []
    soup = BeautifulSoup(html, 'html.parser')

    link_divs = soup.find_all('div',
                              {
                                  'class': 'sc-1mo3ldo-0'
                              }
                              )

    for i in link_divs:
        if '-omi-' in i:
            print('found')
    for link_div in link_divs:

        find_div = link_div.find('div',
                                 {
                                     'class': re.compile('sc-*')
                                 })
        if find_div:
            divs.append(find_div)
    return divs


def get_rest_link_data(divs):
    rest_link_data = []
    rest_links = []
    for i in divs:
        data = {}
        find_div = i.find('div',
                          {
                              'class': re.compile('sc-*')
                          }
                          )
        if find_div:
            next_div = find_div.find('div',
                                     {
                                         'class': re.compile('jumbo-tracker')
                                     }
                                     )
            if next_div:
                next_div2 = next_div.find('div',
                                          {
                                              'class': re.compile('sc-*')
                                          }
                                          ).find_all('a')[1]

                data['link'] = 'https://www.zomato.com' + next_div2['href']
                if '-omi-' in next_div2['href']:
                    print('found')

                rest_links.append(
                    'https://www.zomato.com' + next_div2['href'])
                next_div3 = next_div2.find_all('div',
                                               {
                                                   'class': re.compile('sc-*')
                                               }

                                               )

                data['name'] = next_div3[0].find('h4').text
                p_tags = (next_div2.find_all('p'))
                data['category'] = p_tags[0].text
                data['cost'] = p_tags[1].text
                data['location'] = p_tags[2].text.strip()
                data['rating'] = next_div3[1].find('div').find(
                    'div').find('div').find('div').find('div').text
                rest_link_data.append(data)

    return [rest_link_data, rest_links]


def tile_rest_data_scrape(html):
    divs = get_divs(html)
    for i in divs:
        if '-omi-' in i:
            print('found')
    data, links = get_rest_link_data(divs)
    # for i in links:
    #     print(i)
    # for i in data:
    #     print(i)

    print('data', len(data))
    print('link', len(links))

    if 'dominoes' in html:
        print('found')


def main():
    tile_rest_data_scrape(html)


if __name__ == "__main__":
    main()
