from src.player import player
import json
from pathlib import Path
from prettytable import PrettyTable, ALL
import requests
from requests.exceptions import MissingSchema, ConnectionError

# noinspection SpellCheckingInspection
radio_urls = {'jpop': 'https://listen.moe/stream',
              'anime': 'https://s3.radio.co/sff133d65b/listen',
              'jhits': 'https://igor.torontocast.com/JapanHits',
              'jrock': 'https://kathy.torontocast.com:3340/;',
              'jpop0': 'https://kathy.torontocast.com:3560/;',
              'anime0': 'https://stream.laut.fm/animefm',
              'kpop': 'https://listen.moe/kpop/stream',
              'eurobeat': 'https://stream.laut.fm/eurobeat',
              'vocaloid': 'http://curiosity.shoutca.st:8019/stream',
              'synthwave': 'http://air.radiorecord.ru:805/synth_320',
              'synthwave0': 'https://stream.nightride.fm/nightride.m4a',
              'synthwave1': 'https://ecast.myautodj.com/public1channel',
              'dance': 'https://www.ophanim.net:8444/s/9780',
              'dance0': 'https://stream.laut.fm/dance',
              'dubstep': 'https://stream.24dubstep.pl/radio/8000/mp3_best',
              'dubstep0': 'https://radio.maddubz.net/radio/8000/dubstep.mp3',
              'dubstep1': 'https://ice6.somafm.com/dubstep-128-mp3',
              'country': 'https://pureplay.cdnstream1.com/6029_128.mp3',
              'amazing_80s': 'https://stream.amazingradios.com/80s',
              'heavy_metal': 'https://stream.laut.fm/metal',
              'lo_fi': 'https://laut.fm/lofi',
              'chill': 'https://stream.laut.fm/loungetunes',
              'hip_hop': 'https://stream.laut.fm/1000hiphop'
              }


# TODO: add comments and documentation.

def read_stations():
    """
    reads the radio station json file and returns dict.
    :return: dict{'radio_station': 'url'}
    """
    # REVIEW: probably fixed.
    file_path = Path(__file__).parent.parent / 'radio_stations.json'
    with open(file_path, 'r') as infile:
        old_radio_data = json.load(infile)
    return old_radio_data


def cli_radio_station_list():
    pretty_table = PrettyTable()
    pretty_table.hrules = ALL
    pretty_table.field_names = ["id", "Station"]
    station_list = list(read_stations().keys())
    station_list = [(index, station) for index, station in enumerate(station_list, start=0)]
    pretty_table.add_rows(station_list)
    print(pretty_table)


def station_config(operation, new_station_key, new_station_value=None):
    old_radio_data = read_stations()

    if operation.lower() == 'a':
        old_radio_data.update({new_station_key: new_station_value})
        print(f"Added new station {new_station_key} with url :: {new_station_value}")
    elif operation.lower() == 'd':
        try:
            popped_station = old_radio_data.pop(new_station_key)
        except KeyError:
            print(f"Station named {new_station_key} that you are trying to delete doesn't exist.")
        else:
            print(f"Station named {new_station_key} and url {popped_station} was deleted.")

    else:
        print("Incorrect Configuration Option.")

    # REVIEW: Probably Fixed
    file_path = Path(__file__).parent.parent / 'radio_stations.json'
    with open(file_path, 'w') as outfile:
        json.dump(old_radio_data, outfile, indent=4)


def cli_radio_play(station_name):
    station_url = read_stations().get(station_name)
    if station_url:
        print(f"Station :: {station_name}")
        player(station_url)
    else:
        print("Station name is incorrect, try again.")


def cli_add_station(station_name, station_url):
    try:
        resp = requests.get(station_url, stream=True)
    except MissingSchema:
        print("Stream url is incomplete ...")
    except ConnectionError:
        print("Either you are offline or the site is ...")
    except requests.exceptions.RequestException as e:
        print(e)
        print("There seems to be some problem with Url ...")
    else:
        station_config(operation='a', new_station_key=station_name, new_station_value=station_url)


def cli_del_station(station_name):
    station_config(operation='d', new_station_key=station_name)


def cli_reset_stations():
    file_path = Path(__file__).parent.parent / 'radio_stations.json'
    with open(file_path, 'w') as outfile:
        json.dump(radio_urls, outfile, indent=4)

    print("Radio stations are reset ...")


def cli_radio_check():
    media_extensions = ['audio/mpeg', 'audio/aac', 'application/ogg']
    radio_stations = read_stations()
    for station_name, station_url in radio_stations.items():
        resp_content_type = requests.get(station_url, stream=True).headers.get('Content-Type')
        if resp_content_type in media_extensions:
            print(f'[OK!] {station_name} ->>  {station_url}')
        else:
            print(f'[FAIL!] {station_name} ->>  {station_url}\nChange or delete this station.')


if __name__ == '__main__':
    ...
