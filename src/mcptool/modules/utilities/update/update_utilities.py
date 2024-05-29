import requests

from loguru import logger

from ..notificactions.send import SendNotification
from ..constants import VERSION, GITHUB_REPOSITORY, MCPTOOL_WEBSITE


class UpdateUtilities:
    @staticmethod
    @logger.catch
    def update_available():
        """
        Method to check if an update is available

        Returns:
            bool: True if an update is available, False otherwise
        """

        try:
            response: requests.Response = requests.get(f'{GITHUB_REPOSITORY}settings.json')

            if response.status_code != 200:
                return False

            settings = response.json()

            if settings['version'] != VERSION:
                SendNotification(
                    title='MCPTool Update Available',
                    message=f'An update is available for MCPTool. Current version: {VERSION}, new version: {settings["version"]} Download it from {MCPTOOL_WEBSITE}'
                ).send()

            return settings['version'] != VERSION

        except Exception as e:
            logger.warning(f'Error checking for updates: {e}')
            return False
