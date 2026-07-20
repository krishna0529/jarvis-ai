from pathlib import Path

from automation.core.result import AutomationResult


class StorageStateManager:

    def __init__(self, context):

        self.context = context

        self.storage_dir = Path("outputs/storage")

        self.storage_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, profile="default"):

        try:

            path = self.storage_dir / f"{profile}.json"

            self.context.storage_state(
                path=str(path)
            )

            return AutomationResult(
                True,
                "Storage state saved.",
                data=str(path)
            )

        except Exception as ex:

            return AutomationResult(
                False,
                "Unable to save storage state.",
                error=str(ex)
            )

    def exists(self, profile="default"):

        path = self.storage_dir / f"{profile}.json"

        return path.exists()