from web import BASE_TEMPLATE, run_server
import random


def handler(request, method, path):
    body = 'random: %s' % random.random()
    return BASE_TEMPLATE % body


def main():
    run_server(handler)


main()
