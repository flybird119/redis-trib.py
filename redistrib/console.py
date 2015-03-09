import sys
import logging

import command


def _parse_host_port(addr):
    host, port = addr.split(':')
    return host, int(port)


def start(host_port):
    command.start_cluster(*_parse_host_port(host_port))


def join(cluster_host_port, newin_host_port):
    cluster_host, cluster_port = _parse_host_port(cluster_host_port)
    newin_host, newin_port = _parse_host_port(newin_host_port)
    command.join_cluster(cluster_host, cluster_port, newin_host, newin_port)


def join_no_load(cluster_host_port, newin_host_port):
    cluster_host, cluster_port = _parse_host_port(cluster_host_port)
    newin_host, newin_port = _parse_host_port(newin_host_port)
    command.join_no_load(cluster_host, cluster_port, newin_host, newin_port)


def quit(host_port):
    command.quit_cluster(*_parse_host_port(host_port))


def shutdown(host_port):
    command.shutdown_cluster(*_parse_host_port(host_port))


def fix(host_port):
    command.fix_migrating(*_parse_host_port(host_port))


def replicate(master_host_port, slave_host_port):
    master_host, master_port = _parse_host_port(master_host_port)
    slave_host, slave_port = _parse_host_port(slave_host_port)
    command.replicate(master_host, master_port, slave_host, slave_port)


def migrate_slot(src_host_port, dst_host_port, slot):
    src_host, src_port = _parse_host_port(src_host_port)
    dst_host, dst_port = _parse_host_port(dst_host_port)
    command.migrate_slot(src_host, src_port, dst_host, dst_port, slot)


def main():
    if len(sys.argv) < 2:
        print >> sys.stderr, 'Usage:'
        print >> sys.stderr, '    redis-trib.py ACTION_NAME [arg0 arg1 ...]'
        sys.exit(1)
    logging.basicConfig(level=logging.INFO)
    getattr(sys.modules[__name__], sys.argv[1])(*sys.argv[2:])
