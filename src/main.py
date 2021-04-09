import click
from src.radio_stations import (
    cli_radio_station_list,
    cli_radio_play, cli_add_station,
    cli_del_station,
    cli_reset_stations,
    cli_radio_check
)

"""Entry point for dev-radio."""


@click.group()
# TODO: add help.
def dradio():
    pass


@dradio.command(help="Plays, lists, checks radio streams.")
@click.option('--list', '-L', 'list_', is_flag=True, help="Lists all the radio stations.")
@click.option('--play', '-P', type=str, help="Pass the radio station name, to start playing radio.")
@click.option('--add-station', '-A', 'add_station', nargs=2, type=str,
              help="Add new radio station by passing radio_name and radio_url, resp")
@click.option('--del-station', '-D', 'del_station', type=str, help="Deletes the radio station of the said name.")
@click.option('--reset', is_flag=True,
              help="Resets all the radio stations to default state, may come in handy if you delete some stations.")
@click.option('--check', '-C', is_flag=True, help="Checks which radio urls are working.")
def radio(list_, play, add_station, del_station, reset, check):
    if list_:
        cli_radio_station_list()
    if play:
        cli_radio_play(play)
    if add_station:
        cli_add_station(add_station[0], add_station[1])
    if del_station:
        cli_del_station(del_station)
    if reset:
        if click.confirm('Do you want to reset all radio stations?', abort=True):
            cli_reset_stations()
    if check:
        cli_radio_check()


# TODO: figure out how to add examples in help
if __name__ == '__main__':
    dradio()