class IntegrationManager:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, connector: str, action: str, **kwargs):
        conn = self.registry.get(connector)
        if conn:
            return conn.execute(action, **kwargs)
        raise Exception(f"Connector {connector} not registered")
