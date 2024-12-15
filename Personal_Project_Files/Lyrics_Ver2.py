def Lyrics_v2():
    import time
    from threading import Thread
    import sys

    lyrics = [
        ("\n'Just trust me, you'll be fine'",0.9),
        ("And when I'm back in Chicago, I feel it",0.9),
        ("Another version of me, I was in it",0.9),
        ("I wave goodbye to the end of beginning",0.8),
        ("(Goodbye, goodbye, goodbye, goodbye)",0.1),
    ]
    delays = [0, 5.0, 11.0, 17.0, 20.8]

    def animate_text(text, delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def sing_lyrics(lyric, delay, speed):
        time.sleep(delay)
        animate_text(lyric, speed)

    def sing_song():
        threads = []
        for i in range(len(lyrics)):
            lyric, speed = lyrics[i]
            t = Thread(target=sing_lyrics,args=(lyric, delays[i], speed))
            threads.append(t)
            t.start
        for thread in threads:
            thread.join()

    if __name__ == "__main__":
        sing_song

    """Another Fun Project With A Friend, It Does Not Run Still On Progress"""

Lyrics_v2()