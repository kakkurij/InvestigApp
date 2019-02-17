import requests
from bs4 import BeautifulSoup
from share import share

url = "https://fi.investing.com/equities/"


def element_as_list(data):
    """ 
    Transforms html- element to list
    :param data - htlm element, that has correct information
    :return Information as list
    """
    dataList = []
    for i in data:

        name = ""
        info = i.get_text(separator=" ").split()
        foo = []
        for ind, j in enumerate(info):
            if "," not in j and "/" not in j and ":" not in j:
                # We have a part of the name (or last part)
                if ind is 0:
                    name = j
                else:
                    name += " " + j

            else:
                # We have a float which is type 3,44
                foo.append(j)

        foo.insert(0, name)
        dataList.append(foo)

    # print(foo)
    return dataList


def get_info(url_):
    """ 
    Get's information from spesicied website
    :return returns a list of share-objects
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    r = requests.get(url=url_, headers=headers)

    soup = BeautifulSoup(r.content, "html5lib", from_encoding='utf-8')

    elements = soup.find("div", {"id": "marketInnerContent"})
    table = elements.find_all("tr")

    shares = []

    data = element_as_list(table)

    for i in data:
        try:

            shares.append(share(i[0], i[1], i[3], i[2], i[4]))
        except IndexError:
            data.remove(i)
            continue

    return shares


# "change" = change since yesterday as procents
stock_list = get_info(url)

for osake in stock_list:
    print(osake)
