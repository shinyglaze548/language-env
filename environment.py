
import random

class LanguageEnv:
    def __init__(self):
        self.tasks = [
            {"type": "vocab", "question": "Translate 'Hola'", "answer": "hello"},
            {"type": "vocab", "question": "Translate 'Gracias'", "answer": "thank you"},
            {"type": "sentence", "question": "Translate 'I am happy'", "answer": "estoy feliz"},
            {"type": "sentence", "question": "Translate 'Good morning'", "answer": "buenos dias"},
            {"type": "conversation", "question": "User says: 'How are you?'", "options": ["i am fine", "blue sky banana", "running table"], "answer": "i am fine"},
            {"type": "conversation", "question": "User says: 'Thank you'", "options": ["you are welcome", "banana runs", "sky blue"], "answer": "you are welcome"}
        ]
        self.index = 0
        self.total_reward = 0

    def reset(self):
        random.shuffle(self.tasks)
        self.index = 0
        self.total_reward = 0
        return self.tasks[self.index]

    def step(self, action):
        task = self.tasks[self.index]
        correct = task["answer"]

        if task["type"] == "sentence":
            aw = set(action.lower().split())
            cw = set(correct.split())
            if action == correct:
                reward = 1.0
            elif len(aw & cw) > 0:
                reward = 0.5
            else:
                reward = 0.0
        else:
            reward = 1.0 if action.lower() == correct else 0.0

        self.total_reward += reward
        self.index += 1
        done = self.index >= len(self.tasks)

        next_obs = self.tasks[self.index] if not done else None
        return next_obs, reward, done, {}

    def state(self):
        return self.tasks[self.index]
