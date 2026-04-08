from typing import Tuple, Dict
from env.models import Observation, Action, Reward, Email
from env.tasks import load_task

class EmailEnv:
    def __init__(self, task_id="easy"):
        self.task = load_task(task_id)
        self.reset()

    def reset(self) -> Observation:
        self.inbox = [Email(**e) for e in self.task["emails"]]
        self.labels = self.task["labels"]
        self.index = 0
        self.total_reward = 0
        return self.state()

    def state(self) -> Observation:
        current = self.inbox[self.index] if self.index < len(self.inbox) else None
        return Observation(
            inbox=self.inbox,
            current_email=current,
            time_step=self.index
        )

    def step(self, action: Action) -> Tuple[Observation, Reward, bool, Dict]:
        if self.index >= len(self.inbox):
            return self.state(), Reward(score=0, reason="done"), True, {}

        email = self.inbox[self.index]
        correct = self.labels[email.id]

        reward = 0
        reason = ""

        # Classification
        if action.action_type == "classify":
            if action.label == correct:
                reward += 2
                reason = "correct classification"
            else:
                reward -= 1
                reason = "wrong classification"

        # Reply
        elif action.action_type == "reply":
            if correct != "spam" and action.response:
                reward += 1
                reason = "good reply"
            else:
                reward -= 2
                reason = "bad reply"

        # Delete
        elif action.action_type == "delete":
            if correct == "spam":
                reward += 1
                reason = "correct delete"
            else:
                reward -= 3
                reason = "deleted important email"

        # Skip
        elif action.action_type == "skip":
            reward -= 0.5
            reason = "skipped email"

        self.total_reward += reward
        self.index += 1

        done = self.index >= len(self.inbox)

        return self.state(), Reward(score=reward, reason=reason), done, {}