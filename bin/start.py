#!/usr/bin/env python3

from subprocess import Popen, run

from webmonitoring.default import get_homedir


def main():
    # Just fail if the env isn't set.
    get_homedir()
    print('Start backend (redis)...')
    p = run(['run_backend', '--start'])
    p.check_returncode()
    print('done.')
    print('Start queue manager...')
    Popen(['monitoring_queue_manager'])
    print('done.')
    print('Start website...')
    Popen(['start_website'])
    print('done.')


if __name__ == '__main__':
    main()
