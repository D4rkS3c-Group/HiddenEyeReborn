from argparse import ArgumentParser


arg_parser = ArgumentParser(  # TODO fill with some actual info
    prog='HiddenEye Reborn',
    description='HiddenEye with completely new codebase and better features set!',
    epilog='To be filled')

arg_parser.add_argument('-ni', '--non-interactive', help='Runs HiddenEye in non-interactive mode (options-only)', dest='non_interactive', action='store_true')

args = arg_parser.parse_args()

