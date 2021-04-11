"""
Handles parsing of podcasts
"""
from collections import namedtuple

import feedparser
from prettytable import PrettyTable, ALL
from src.player import player
import requests
from requests import ConnectionError


podcast_urls = {
    'stackoverflow': 'https://feeds.simplecast.com/XA_851k3',
    'real_python': 'https://realpython.com/podcasts/rpp/feed',
    'python_bytes': 'https://pythonbytes.fm/episodes/rss_full_history',
    'talk_python': 'https://talkpython.fm/episodes/rss_full_history',
    'data_engineering': 'https://www.dataengineeringpodcast.com/feed/mp3/',
    'test_n_code': 'https://feeds.fireside.fm/testandcode/rss',
    'profitable_python': 'https://anchor.fm/s/c8df638/podcast/rss',
    'teaching_python': 'https://feeds.fireside.fm/teachingpython/rss',
    'python_podcast': 'https://www.pythonpodcast.com/feed/mp3/'
}


def read_podcasts():
    # MAYBE: maybe make podcast in file?
    return podcast_urls


def podcast_extractor(podcast_name):
    """
    Returns a list of namedtuple(Episode) with id, episode title, episode number, and stream url.

    :param podcast_name: rss feed link for the podcast.
    :return: [Episode(['id', 'episode_title', 'episode_number', 'date', 'stream_url'])]
    """
    podcast_link = read_podcasts().get(podcast_name)
    if podcast_link:
        try:
            requests.get(podcast_link)
        except ConnectionError:
            print("Either you are offline or the site is ...")
        except requests.exceptions.RequestException as e:
            print(e)
            print("Something went wrong, when accessing podcast ...")
        else:
            all_episodes = []
            Episode = namedtuple('Episode', ['id', 'episode_title', 'episode_number', 'date', 'stream_url'])

            rss_feed = feedparser.parse(podcast_link)
            episode_entries = rss_feed.entries
            for index, episode_item in enumerate(episode_entries):
                all_episodes.append(
                    Episode(id=index,
                            episode_title=episode_item.get('title', 'NULL'),
                            episode_number=episode_item.get('itunes_episode', 'NULL'),
                            date=' '.join(episode_item.get('published', 'NULL').split()[:-2]),
                            stream_url=episode_item.links[-1].get('href', 'NULL')
                            )
                )

            return all_episodes
    else:
        print("Incorrect podcast name, try again.")


def cli_print_episodes(podcast_name):
    """
    CLI facing function to pretty print the episode data.

    :param podcast_name:  podcast name from podcast dict.
    :return:
    """
    # FIXME: check the column width and other formatting issues for other podcasts.
    episode_list = podcast_extractor(podcast_name)
    if episode_list:
        pretty_table = PrettyTable()
        pretty_table.field_names = ['id', 'Title', 'Episode', 'Date', 'Url']
        pretty_table.add_rows(episode_list)
        pretty_table.hrules = ALL

        pretty_table.fields = ['id', 'Title', 'Episode', 'Date']
        print(pretty_table)


def cli_podcast_list():
    """
    CLI facing function to pretty print all available podcast name.

    :return:
    """
    pretty_table = PrettyTable()
    pretty_table.hrules = ALL
    pretty_table.field_names = ["id", "Podcast Name"]
    podcast_list = read_podcasts()
    podcast_list = [(index, podcast) for index, podcast in enumerate(podcast_list, start=0)]
    pretty_table.add_rows(podcast_list)
    print(pretty_table)


def cli_podcast_play(podcast_name, episode_id):
    """
    CLI facing function to play the podcast episode, when passed podcast name and episode id, (NOT episode number).

    :param podcast_name: name of the podcast.
    :param episode_id: id(index) of episode.
    :return:
    """
    episode = None
    episode_list = podcast_extractor(podcast_name)
    if episode_list:
        try:
            episode = episode_list[episode_id]
        except IndexError:
            print("Episode id is incorrect")
        except Exception as e:
            print(e)
            print("Something went wrong, when getting podcast episode data to play.")
        else:
            print(f"Episode:: {episode.episode_number} ->> Title:: {episode.episode_title}\nDate:: {episode.date}")
            player(episode.stream_url)


if __name__ == '__main__':
    cli_podcast_list()
