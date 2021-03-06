import numpy as np
import matplotlib.pyplot as plt
import gym
from gym.envs.registration import register
import random as pr

def rargmax(vector):

    """ Argmax that chooses randomly among eligible maximum indices. """
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)

if __name__ == "__main__":
    # Register FrozenLake with is_slippery False
    register(
        id='FrozenLake-v3',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name': '4x4', 'is_slippery': True}
    )

    env = gym.make('FrozenLake-v3')
    env.render()

    # Initialize table with all zeros
    Q = np.zeros([env.observation_space.n, env.action_space.n])  # Q(s,a) 16 states, 4 actions
    # Set learning parameters
    # Discount factor
    dis = .99
    num_episodes = 2000
    # do not take Q^'s opinion seriously
    learning_rate = 0.85
    # create lists to contain total reward and steps per episode
    rList = []
    for i in range(num_episodes):
        # Reset enviroment and get first new observation
        state = env.reset()
        rAll = 0
        done = False

        # The Q-Table leaerning algorithm
        while not done:
            # Choose an action by greedily (with noise) picking from Q table
            action = np.argmax((Q[state, :] + np.random.randn(1, env.action_space.n) / (i + 1)))

            # Get new state and reward from environment
            new_state, reward, done, _ = env.step(action)

            # Update Q-Table with new knowledge using decay rate
            Q[state, action] = (1-learning_rate)*Q[state, action] + learning_rate*(reward + dis * np.max(Q[new_state, :]))

            rAll += reward
            state = new_state

        rList.append(rAll)

    print("Success rate: " + str(sum(rList)/num_episodes))
    print("Final Q-Table Values")
    print("LEFT DOWN RIGHT UP")
    print(Q)
    plt.bar(range(len(rList)), rList, color="blue")
    plt.show()