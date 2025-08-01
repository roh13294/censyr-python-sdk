class Model:
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version

class Inference:
    def __init__(self, input_data: dict, output_data: dict):
        self.input_data = input_data
        self.output_data = output_data

class Violation:
    def __init__(self, rule: str, details: str):
        self.rule = rule
        self.details = details

class AuditLog:
    def __init__(self, event: str, metadata: dict):
        self.event = event
        self.metadata = metadata

class CustomRule:
    def __init__(self, name: str, condition: str):
        self.name = name
        self.condition = condition
