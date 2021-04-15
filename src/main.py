import click
from src.radio_stations import (
    cli_radio_station_list,
    cli_radio_play,
    cli_add_station,
    cli_del_station,
    cli_reset_stations,
    cli_radio_check,
    cli_ren_station,
)
from src.podcasts import cli_podcast_list, cli_print_episodes, cli_podcast_play

"""Entry point for dev-radio."""


class AliasedGroup(click.Group):
    """
    A class for creating aliases for commands.
    """

    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)


@click.group(cls=AliasedGroup)
def dradio():
    """
    dev-radio is simple command line tool to listen to python podcast and radio streams.
    Use --help with Commands to get their help.
    """
    pass


radio_play_help = """Pass the radio station name, to start playing radio.

\b
Example: dradio radio --play <radio_station_name>
"""
radio_add_help = """Add new radio station by passing radio_name and radio_url, resp

\b
Example: dradio radio --add-station <radio_station_name> <radio_station_url>
"""
radio_del_help = """Deletes the radio station of the said name.

\b
Example: dradio radio --del-station <radio_station_name>
"""
radio_ren_help = """Renames the radio station. This just performs delete and add station.

\b
Example: dradio radio --rename-station <old_station_name> <new_station_name>
"""


@dradio.command(help="ALIAS: rad, Plays radio streams.")
@click.option(
    "--list", "-L", "list_", is_flag=True, help="Lists all the radio stations."
)
@click.option("--play", "-P", type=str, help=radio_play_help)
@click.option(
    "--add-station", "-A", "add_station", nargs=2, type=str, help=radio_add_help
)
@click.option("--del-station", "-D", "del_station", type=str, help=radio_del_help)
@click.option(
    "--rename-station", "-R", "ren_station", nargs=2, type=str, help=radio_ren_help
)
@click.option(
    "--reset",
    is_flag=True,
    help="Resets all the radio stations to default state, may come in handy if you delete some stations.",
)
@click.option(
    "--check", "-C", is_flag=True, help="Checks which radio urls are working."
)
def radio(list_, play, add_station, del_station, ren_station, reset, check):
    if list_:
        cli_radio_station_list()
    elif play:
        cli_radio_play(play)
    elif add_station:
        print("Wait for a few seconds, checking if the url is online ...")
        cli_add_station(add_station[0], add_station[1])
    elif del_station:
        if click.confirm(f"Do you want to delete {del_station} station?", abort=True):
            cli_del_station(del_station)
    elif ren_station:
        cli_ren_station(ren_station[0], ren_station[1])
    elif reset:
        if click.confirm("Do you want to reset all radio stations?", abort=True):
            cli_reset_stations()
    elif check:
        cli_radio_check()


podcast_play_help = """Pass the podcast name and episode_id (NOT the episode_number) to play the episode,
resp. pass <podcast_episode_id> as 0 for latest episode.

\b
Example: dradio podcast <podcast_name> <podcast_episode_id>
"""


@dradio.command(help="ALIAS: pod, Plays podcasts.")
@click.option("--list", "-L", "pod_list_", is_flag=True, help="Lists all the podcasts.")
@click.option(
    "--all-eps",
    "-A",
    "eps",
    type=str,
    help="Shows all the episodes of podcast <podcast_name>",
)
@click.option(
    "--play", "-P", type=(str, int), default=(None, None), help=podcast_play_help
)
def podcast(pod_list_, eps, play):
    if pod_list_:
        cli_podcast_list()
    elif eps:
        cli_print_episodes(eps)
    elif play:
        if None not in play:
            cli_podcast_play(podcast_name=play[0], episode_id=play[1])


# Alias dictionary for commands.
ALIASES = {"rad": radio, "pod": podcast}

if __name__ == "__main__":
    dradio()
