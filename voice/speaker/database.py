class SpeakerDatabase:

    def __init__(self):

        self.users = {}

    def add(self, profile):

        self.users[profile.user_id] = profile

    def get(self, user_id):

        return self.users.get(user_id)