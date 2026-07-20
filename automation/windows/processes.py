import psutil
from automation.core.result import AutomationResult


class ProcessManager:

    def list_processes(self):
        """
        Returns all running processes.
        """
        processes = []

        try:
            for process in psutil.process_iter(
                ['pid', 'name', 'status']
            ):
                processes.append(process.info)

            return AutomationResult(
                True,
                "Running processes fetched successfully.",
                data=processes
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to fetch processes.",
                error=str(ex)
            )

    def find_process(self, process_name: str):
        """
        Find process by name.
        """
        process_name = process_name.lower()

        try:
            for process in psutil.process_iter(
                ['pid', 'name']
            ):

                name = process.info["name"]

                if name and process_name in name.lower():
                    return AutomationResult(
                        True,
                        "Process found.",
                        data=process.info
                    )

            return AutomationResult(
                False,
                "Process not found."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Search failed.",
                error=str(ex)
            )

    def terminate_process(self, process_name: str):
        """
        Kill process safely.
        """
        process_name = process_name.lower()

        try:
            for process in psutil.process_iter(
                ['pid', 'name']
            ):

                name = process.info["name"]

                if name and process_name in name.lower():
                    process.terminate()

                    return AutomationResult(
                        True,
                        f"{name} terminated successfully."
                    )

            return AutomationResult(
                False,
                "Process not found."
            )

        except Exception as ex:
            return AutomationResult(
                False,
                "Unable to terminate process.",
                error=str(ex)
            )