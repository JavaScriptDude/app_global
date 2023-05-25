# -*- coding: utf-8 -*-
"""app_global_sample project

config is a global namespace to be shared across all libraries of your application. 
From local utility code to imported modules that your organization may utilize.

config is simply an empty python file which when imported, will make its namespace shared across all importers

From python.org: 
    The canonical way to share information across modules within a single program is to create a 
    special module (often called config or cfg). Just import the config module in all modules of 
    your application; the module then becomes available as a global name. Because there is only 
    one instance of each module, any changes made to the module object get reflected everywhere.
    see: https://docs.python.org/3/faq/programming.html?highlight=global#how-do-i-share-global-variables-across-modules

In the example below, I have laid out my common application structure which focuses on putting important and useful declarations
near the top and repedetive initialization and boilerplate near the bottom of the file.

namespaces within config (config)
  [opts] - application init or cli options
  [C_] - global constants
  [G_] - global state, caches, etc.
    

To run from commandline see <root>/main.sh

"""
import os
from pretty_python import pretty
from datetime import datetime
from app_global import config
from . import util
import sub_proj

""" startup/cli options (config.opts) """
opts = None
    
""" Global Constants """
class C_():
    # predifine constants to aid in readability
    NAME = "app_global_sample"
    CWD = os.getcwd()
    TS_LOAD = datetime.now()
    EVERYTHING_IS="awesome"


""" Global State / Configs (config.G_) """
class G_():
    # predifine state / configs for readability
    DB_MAIN: None


""" Location of all your main business logic """
def main(args):
    app_init(args) # initialize app and process cli args

    if opts.get('debug'): print(f"[DEBUG] {C_.NAME} started at {C_.TS_LOAD} (PWD={C_.CWD})")

    # Print out app config at load
    print(f"\nApp Config:\n{pretty(config)}")

    sub_proj.do_stuff()

    # Put business logic here ...

    print("main() done")


""" Application init """
def app_init(args):
    # Process cli
    global opts; opts = process_cli_opts(args)

    # Initialize logging
    # ...

    # Initialize app_global
    (config.C, config.G, config.opts) = (C_, G_, opts)

    # Call initialize other libraries
    util.init()
    


""" CLI arg processing - returns opts dict """
def process_cli_opts(args):
    # do stuff
    return dict(debug=True)# dummy stub in place of actual cli parsing

