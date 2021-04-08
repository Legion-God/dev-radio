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

    # FIXME: OLDER version, may delete this later
    # media_player = vlc.MediaPlayer(stream_url)
    media_player.play()
    print("Radio stream has started ...")

    media_control_input = None
    while not media_control_input == 'q':
        media_control_input = input("Enter q to quit, p to play/pause, m to mute/unmute\ndev-radio>").lower()
        # TODO: if possible add +/- to increase/decrease volume in steps of 10.
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

        else:
            print("Incorrect input choice, try again ... :D")
