from decouple import config


WEBSITE_CHECKER_LOGNAME = config(
    'WEBSITE_CHECKER_LOGNAME',
    default='website_checker'
)
WEBSITE_CHECKER_LOGFILE = config(
    'WEBSITE_CHECKER_LOGFILE',
    default='logs/website_checker.log'
)
