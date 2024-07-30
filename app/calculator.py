import click

from app.model import Calculator


@click.group()
@click.pass_context
def calc(ctx: click.Context):
    """A simple calculator"""
    ctx.obj = {"calculator_object": Calculator()}


@click.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
@click.pass_context
def add(ctx: click.Context, a: float, b: float) -> None:
    """Add two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.add(a, b)
    click.echo(result)


@click.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
@click.pass_context
def subtract(ctx: click.Context, a: float, b: float) -> None:
    """Add two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.subtract(a, b)
    click.echo(result)



@click.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
@click.pass_context
def multiply(ctx: click.Context, a: float, b: float) -> None:
    """Multiply two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.multiply(a, b)
    click.echo(result)
    

@click.command()
@click.argument('a', type=float)
@click.argument('b', type=float)
@click.pass_context
def divide(ctx: click.Context, a: float, b: float) -> None:
    """Divide two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.divide(a, b)
    click.echo(result)
    

calc.add_command(add)
calc.add_command(subtract)
calc.add_command(multiply)
calc.add_command(divide)
