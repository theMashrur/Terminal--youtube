"""A video playlist class."""

from .video_library import VideoLibrary


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, playlist_name):
        self.name = playlist_name
        self.videos = []
        self._video_library = VideoLibrary()
    
    def add_video(self, video_id):
        self.videos.append(video_id)


    def remove_video(self, video_id):
        self.videos.remove(video_id)
    
    def clear(self):
        self.videos.clear()

    def show(self):
        lis = []
        list_videos = self._video_library.get_all_videos()
        if self.videos:
            for item in list_videos:
                if len(item.tags):
                    tag1 = item.tags[0]
                    tag2 = item.tags[1]
                    lis.append("{0} ({1}) [{2} {3}]".format(item.title, item.video_id, tag1, tag2))
                else:
                    lis.append("{0} ({1}) []".format(item.title, item.video_id))
            return lis
        else:
            return "No videos here yet"    



    @property
    def videos(self):
        return self.videos
