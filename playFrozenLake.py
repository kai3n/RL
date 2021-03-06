import gym
from gym.envs.registration import register
import readchar

if __name__ == "__main__":

    LEFT, DOWN, RIGHT, UP = range(4)
    arrow_keys = {
        '\x1b[A': UP,
        '\x1b[B': DOWN,
        '\x1b[C': RIGHT,
        '\x1b[D': LEFT,
    }

    # Register FrozenLake with is_slippery False
    register(
        id='FrozenLake-v3',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name': '4x4', 'is_slippery': False}
    )

    env = gym.make('FrozenLake-v3')
    env.render()

    while True:
        # Choose an action from keyboard
        key = readchar.readchar()
        if key not in arrow_keys.keys():
            print('Game aborted!')
            break

        action = arrow_keys[key]
        state, reward, done, info = env.step(action)
        env.render()  # Show the board after action
        print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

        if done:
            print("Finished with reward", reward)
            break
