from app_global import config

# see init() for intialization
C_ = None # global constants
G_ = None # global state, caches, etc.
opts = None # startup/cli options (config.opts)

def init():
    global C_, G_, opts
    (C_, G_, opts) = (config.C, config.G, config.opts)

    if opts.get('debug'): print(f"[DEBUG] prj1.util.init() called from {C_.NAME}")

    G_.SOME_PRJ1_UTIL_STATE = dict(state="prj1.util")

    G_.DB_MAIN="tbc" # prepare db authentication etc...
    

"""
  More functionality added here
  ...
"""
    