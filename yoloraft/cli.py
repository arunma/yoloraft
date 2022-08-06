# import logging
# import os
#
# import click
# from click_repl import register_repl
#
# from yoloraft.config import ConfigLoader
#
# """
#     The main function executes on commands:
#     `python -m yoloraft` and `$ yoloraft `.
# """
#
#
# @click.group()
# @click.option(
#     "--config",
#     envvar="CONFIG_HOME",
#     metavar="CONFIG_PATH",
#     help="Absolute path to the config file.",
# )
# @click.version_option("1.0")
# def cli(path):  # pragma: no cover
#     config = ConfigLoader.load(os.path.abspath(path))
#     logging.debug(f"Config: {config}")
#     id, peers, data_dir, listen_raft = (
#         config.id,
#         config.peers,
#         config.data_dir,
#         config.listen_raft,
#     )
#     Server(id, peers, data_dir).serve(listen_raft)
#
#
# def main():
#     register_repl(cli)
#     cli()
