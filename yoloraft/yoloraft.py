# import logging
# import os
# import sys
#
# import click
# import yaml
# from click_repl import register_repl
# from learn_raft.server import Server
#
#
# class Config:
#     def __init__(self, path):
#         self.path = path
#         with open(path, "r") as file:
#             config = yaml.safe_load(file)
#             self.id = config["id"]
#             self.data_dir = config["data_dir"]
#             self.listen_raft = config["listen_raft"]
#             self.peers = config["peers"]
#
#     def __repr__(self):
#         return f"<Config> {str(self.__dict__)}"
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
#     config = Config(os.path.abspath(path))
#     logging.debug(f"Config: {config}")
#     id, peers, data_dir, listen_raft = (
#         config.id,
#         config.peers,
#         config.data_dir,
#         config.listen_raft,
#     )
#     server = Server(id, peers, data_dir).serve(listen_raft)
#
#
# register_repl(cli)
# cli()
