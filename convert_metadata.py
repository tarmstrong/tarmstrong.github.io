#!/usr/bin/env python3
import argparse
import logging
import pathlib
import re

from dateutil import parser as dateparser

logger = logging.getLogger(__name__)

METADATA_PATTERN = re.compile(r'(?P<key>\w+):\s(?P<value>.*$)')

def convert_date_to_iso8601(date_string):
    dt = dateparser.parse(date_string)
    return '"{}"'.format(dt.isoformat())

def handle_list_string(list_string):
    quoted_list = list()
    for item in list_string.split(','):
        item = item.strip()
        quoted_list.append('"{}"'.format(item))
    quoted_list_string = ', '.join(quoted_list)
    return '[ {} ]'.format(quoted_list_string)

def handle_title(title):
    if title.startswith('"') and title.endswith('"'):
        return title
    else:
        return '"{}"'.format(title)


TRANSFORMATIONS = {
    'title': handle_title,
    'tags': handle_list_string,
    # 'author': lambda x: x,
    'date': convert_date_to_iso8601
}


def convert_file(source_path, output_dir):
    with source_path.open(mode='rt') as f:
        with output_dir.joinpath(source_path.name).open(mode='wt') as outfile:
            outfile.write("+++\n")
            for line in f:
                if line == "\n":
                    # end of metadata
                    outfile.write("+++\n\n")
                    break
                else:
                    match = METADATA_PATTERN.match(line)
                    if match is None:
                        logger.warning("EEEK! no match: %s", line)
                    else:
                        key, value = match.group('key').lower(), match.group('value')
                        if not key in TRANSFORMATIONS:
                            logger.warning("unknown key: '%s' in '%s'", key, source_path.name)
                        else:
                            transformation = TRANSFORMATIONS[key]
                            value = transformation(value)
                            outfile.write("{} = {}\n".format(key, value))
            for line in f:
                outfile.write(line)


def main(input_dir, output_dir):
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)
    for item in input_dir.glob('*.md'):
        convert_file(item, output_dir)


if __name__ == "__main__":
    logging.basicConfig()
    parser = argparse.ArgumentParser(
        description='Convert Pelican metadata into Hugo frontmatter.')
    parser.add_argument('input_dir')
    parser.add_argument('output_dir')
    args = parser.parse_args()
    main(args.input_dir, args.output_dir)
