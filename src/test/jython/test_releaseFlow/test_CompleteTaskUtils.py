import unittest
from releaseFlow.CompleteTaskUtils import capitalize


class TestCompleteTask(unittest.TestCase):
    def test_capitalize_name(self):
        self.assertEqual('Foo', capitalize('foo'))
