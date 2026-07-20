from brain.intent.schema import IntentSchema

class IntentValidator:

    def validate(self, data):

        return IntentSchema(**data)