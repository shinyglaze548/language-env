import os

API_BASE_URL = os.getenv("API_BASE_URL", "dummy")   
MODEL_NAME = os.getenv("MODEL_NAME", "dummy")
HF_TOKEN = os.getenv("HF_TOKEN") 

from environment import LanguageEnv

def agent(obs):
    return obs["answer"]

def grade(total, maxr):
    return total / maxr

def run():
    env = LanguageEnv()
    obs = env.reset()

    print("[START]")

    done = False
    step = 0

    while not done:
        action = agent(obs)
        obs, reward, done, _ = env.step(action)
        print(f"[STEP] step={step} action={action} reward={reward}")
        step += 1

    score = grade(env.total_reward, len(env.tasks))
    print(f"[END] final_score={score}")

if __name__ == "__main__":
    run()
