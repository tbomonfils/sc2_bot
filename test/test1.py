from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features
from absl import app
import tensorflow as tf
import baselines
import pysc2

import sys
from absl import flags
FLAGS = flags.FLAGS
tf.app.flags.DEFINE_string('f', '', 'kernel')
FLAGS(sys.argv)

import os
os.environ["SC2PATH"] = "/home/nsml/StarCraftII"

players = [sc2_env.Agent(sc2_env.Race.zerg)]
map_name = "CollectMineralShards"

class ZergAgent(base_agent.BaseAgent):
  def step(self, obs):
    super(ZergAgent, self).step(obs)
    
    return actions.FUNCTIONS.no_op()
	
def main(unused_argv):
  agent = ZergAgent()
  try:
    while True:
      with sc2_env.SC2Env(
          map_name=map_name,
          players=players,
          agent_interface_format=features.AgentInterfaceFormat(
              feature_dimensions=features.Dimensions(screen=84, minimap=64)),
          step_mul=16,
           game_steps_per_episode=0,
          visualize=True) as env:
        
        print('hello')
        
  except KeyboardInterrupt:
    pass
	
if __name__ == '__main__':
	main('')