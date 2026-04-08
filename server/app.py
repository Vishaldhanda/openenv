from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done,
        "info": info
    }

# ✅ REQUIRED FUNCTION
def main():
    return app

# 🔥 THIS WAS MISSING (IMPORTANT)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)