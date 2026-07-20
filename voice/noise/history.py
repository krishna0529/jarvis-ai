class NoiseHistory:

    def __init__(self):

        self.records = []

    def add(self, profile):

        self.records.append(profile)

    def latest(self):

        if self.records:

            return self.records[-1]

        return None