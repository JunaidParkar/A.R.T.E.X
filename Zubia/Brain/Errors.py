from typing import Dict

CHROME_ERROR:Dict[str, str] = {
    'download_failed': "Failed to download Chrome installer.",
    'invalid_status': "Failed to download Chrome installer. Status code: {status}",
    'generic_error': "An error occurred: {error}"
}