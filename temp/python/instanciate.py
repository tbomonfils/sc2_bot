import sys

sys.path.append("/home/AI_core/app/temp/python")

from absl import app

import config

def main(_):
    config.define_conf()
    print("app configuration success !!")

if __name__ == "__main__":
    app.run(main)