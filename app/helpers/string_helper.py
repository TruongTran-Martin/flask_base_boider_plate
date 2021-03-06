import random
import string


class StringHelper(object):
    @classmethod
    def random_string(self, string_length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))
