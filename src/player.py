import vlc


def player(stream_url):
    """
    Takes the stream url and plays the audio in background process while listening for input controls.
    :param stream_url:
    :return:
    """

    instance_vlc = vlc.Instance('--quiet')
    # Suppresses prefetch stream errors to stdout.

    media_player = instance_vlc.media_player_new()
    media_url_vlc_obj = instance_vlc.media_new(stream_url)
    media_player.set_media(media_url_vlc_obj)

    media_player.play()
    print("Radio stream has started ...")

    media_control_input = None
    while not media_control_input == 'q':
        media_control_input = input("Enter q to quit, p to play/pause, m to mute/unmute, +/- to change volume."
                                    "\ndev-radio>").lower()
        volume_step = 10
        # Volume is decreased/increased in steps.

        if media_control_input == 'p':
            media_player.pause()
            print("Play/Pause\n")

        elif media_control_input == 'q':
            print("Aww, man you killed the radio :(")
            media_player.stop()
            break

        elif media_control_input == 'm':
            print("Mute/Unmute\n")
            media_player.audio_toggle_mute()

        elif media_control_input == '+':
            current_volume = media_player.audio_get_volume()
            current_volume += volume_step
            max_volume = 150
            if current_volume <= max_volume:
                media_player.audio_set_volume(current_volume)
                print(f"+vol {current_volume}\n")
            else:
                print("Max volume reached, you will bleed through ears, if you go any further.\n")

        elif media_control_input == '-':
            current_volume = media_player.audio_get_volume()
            current_volume -= volume_step
            min_volume = 0
            if current_volume >= min_volume:
                media_player.audio_set_volume(current_volume)
                print(f"-vol {current_volume}\n")
            else:
                print("Min volume reached\n")

        else:
            print("Incorrect input choice, try again ... :D")
