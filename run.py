import json
import random
import telegram
from os import getenv


class Adv:
    message = None
    link = None

    def __init__(self, message, link):
        self.message = message
        self.link = link

    def build_message(self):
        return '{}[Открыть]({})'.format(self.message, self.link)


if __name__ == '__main__':
    adv_list = None
    with open('adv_source.json', 'r') as f:
        adv_list = json.loads(f.read())

    selected_adv = random.choice([Adv(**adv) for adv in adv_list['adv_list']])

    message = selected_adv.build_message()

    bot = telegram.Bot(getenv('BOT_TOKEN'))

    bot.send_message(format(getenv('TELEGRAM_CHANNEL')), message, parse_mode=telegram.ParseMode.MARKDOWN,
                     disable_notification=True)
