# global variables
# define a board

BOARD_ROWS = 3
BOARD_COLS = 4
WIN_STATE = (0, 3)
LOSE_STATE = (1, 3)
START = (2, 0)
DETERMINISTIC = True


#give rewards according to agent state

def giveReward(self):
  if self.state == WIN_STATE:
    return 1
  elif self.state == LOSE_STATE:
    return -1
  else:
    return 0
  
#When our agent takes an action, the State should have a function
#to accept an action and return a legal position of next state.

def nxtPosition(self, action):
        """
        action: up, down, left, right
        -------------
        0 | 1 | 2| 3|
        1 |
        2 |
        return next position
        """
    if self.determine:
      if action == "up":
        nxtState = (self.state[0] - 1, self.state[1])
      elif action == "down":
        nxtState = (self.state[0] + 1, self.state[1])
      elif action == "left":
        nxtState = (self.state[0], self.state[1] - 1)
      else:
        nxtState = (self.state[0], self.state[1] + 1)
      # if next state legal
      if (nxtState[0] >= 0) and (nxtState[0] <= 2):
        if (nxtState[1] >= 0) and (nxtState[1] <= 3):
          if nxtState != (1, 1):
            return nxtState
      return self.state
    
    
#value iteration
def play(self, rounds=10):
        i = 0
        while i < rounds:
            # to the end of game back propagate reward
            if self.State.isEnd:
                # back propagate
                reward = self.State.giveReward()
                # explicitly assign end state to reward values
                self.state_values[self.State.state] = reward  # this is optional
                print("Game End Reward", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.chooseAction()
                # append trace
                self.states.append(self.State.nxtPosition(action))
                print("current position {} action {}".format(self.State.state, action))
                # by taking the action, it reaches the next state
                self.State = self.takeAction(action)
                # mark is end
                self.State.isEndFunc()
                print("nxt state", self.State.state)
                print("---------------------")
