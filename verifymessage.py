#!/usr/bin/env python3
#
# Copyright (C) 2013-2015 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from bitcoin.signmessage import BitcoinMessage, VerifyMessage


def parser():
    import argparse
    parser = argparse.ArgumentParser(
        description='Verify a message with a signature.',
        epilog='Security warning: arguments may be visible to other users on the same host.')
    parser.add_argument(
        '-a', '--adr',
        required=True,
        help='wallet address')
    parser.add_argument(
        '-m', '--msg',
        required=True,
        help='message')
    parser.add_argument(
        '-s', '--sig',
        required=True,
        help='signature')
    return parser


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        address = input('Address: ')
        message = input('Message: ')
        signature = input('Signature: ')
    else:
        args = parser().parse_args()
        address = args.adr
        message = args.msg
        signature = args.sig
    try:
        verified = VerifyMessage(address, BitcoinMessage(message), signature)
    except Exception as error:
        print('%s: %s' % (error.__class__.__name__, str(error)))
        exit(1)
    else:
        print(verified)
        exit(not verified)
