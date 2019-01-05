import requests
import bs4


def get_animals():
    animals = set()
    animals.update(get_a_to_z_animals())
    return animals


def get_a_to_z_animals(do_trim=False):
    animals = set()
    response = requests.get('https://a-z-animals.com/animals/')
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    letter_divs = soup.find_all('div', class_='letter')
    for letter_div in letter_divs:
        ul = letter_div.find_all('ul')[0]
        for li in ul:
            animal = li.getText()
            if do_trim:
                words = animal.split(' ')
                if len(words) > 1:
                    animal = words[-1]
            animals.add(animal)
    return animals


if __name__ == '__main__':
    print(get_a_to_z_animals())
