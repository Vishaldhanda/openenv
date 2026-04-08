from env.environment import EmailEnv
from env.models import Action
from env.grader import grade

def simple_agent(email):
    text = (email.subject + " " + email.body).lower()

    if any(x in text for x in ["sale", "offer", "buy", "discount"]):
        return "spam"
    elif any(x in text for x in ["urgent", "asap", "meeting", "server", "fix"]):
        return "urgent"
    else:
        return "normal"

def run(task):
    env = EmailEnv(task)
    obs = env.reset()

    correct = 0
    total = 0
    total_reward = 0

    while True:
        email = obs.current_email
        label = simple_agent(email)

        action = Action(action_type="classify", label=label)

        obs, reward, done, _ = env.step(action)
        total_reward += reward.score

        if reward.score > 0:
            correct += 1

        total += 1

        if done:
            break

    return grade(correct, total), total_reward

if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        acc, rew = run(t)
        print(f"{t} -> accuracy: {acc}, reward: {rew}")