from player import player
import json

# noinspection SpellCheckingInspection
radio_urls = {'jpop_listen_moe': 'https://listen.moe/stream',
              'everything_weeb': 'https://s3.radio.co/sff133d65b/listen',
              'jhits': 'https://igor.torontocast.com/JapanHits',
              'jrock': 'https://kathy.torontocast.com:3340/;',
              'jpop_alter': 'https://kathy.torontocast.com:3560/;',
              'anime': 'https://stream.laut.fm/animefm',
              'kpop_listen_moe': 'https://listen.moe/kpop/stream',
              'eurobeat': 'https://stream.laut.fm/eurobeat',
              'vocaloid': 'http://curiosity.shoutca.st:8019/stream',
              'synthwave': 'http://air.radiorecord.ru:805/synth_320',
              'synthwave_alter': 'https://stream.nightride.fm/nightride.m4a',
              'synthwave_alter1': 'https://ecast.myautodj.com/public1channel',
              'dance': 'https://www.ophanim.net:8444/s/9780',
              'dance_alter': 'https://stream.laut.fm/dance',
              'dubstep': 'https://stream.24dubstep.pl/radio/8000/mp3_best',
              'dubstep_247': 'https://radio.maddubz.net/radio/8000/dubstep.mp3',
              'dubstep_alter': 'https://ice6.somafm.com/dubstep-128-mp3',
              'country': 'https://pureplay.cdnstream1.com/6029_128.mp3',
              'amazing_80s': 'https://stream.amazingradios.com/80s',
              'heavy_metal': 'https://stream.laut.fm/metal',
              'lo_fi': 'https://laut.fm/lofi',
              'chill': 'https://stream.laut.fm/loungetunes',
              'hip_hop': 'https://stream.laut.fm/1000hiphop'
              }

'''
everything_weeb contains, classic, modern anime, city pop, eurobeat and video game music.
'''

# TODO: convert this file to JSON file, and add options to write to file.


def read_stations():
    """
    reads the radio station json file and returns dict.
    :return: dict{'radio_station': 'url'}
    """
    with open('../radio_stations.json', 'r') as infile:
        old_radio_data = json.load(infile)
    return old_radio_data


def station_config(operation, new_station_key, new_station_value=None):
    old_radio_data = read_stations()
    # TODO: use input validation for operation inside click, this is temp solution.
    if operation.lower() == 'a':
        old_radio_data.update({new_station_key: new_station_value})
    elif operation.lower() == 'd':
        old_radio_data.pop(new_station_key)
        # TODO: handle exception for keyerror.
    else:
        print("Incorrect Configuration Option.")
        # TODO: Raise custom exception

    with open('../radio_stations.json', 'w') as outfile:
        json.dump(old_radio_data, outfile, indent=4)
        # TODO: print different message based on type of operation performed.
        print("Added new radio stations ...")


if __name__ == '__main__':
    # station_config('d', 'test_radio', 'test_URLRLGDKDG')
    # player(radio_urls['jpop_alter'])

    # Testing
    player(read_stations()['anime'])
