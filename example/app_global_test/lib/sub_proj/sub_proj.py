from app_global import config

def do_stuff():
    if config.opts.get('debug'): print(f"sub_proj.do_stuff() called from {config.C.NAME} app")
    config.G.SUB_PROJ_STUFF="TBD"