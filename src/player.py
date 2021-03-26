from playsound import playsound
import multiprocessing


def player(stream_url):
    """
    Takes the stream url and plays the audio in background process while listening for input,
    to cancel the stream.
    :param stream_url:
    :return:
    """
    player_process = multiprocessing.Process(target=playsound, args=(stream_url,))
    player_process.start()

    print("Plz wait for a few seconds, streaming is now starting ...")
    input("Press ENTER key to terminate the stream ...")
    player_process.terminate()

    print("Stream has been terminated ...")
