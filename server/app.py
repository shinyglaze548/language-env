from fastapi import FastAPI
from pydantic import BaseModel
from environment import LanguageEnv

app = FastAPI()
env = LanguageEnv()

class Action(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "Env running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action.action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

# 👇 ADD THIS PART (IMPORTANT)
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
