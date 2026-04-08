from env.environment import EmailEnv
from env.models import Action

def run_task(task):
    env = EmailEnv(task)
    obs = env.reset()

    results = []

    while True:
        email = obs.current_email

        # simple rule-based agent
        text = (email.subject + " " + email.body).lower()

        if "sale" in text or "offer" in text:
            label = "spam"
        elif "urgent" in text or "asap" in text or "server" in text:
            label = "urgent"
        else:
            label = "normal"

        action = Action(action_type="classify", label=label)

        obs, reward, done, _ = env.step(action)

        results.append({
            "reward": reward.score,
            "reason": reward.reason
        })

        if done:
            break

    return {"results": results}