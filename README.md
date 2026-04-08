# Email Triage OpenEnv

## Description
This environment simulates real-world email classification and response tasks.

## Tasks
- Easy: clear spam vs urgent
- Medium: mixed signals
- Hard: ambiguous emails

## Action Space
- classify
- reply
- delete
- skip

## Reward
+2 correct classification  
-1 wrong  
-3 bad delete  
-0.5 skip  

## Run
docker build -t email-env .
docker run email-env

## Baseline
Includes rule-based agent for reproducibility.

## Observation Space
- inbox: list of emails
- current_email: email being processed
- time_step: current index in episode

## Task Difficulty Progression
- Easy: clear keyword-based emails
- Medium: mixed intent and ambiguity
- Hard: realistic emails with unclear intent

## Grading
Score is normalized between 0.0–1.0:
accuracy = correct_predictions / total_emails

This ensures deterministic and reproducible evaluation.

## OpenEnv Compliance
- Uses Pydantic models for Observation, Action, Reward
- Implements reset(), step(), state()
- Includes 3 tasks with increasing difficulty
- Deterministic grader (0–1 scoring)

## Sample Output
easy -> accuracy: 1.0, reward: 4
medium -> accuracy: 0.67, reward: 3
hard -> accuracy: 0.5, reward: 2

## Baseline Agent
A rule-based agent is used for reproducibility.
An optional LLM-based agent can be added using OpenAI API.

