import datetime
import random
import numpy as np
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TreasureMaze:
    def __init__(self, maze):
        self.maze = maze
        self.free_cells = []

    def reset(self, cell):
        pass

    def observe(self):
        return np.zeros((1, 4))

    def valid_actions(self):
        return [0, 1, 2, 3]

    def act(self, action):
        return np.zeros((1, 4)), random.choice([0, 1]), random.choice(['ongoing', 'win', 'lose'])

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
        return np.zeros((data_size, 4)), np.zeros((data_size, 4))

def completion_check(model, qmaze):
    return True

# Helper functions
def choose_action(envstate, valid_actions, model, epsilon):
    if np.random.rand() < epsilon:
        return random.choice(valid_actions)
    q = model.predict(envstate)
    return np.argmax(q[0])

def log_progress(epoch, total_epochs, loss, episodes, win_history, win_rate, elapsed_time):
    template = "Epoch: {:03d}/{:d} | Loss: {:.4f} | Episodes: {:d} | Win count: {:d} | Win rate: {:.3f} | time: {}"
    logging.info(template.format(epoch, total_epochs, loss, episodes, sum(win_history), win_rate, elapsed_time))

def format_time(seconds):
    if seconds < 400:
        return "%.1f seconds" % seconds
    elif seconds < 4000:
        return "%.2f minutes" % (seconds / 60.0)
    else:
        return "%.2f hours" % (seconds / 3600.0)

# Enhanced training function
def qtrain(model, maze):
    epsilon = 1.0
    n_epoch = 15000
    max_memory = 1000
    data_size = 50

    qmaze = TreasureMaze(maze)
    experience = GameExperience(model, max_memory=max_memory)

    start_time = datetime.datetime.now()
    win_history = []
    hsize = qmaze.maze.size // 2 if hasattr(qmaze.maze, 'size') else 50

    for epoch in range(n_epoch):
        n_episodes = 0
        loss = 0.0
        agent_cell = random.choice(qmaze.free_cells) if qmaze.free_cells else (0, 0)
        qmaze.reset(agent_cell)
        envstate = qmaze.observe()
        game_over = False

        while not game_over:
            valid_actions = qmaze.valid_actions()
            if not valid_actions:
                break

            prev_envstate = envstate
            action = choose_action(prev_envstate, valid_actions, model, epsilon)
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

        elapsed = datetime.datetime.now() - start_time
        log_progress(epoch, n_epoch - 1, loss, n_episodes, win_history, win_rate, format_time(elapsed.total_seconds()))

        if win_rate > 0.9:
            epsilon = 0.05
        if sum(win_history[-hsize:]) == hsize and completion_check(model, qmaze):
            logging.info("Reached 100% win rate at epoch: %d", epoch)
            break

    elapsed = datetime.datetime.now() - start_time
    logging.info("Training completed in: %s", format_time(elapsed.total_seconds()))
    return elapsed.total_seconds()
