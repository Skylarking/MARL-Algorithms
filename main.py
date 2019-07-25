from runner import Runner
from smac.env import StarCraft2Env
from common.arguments import get_args


if __name__ == '__main__':
    args = get_args()
    env = StarCraft2Env(map_name=args.map,
                        step_mul=args.step_mul,
                        difficulty=args.difficulty,
                        game_version=args.game_version,
                        seed=args.seed,
                        replay_dir=args.replay_dir)
    env_info = env.get_env_info()
    args.n_actions = env_info["n_actions"]
    args.n_agents = env_info["n_agents"]
    args.state_shape = env_info["state_shape"]
    args.obs_shape = env_info["obs_shape"]
    args.episode_limit = env_info["episode_limit"]
    runner = Runner(env, args)
    runner.run()
    args.alg = 'vdn'
    args.result_dir = './model/vdn/7-18'
    runner = Runner(env, args)
    runner.run()

    env.close()