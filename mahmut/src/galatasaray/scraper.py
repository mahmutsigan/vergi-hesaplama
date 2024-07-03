import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.mackolik.com/takim/galatasaray/ma%C3%A7lar/esa748l653sss1wurz5ps3228"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    css_selector = 'tbody > tr[data-match-type] div[class="p0c-team-matches__teams"]'

    for match in soup.select(css_selector):
        print(match.text)


if __name__ == '__main__':
    main()
