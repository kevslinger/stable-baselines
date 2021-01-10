from stable_baselines.deepq_poher.policies import MlpPolicy, CnnPolicy, LnMlpPolicy, LnCnnPolicy
from stable_baselines.deepq_poher.build_graph import build_act, build_train  # noqa
from stable_baselines.deepq_poher.dqn import DQNPOHER
from stable_baselines.common.buffers import ReplayBuffer, PrioritizedReplayBuffer  # noqa


def wrap_atari_dqn(env):
    """
    wrap the environment in atari wrappers for DQN

    :param env: (Gym Environment) the environment
    :return: (Gym Environment) the wrapped environment
    """
    from stable_baselines.common.atari_wrappers import wrap_deepmind
    return wrap_deepmind(env, frame_stack=True, scale=False)