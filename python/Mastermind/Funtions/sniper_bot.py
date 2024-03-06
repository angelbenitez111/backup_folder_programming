from time import sleep
from requests_html import HTMLSession

url_coolmod_Radeon_RX_6600 = "https://www.coolmod.com/zotac-gaming-geforce-rtx-3090-arcticstorm-24gb-gddr6x-tarjeta-grafica/"
section = HTMLSession()


def buy_button_detector(section, url):
    while True:
        page = section.get(url)
        stock = page.html.find("div p#messageStock.m-0.off")
        print(stock)
        """if stock.text != "Agotado":
            print("We have stock")
        else:
            print("We do not have stock")"""


def main():
    buy_button_detector(section, url_coolmod_Radeon_RX_6600)


if __name__ == "__main__":
    main()
