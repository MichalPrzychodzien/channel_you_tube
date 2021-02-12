from unittest import TestCase
from basic_files.video import Video
from basic_files.channel import Channel

class TestChannel(TestCase):
    def test_init(self):
        channel1 = Channel("testowy1", "testowy2")
        self.assertEqual(channel1.videos, [])
        self.assertNotEqual(channel1.videos, [1, 6])
        self.assertEqual(channel1.subscriptions, 0)
        self.assertNotEqual(channel1.subscriptions, -2)

    def test_add_videos(self):
        channel1 = Channel("testowy1", "testowy2")
        video1 = Video("testowy2", 1111, 222)
        channel1.add_videos(video1)

        self.assertEqual(len(channel1.videos), 1)
        self.assertNotEqual(len(channel1.videos), 0)
        self.assertEqual(channel1.videos[0], video1)

    def test_delete_videos(self):
        channel1 = Channel("testowy1", "testowy2")
        video1 = Video("testowy2", 1111, 222)
        channel1.add_videos(video1)
        channel1.delete_videos(video1)

        self.assertEqual(len(channel1.videos), 0)
        self.assertNotEqual(len(channel1.videos), 1)
        self.assertEqual(channel1.videos, [])

    def test_add_subscription(self):
        channel1 = Channel("testowy1", "testowy2")
        channel1.add_subscription()

        self.assertEqual(channel1.subscriptions, 1)
        self.assertNotEqual(channel1.subscriptions, 0)

    def test_delete_subscription(self):
        channel1 = Channel("testowy1", "testowy2")
        channel1.add_subscription()

        self.assertEqual(channel1.subscriptions, 1)
        self.assertNotEqual(channel1.subscriptions, 0)