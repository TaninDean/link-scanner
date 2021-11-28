import sys
import urllib
from types import coroutine
from selenium import webdriver


def get_linked(url: str) -> list:
    """Method to get all hyperlink in URL.

    Args:
        url(str): string of page URL.
    Return:
        list_hyper(list): list that contains all hyperlink.
    """
    
    list_hyper = []
    browser = webdriver.Chrome()
    browser.get(url)
    a_tag = browser.find_elements_by_tag_name("a")
    for a in a_tag:
        link = a.get_attribute('href')
        if link == None:
            coroutine
        elif '?' in link:
            list_hyper.append(link.split('?')[0])
        elif '#' in link:
            if link.split('#')[0] != '':
                list_hyper.append(link.split('#')[0])
        else:
            list_hyper.append(link)
    return list_hyper


def is_valid_url(url: str) -> bool:
    """Validate the urls. 

    Return:
        bool: True
    """
    header = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
    request = urllib.request.Request(url, None, header)
    try:
        if urllib.request.urlopen(request).getcode() == 200:
            return True
        return False
    except urllib.error.HTTPError:
        return False


def invalid_urls(urllist: list[str]) -> list[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.

    Return:
        bad_url(list): list of bad url.
    """
    bad_url = []
    for url in urllist:
        if not is_valid_url(url):
            bad_url.append(url)
    return bad_url


if __name__ == '__main__':
    url = sys.argv[1]
    all_link = get_linked(url)
    bad_url = invalid_urls(all_link)
    for url in all_link:
        print(url)
    print('')
    print("Bad Links:")
    for url in bad_url:
        print(url)
