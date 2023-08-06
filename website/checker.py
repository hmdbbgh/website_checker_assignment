import re
import logging
import requests

from logging_config import setup_logging
from .settings import (
    WEBSITE_CHECKER_LOGNAME,
    WEBSITE_CHECKER_LOGFILE
)


logging = setup_logging(
    WEBSITE_CHECKER_LOGNAME,
    WEBSITE_CHECKER_LOGFILE
)


def check_website(
    website_url: str,
    timeout=10,
    pattern=None
) -> dict | None:
    try:
        response = requests.get(website_url, timeout=timeout)
        response_time = response.elapsed.total_seconds()
        status_code = response.status_code
        content = response.text

        pattern_found = None
        if pattern:
            regex = re.compile(pattern)
            pattern_found = bool(regex.search(content))

        return {
            'website_url': website_url,
            'response_time': response_time,
            'status_code': status_code,
            'pattern_found': pattern_found
        }

    except requests.Timeout:
        logging.warning(f"Timeout while checking {website_url}.")
        return None

    except requests.ConnectionError as e:
        logging.error(
            f"Connection error while checking {website_url}: {str(e)}")
        return None

    except requests.RequestException as e:
        logging.error(f"Error checking {website_url}: {str(e)}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error checking {website_url}: {str(e)}")
        return None
