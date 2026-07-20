class AdaptiveNoiseEngine:

    def apply(self, profile):

        print(f"Environment : {profile.environment}")

        print(f"Noise Level : {profile.level:.4f}")

        print(f"Reduction : {profile.reduction_strength}")

        print(f"Whisper Model : {profile.whisper_model}")