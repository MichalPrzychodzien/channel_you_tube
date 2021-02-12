from basic_files.video import Video


class Channel:
    def __init__(self, name: str, owner: str) -> None:
        self.owner = owner
        self.name = name
        self.videos = []
        self.subscriptions = 0


    def add_videos(self, video):
        self.videos.append(video)

    def delete_videos(self, video):
        self.videos.remove(video)

    def add_subscription(self):
        self.subscriptions += 1

    def delete_subscription(self):
        if self.subscriptions == 0:
            print("Nie ma subskrypcji")
        else:
            self.subscriptions -= 1

    def show_information(self):
        print(f"Kanał {self.name}, stworzony przez {self.owner} posiada {self.subscriptions} subskrypcje, z kolekcją {len(self.videos)} filmów")

    def show_videos(self):
        for i in self.videos:
            i.show_vid_information()




if __name__ == '__main__':
    kanal = Channel("costam", "Jan")
    jakis_film = Video("programuje", 100, 2021)
    kanal.add_subscription()
    kanal.add_videos(jakis_film)
    kanal.show_information()
    kanal.show_videos()










