import logging

import click

from .annotate import predict_effects_cmd as predict
from .annotate import gtf_to_bed_cmd as makebed

from .call import call_events_cmd as call
from .call import cluster_filter_cmd as cluster_filter
from .call import event_filter_cmd as event_filter
from .call import run_all_cmd as run_all


@click.group()
@click.option('--loglevel', default='INFO', help='level of logging')
def base(loglevel):
    setup_logging(loglevel)


@click.group()
@click.option('--loglevel', default='INFO', help='level of logging')
def sveffect(loglevel):
    setup_logging(loglevel)


def setup_logging(loglevel="INFO"):
    """
    Set up logging
    :param loglevel: loglevel to use, one of ERROR, WARNING, DEBUG, INFO (default INFO)
    :return:
    """
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level,
                        format='%(levelname)s %(asctime)s %(funcName)s - %(message)s')
    logging.debug("Started log with loglevel %(loglevel)s" % {"loglevel": loglevel})


base.add_command(run_all, name="run-all")
base.add_command(event_filter, name="event-filter")
base.add_command(cluster_filter, name='cluster-filter')
base.add_command(call, name="call-events")

sveffect.add_command(predict, name="predict")
sveffect.add_command(makebed, name="make-bed")