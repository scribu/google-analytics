# encoding: utf-8

import logging
import click
import inspector

import googleanalytics as ga


@click.group()
def cli():
    logger = logging.getLogger('googleanalytics')

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
                    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def authenticated(fn):
    @inspector.wraps(fn)
    @click.option('--identity')
    def authenticated_fn(identity=None, *vargs, **kwargs):
        accounts = ga.authenticate(identity=identity, interactive=True, save=True)
        return fn(identity, accounts, *vargs, **kwargs)
    return authenticated_fn
