import requests
import json
from config import keys

class ConvertionException(Exception):
    pass


class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException('Вы пытаетесь конвертировать одинаковые валюты, не надо так! ;) ')
        try:
            quote_tik = keys[quote]
            base_tik = keys[base]
        except KeyError:
            raise ConvertionException(
                'Вы запросили конвертацию не потдерживаемой валюты! \nЧто бы узнать потдерживаемые конвертером валюты, воспользуйтесь командой /values')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tik}&tsyms={base_tik}')

        try:
            amount = float(amount)

        except ValueError:
            raise ConvertionException(
                'Вы не правильно ввели количество конвертируемой валюты!\nЧто бы уточнить как правельно вводить запрос, воспользуйтесь командой /help')

        t_base = float(json.loads(r.content)[keys[base]]) * amount

        return t_base