# -*- coding: utf-8 -*-
import click


def info(msg, blink=False):
    echo(msg, fg="green", level="info", blink=blink)


def warn(msg, blink=True):
    echo(msg, blink=blink)


def error(msg, blink=False):
    echo(msg, fg="red", level="error", blink=blink)


def echo(msg, fg="yellow", level="warn", blink=True):
    click.echo(click.style("[", fg=fg) + click.style(level, fg=fg, blink=blink) + click.style("] ", fg=fg) + click.style(msg, fg=fg))
