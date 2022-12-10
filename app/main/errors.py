from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return "<h1>Not Found</h1>", 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return "<h1>Something went wrong! Sorry about that.</h1>", 500