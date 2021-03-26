from player import player

# noinspection SpellCheckingInspection
radio_urls = {'jpop_listen_moe': 'https://listen.moe/stream',
              'everything_weeb': 'https://s3.radio.co/sff133d65b/listen',
              'jpop_alter': 'https://streamingv2.shoutcast.com/japanimradio',
              'anime': 'https://stream.laut.fm/animefm',
              'kpop_listen_moe': 'https://listen.moe/kpop/stream',
              'eurobeat': 'https://stream.laut.fm/eurobeat',
              'vocaloid': 'http://curiosity.shoutca.st:8019/stream',
              'synthwave': 'http://air.radiorecord.ru:805/synth_320',
              'synthwave_alter': 'https://stream.nightride.fm/nightride.m4a',
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
everthing_weeb contains, classic, modern anime, city pop, eurobeat and video game music.
'''

if __name__ == '__main__':
    player(radio_urls['lo_fi'])
