from absl import flags
from pysc2.lib import point_flag
from pysc2.env import sc2_env

# because of Abseil's horrible design for running code underneath Colabs
# We have to pull out this ugly hack from the hat

def define_conf():

    FLAGS = flags.FLAGS

    if "flags_defined" not in globals():
        flags.DEFINE_bool("render", True, "Whether to render with pygame.")
        point_flag.DEFINE_point("feature_screen_size", "84",
                                "Resolution for screen feature layers.")
        point_flag.DEFINE_point("feature_minimap_size", "64",
                                "Resolution for minimap feature layers.")
        point_flag.DEFINE_point("rgb_screen_size", None,
                                "Resolution for rendered screen.")
        point_flag.DEFINE_point("rgb_minimap_size", None,
                                "Resolution for rendered minimap.")
        flags.DEFINE_enum("action_space", None, sc2_env.ActionSpace._member_names_,  # pylint: disable=protected-access
                        "Which action space to use. Needed if you take both feature "
                        "and rgb observations.")
        flags.DEFINE_bool("use_feature_units", False,
                        "Whether to include feature units.")
        flags.DEFINE_bool("disable_fog", False, "Whether to disable Fog of War.")

        flags.DEFINE_integer("max_agent_steps", 0, "Total agent steps.")
        flags.DEFINE_integer("game_steps_per_episode", None, "Game steps per episode.")
        flags.DEFINE_integer("max_episodes", 0, "Total episodes.")
        flags.DEFINE_integer("step_mul", 8, "Game steps per agent step.")

        flags.DEFINE_string("agent", "pysc2.agents.random_agent.RandomAgent",
                            "Which agent to run, as a python path to an Agent class.")
        flags.DEFINE_enum("agent_race", "random", sc2_env.Race._member_names_,  # pylint: disable=protected-access
                        "Agent 1's race.")

        flags.DEFINE_string("agent2", "Bot", "Second agent, either Bot or agent class.")
        flags.DEFINE_enum("agent2_race", "random", sc2_env.Race._member_names_,  # pylint: disable=protected-access
                        "Agent 2's race.")
        flags.DEFINE_enum("difficulty", "very_easy", sc2_env.Difficulty._member_names_,  # pylint: disable=protected-access
                        "If agent2 is a built-in Bot, it's strength.")

        flags.DEFINE_bool("profile", False, "Whether to turn on code profiling.")
        flags.DEFINE_bool("trace", False, "Whether to trace the code execution.")
        flags.DEFINE_integer("parallel", 1, "How many instances to run in parallel.")

        flags.DEFINE_bool("save_replay", True, "Whether to save a replay at the end.")

        flags.DEFINE_string("map", None, "Name of a map to use.")
        flags.mark_flag_as_required("map")

    flags_defined = True