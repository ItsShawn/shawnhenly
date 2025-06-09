import datetime
import random
import numpy as np

# Placeholder classes assumed from project context
# You must include their real implementations if you're submitting the full artifact
class TreasureMaze:
    def __init__(self, maze):
        self.maze = maze
        self.free_cells = []  # Fill this with appropriate logic

    def reset(self, cell):
        pass

    def observe(self):
        pass

    def valid_actions(self):
        return []

    def act(self, action):
        return None, 0, 'ongoing'

class GameExperience:
    def __init__(self, model, max_memory=1000):
        self.model = model
        self.memory = []
        self.max_memory = max_memory

    def remember(self, episode):
        if len(self.memory) >= self.max_memory:
            self.memory.pop(0)
        self.memory.append(episode)

    def get_data(self, data_size=50):
        # Return dummy inputs and targets as placeholders
        return np.zeros((data_size, 4)), np.zeros((data_size, 4))

def completion_check(model, qmaze):
    # Dummy placeholder
    return True

# Global epsilon (exploration rate)
epsilon = 1.0

def qtrain(model, maze, **opt):
    global epsilon

    n_epoch = opt.get('n_epoch', 15000)
    max_memory = opt.get('max_memory', 1000)
    data_size = opt.get('data_size', 50)
    start_time = datetime.datetime.now()

    qmaze = TreasureMaze(maze)
    experience = GameExperience(model, max_memory=max_memory)

    win_history = []
    hsize = qmaze.maze.size // 2 if hasattr(qmaze.maze, 'size') else 50
    win_rate = 0.0

    for epoch in range(n_epoch):
        n_episodes = 0
        loss = 0.0
        agent_cell = random.choice(qmaze.free_cells)
        qmaze.reset(agent_cell)
        envstate = qmaze.observe()
        game_over = False

        while not game_over:
            valid_actions = qmaze.valid_actions()
            if not valid_actions:
                break

            prev_envstate = envstate

            if np.random.rand() < epsilon:
                action = random.choice(valid_actions)
            else:
                q = model.predict(prev_envstate)
                action = np.argmax(q[0])

            envstate, reward, game_status = qmaze.act(action)
            game_over = (game_status != 'ongoing')

            episode = [prev_envstate, action, reward, envstate, game_status]
            experience.remember(episode)

            inputs, targets = experience.get_data(data_size=data_size)
            h = model.fit(inputs, targets, epochs=1, batch_size=16, verbose=0)
            loss = h.history['loss'][0]

        n_episodes += 1
        win_history.append(1 if game_status == 'win' else 0)
        win_rate = sum(win_history[-hsize:]) / hsize

        dt = datetime.datetime.now() - start_time
        t = format_time(dt.total_seconds())
        template = "Epoch: {:03d}/{:d} | Loss: {:.4f} | Episodes: {:d} | Win count: {:d} | Win rate: {:.3f} | time: {}"
        print(template.format(epoch, n_epoch - 1, loss, n_episodes, sum(win_history), win_rate, t))

        if win_rate > 0.9:
            epsilon = 0.05
        if sum(win_history[-hsize:]) == hsize and completion_check(model, qmaze):
            print("Reached 100% win rate at epoch: %d" % (epoch,))
            break

    dt = datetime.datetime.now() - start_time
    seconds = dt.total_seconds()
    t = format_time(seconds)

    print("n_epoch: %d, max_mem: %d, data: %d, time: %s" % (epoch, max_memory, data_size, t))
    return seconds

def format_time(seconds):
    if seconds < 400:
        return "%.1f seconds" % seconds
    elif seconds < 4000:
        return "%.2f minutes" % (seconds / 60.0)
    else:
        return "%.2f hours" % (seconds / 3600.0)
