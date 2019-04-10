import os


def get_disk_stats():
    stats = os.statvfs('/')
    block_size = stats[0]
    total_blocks = stats[2]
    free_blocks = stats[3]
    stats = dict()
    stats['free'] = block_size * free_blocks
    stats['total'] = block_size * total_blocks
    stats['used'] = stats['total'] - stats['free']
    return stats


def format_size(val):
    val = int(val / 1024)               # convert bytes to KiB
    val = '{:,}'.format(val)            # add thousand separator
    val = '{0: >6} KiB'.format(val)     # right align amounts
    return val


def print_stats():
    stats = get_disk_stats()
    print('free space: ', format_size(stats['free']))
    print('used space: ', format_size(stats['used']))
    print('total space:', format_size(stats['total']))


print_stats()
