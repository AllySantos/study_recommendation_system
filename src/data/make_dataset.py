"""CLI for turning raw data into a processed dataset."""

import logging
from pathlib import Path

import click
from dotenv import find_dotenv, load_dotenv

LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

def main(input_filepath, output_filepath):
    """Run data processing scripts for the project dataset."""
    logger = logging.getLogger(__name__)
    logger.info(
        'making final data set from raw data: %s -> %s',
        input_filepath,
        output_filepath,
    )


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True, path_type=Path))
@click.argument('output_filepath', type=click.Path(path_type=Path))
def cli(input_filepath, output_filepath):
    """Command-line entrypoint for dataset processing."""
    main(input_filepath, output_filepath)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    logging.getLogger(__name__).debug('project directory resolved to %s', project_dir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    cli.main()
