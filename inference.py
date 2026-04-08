import os
from openai import OpenAI
from env.environment import EmailEnv
from env.models import Action

# ✅ USE THEIR PROXY
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def llm_agent(email):
    try:
        prompt = f"""
        Classify this email as urgent, normal, or spam:

        Subject: {email.subject}
        Body: {email.body}
        """

        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.lower()

        if "spam" in text:
            return "spam"
        elif "urgent" in text:
            return "urgent"
        else:
            return "normal"

    except Exception:
        # 🔥 FALLBACK (VERY IMPORTANT)
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

    print(f"[START] task={task}", flush=True)

    while True:
        email = obs.current_email

        # ✅ USE LLM (IMPORTANT)
        label = llm_agent(email)

        action = Action(action_type="classify", label=label)

        obs, reward, done, _ = env.step(action)

        total_reward += reward.score
        step += 1

        print(f"[STEP] step={step} reward={reward.score}", flush=True)

        if done:
            break

    print(f"[END] task={task} total_reward={total_reward} steps={step}", flush=True)


if __name__ == "__main__":
    for t in ["easy", "medium", "hard"]:
        run_task(t)