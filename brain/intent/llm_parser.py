from brain.intent.schema import IntentSchema

class LLMIntentParser:

    def parse(self, text: str):

        """
        Future:
        Call OpenAI Responses API
        Parse JSON
        Validate output
        """

        return IntentSchema(
            intent="UNKNOWN",
            confidence=0.0,
            entities={}
        )