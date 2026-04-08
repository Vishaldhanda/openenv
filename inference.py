from env.environment import EmailEnv
from env.models import Action

def simple_agent(email):
    text = (email.subject + " " + email.body).lower()

    if any(x in text for x in ["sale", "offer", "buy", "discount"]):
        return "spam"
    elif any(x in text for x in ["urgent", "asap", "meeting", "server", "fix"]):
        return "urgent"
    else:
        return "normal"

def run_task(task):
    env = EmailEnv(task)
    obs = env.reset()

    total_reward = 0
    step = 0

    # ✅ START BLOCK
    print(f"[START] task={task}", flush=True)

    while True:
        email = obs.current_email
        label = simple_agent(email)

        action = Action(action_type="classify", label=label)

        obs, reward, done, _ = env.step(action)

        total_reward += reward.score
        step += 1

        # ✅ STEP BLOCK
        print(f"[STEP] step={step} reward={reward.score}", flush=True)

        if done:
            break

    # ✅ END BLOCK
    print(f"[END] task={task} total_reward={total_reward} steps={step}", flush=True)


if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        run_task(t)