import vlc
import requests
import click


def player(stream_url):
    """
    Takes the stream url and plays the audio in background process while listening for input controls.
    :param stream_url:
    :return:
    """
    valid_media_extensions = [
        "audio/mpeg",
        "audio/aac",
        "application/ogg",
        "audio/x-m4a",
        "audio/3gpp",
        "audio/3gpp2",
        "audio/opus",
        "audio/vorbis",
    ]
    resp_content_type = requests.get(stream_url, stream=True, timeout=50).headers.get(
        "Content-Type"
    )

    if resp_content_type in valid_media_extensions:
        instance_vlc = vlc.Instance("--quiet")
        # Suppresses prefetch stream errors to stdout.

        media_player = instance_vlc.media_player_new()
        media_url_vlc_obj = instance_vlc.media_new(stream_url)
        media_player.set_media(media_url_vlc_obj)

        media_player.play()
        print("Radio stream has started ... ((d[-_-]b))\n")
        print("NOTE: If you can't hear anything, try increasing volume ...\n")

        media_control_input = None
        while not media_control_input == "q":
            click.echo(
                "Enter q to quit, p to play/pause, m to mute/unmute, +/- to change "
                "volume. \ndev-radio>",
                nl=False,
            )
            media_control_input = click.getchar().lower()
            click.echo()
            volume_step = 10
            # Volume is decreased/increased in steps.

            if media_control_input == "p":
                media_player.pause()
                print("Play/Pause (^_^)\n")

            elif media_control_input == "q":
                print("Aww, man you killed the radio. (T_T)\n")
                media_player.stop()
                break

            elif media_control_input == "m":
                print("Mute/Unmute (~_~)\n")
                media_player.audio_toggle_mute()

            elif media_control_input == "+":
                current_volume = media_player.audio_get_volume()
                current_volume += volume_step
                max_volume = 151
                if current_volume <= max_volume:
                    media_player.audio_set_volume(current_volume)
                    print(f"+vol {current_volume}\n")
                else:
                    print(
                        "Max volume reached, you will bleed through ears, if you go any further. (o_O)\n"
                    )

            elif media_control_input == "-":
                current_volume = media_player.audio_get_volume()
                current_volume -= volume_step
                min_volume = 0
                if current_volume >= min_volume:
                    media_player.audio_set_volume(current_volume)
                    print(f"-vol {current_volume}\n")
                else:
                    print("Min volume reached (-_-)zzz\n")

            else:
                print("Incorrect input choice, try again ... (?_?)\n")

    else:
        print("Invalid url:: url maybe dead ...")
