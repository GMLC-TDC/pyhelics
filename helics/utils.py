# Copyright (c) 2017-2026,
# Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Energy
# Innovation LLC. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause

import click


def info(msg, blink=False):
    echo(msg, fg="green", level="info", blink=blink)


def warn(msg, blink=True):
    echo(msg, blink=blink)


def error(msg, blink=False):
    echo(msg, fg="red", level="error", blink=blink)


def echo(msg, fg="yellow", level="warn", blink=True):
    click.echo(click.style("[", fg=fg) + click.style(level, fg=fg, blink=blink) + click.style("] ", fg=fg) + click.style(msg, fg=fg))
