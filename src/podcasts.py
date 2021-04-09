"""
Handles parsing of podcasts
"""
from collections import namedtuple

import feedparser
from prettytable import PrettyTable, ALL
from src.player import player


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


def podcast_extractor(podcast_link):
    """
    Returns a list of dictionary with episode number, episode title, and audio stream url
    :param podcast_link: rss feed link for the podcast.
    :return: [{'epi_numb': epi_numb, 'epi_title': epi_title, 'stream_url': stream_url},...]
    """

    all_episodes = []
    Episode = namedtuple('Episode', ['id', 'episode_title', 'episode_number', 'stream_url'])
    rss_feed = feedparser.parse(podcast_link)
    episode_entries = rss_feed.entries
    for index, episode_item in enumerate(episode_entries):
        all_episodes.append(
            Episode(id=index,
                    episode_title=episode_item.get('title', 'NULL'),
                    episode_number=episode_item.get('itunes_episode', 'NULL'),
                    stream_url=episode_item.links[-1].get('href', 'NULL')
                    )
        )

    return all_episodes


def print_episodes(episode_list):
    """
    A utility function to pretty print the episode data.
    :param episode_list: list of all episodes
    :return:
    """
    # Pretty print the episode data in table.
    pretty_episode_table = PrettyTable()
    pretty_episode_table.field_names = ['id', 'Title', 'Episode', 'Url']
    pretty_episode_table.add_rows(episode_list)
    pretty_episode_table.hrules = ALL

    pretty_episode_table.fields = ['id', 'Title', 'Episode']
    print(pretty_episode_table)


def main():
    """This will act as wrapper function, may change later when using @click"""
    episodes = podcast_extractor(podcast_urls['real_python'])
    print_episodes(episodes)
    # FIXME: use input validation provide by click.

    episode_id_choice = int(input("Enter the Episode ID to listen to the podcast ...\ndev-radio>"))
    print(f"Episode#:{episodes[episode_id_choice].episode_number} -- Title:{episodes[episode_id_choice].episode_title}")
    player(episodes[episode_id_choice].stream_url)


if __name__ == '__main__':
    # FIXME: convert timezone to local and add published date to episode data.
    # TODO: mvp is done, use click and write some tests to verify. Also check for other sites.
    main()
