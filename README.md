# GridWorld-Reinforcment-Learning-Problem

The most basic as well as classic problem in reinforcement learning

## Rules
--------------------------------------

The rule is simple. Your agent/robot starts at the left-bottom corner(the ‘start’ sign)
and ends at either +1 or -1 which is the corresponding reward.
At each step, the agent has 4 possible actions including up, down, left and right,
whereas the black block is a wall where your agent won’t be able to penetrate through.
In order to make it more straight forward, our first implementation assumes that each action is deterministic,
that is, the agent will go where it intends to go. For instance, when the agent decides to take
action up at (2, 0), it will land in (1, 0) rather than (2, 1) or elsewhere. (We will add uncertainty
in out second implementation) However, it the agents hit the wall, it will remain at the same position.

![Grid](/img/rl.png)
