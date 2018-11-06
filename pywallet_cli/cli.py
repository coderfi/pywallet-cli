#!/usr/bin/env python

from pywallet import wallet
from pywallet import network as networks
import click
import json
import sys


_x = [
    'bitcoin', 'btc',
    'ethereum', 'eth',
    'bitcoin_testnet', 'btctest',
    'dogecoin', 'doge',
    'dogecoin_testnet', 'dogetest',
    'litecoin', 'ltc',
    'litecoin_testnet', 'ltctest',
    'bitcoin_cash', 'bitcoin_cash',
    'bitcoin_gold', 'btg',
    'dash',
    'dash_testnet', 'dashtest',
    'omni',
    'omni_testnet',
    'feathercoin', 'ftc',
    'qtum',
    'qtum_testnet', 'qtumtest'
]
NETWORKS = sorted(set([x.upper() for x in _x] + _x))
del _x

@click.command()
@click.option('-c', '--children', type=int, default=3)
@click.option('-n', '--net', '--network', default='BTC', type=click.Choice(NETWORKS))
@click.option('-r', '--random/--no-random', '--random-seed/--no-random-seed', is_flag=True, default=False, help='generate random seed')
@click.option('--pretty/--no-pretty', is_flag=True, default=True)
@click.argument('seed', nargs=-1)
def main(seed, network, children, pretty, random_seed=False):
    '''Where args is the seed to use.
    If none specified, reads from STDIN.

    pywallet-cli traffic happy world clog clump cattle great toy game absurd alarm auction

    cat myseeds.txt | pywallet-cli

    pywallet-cli --network=ETH --children=3 --no-pretty --random-seed
    '''
    # generate 12 word mnemonic seed
    if seed:
        seed = " ".join(seed)
    else:
        if random_seed:
            seed = wallet.generate_mnemonic()
        else:
            arr = []
            for words in sys.stdin:
                arr.extend(words.split())
                if len(arr) >= 12:
                    break
            seed = " ".join(arr)

    # create bitcoin wallet
    w = wallet.create_wallet(network=network, seed=seed, children=children)
    b2asc(w)

    indent = 4 if pretty else None
    print(json.dumps(w, sort_keys=True, indent=indent))


def b2asc(d):
    for k in d.keys():
        v = d[k]

        if isinstance(v, dict):
            for k2 in v.keys():
                b2asc(v)
        elif isinstance(v, tuple):
            d[k] = tuple(b2asci(v2) for v2 in v)
        elif isinstance(v, list):
            for i in range(len(v)):
                v[i] = b2asc(v[i])
        elif isinstance(v, bytes):
           d[k] = v.decode('ascii')

    return d


if __name__ == '__main__':
    main()
