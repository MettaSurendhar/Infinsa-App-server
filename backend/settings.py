from data import prompts
from haystack.dataclasses import ChatMessage, ChatRole

## Global Variables :

bank_chat_history = [
    ChatMessage(
        content="""You are 'Infinsa Intelligence,' a financial assistant. Provide insights and tips on navigating and utilizing digital banking effectively.""",
        role=ChatRole.SYSTEM,
        name="Infinsa-Agent")
]

plan_chat_history = [
    ChatMessage(
        content="""You are 'Infinsa Intelligence,' a financial assistant. Help create a strategic financial plan tailored for long-term goals and short-term needs.""",
        role=ChatRole.SYSTEM,
        name="Infinsa-Agent")
]

learn_chat_history = [
    ChatMessage(
        content="""You are 'Infinsa Intelligence,' a financial assistant. Explain key financial concepts in an easy-to-understand manner to promote financial literacy.""",
        role=ChatRole.SYSTEM,
        name="Infinsa-Agent")
]

## Functions 

def get_prompt_by_category(category):
    matched_prompts= list(filter(lambda p: p["category"] == category, prompts))
    return matched_prompts[0]["prompt"]

def get_chat_message_user(prompt):
  return [ChatMessage(content=prompt, role=ChatRole.USER, name="Metta")]

def get_chat_message_assistant(prompt):
  return [ChatMessage(content=prompt, role=ChatRole.ASSISTANT, name="Infinsa-Intelligence")]

def get_chat_history_by_type(type):
  if type == "bank":
    return bank_chat_history
  elif type == "plan":
    return plan_chat_history
  elif type == "learn":
    return learn_chat_history