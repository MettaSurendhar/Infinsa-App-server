from agents import Agent,ChatAgent
from settings import bank_chat_history, get_prompt_by_category,get_chat_message_user,get_chat_message_assistant,get_chat_history_by_type

# /chat/{type}?category=
# type = account/plan/learn

# /generate/?category=
# recommendations_budget/financial_health

def chat_response_generator(type: str, category: str, query: str, data: str):
  
  chat_history = get_chat_history_by_type(type)
  chat_agent = ChatAgent(chat_history)
  prompt = get_prompt_by_category(category=category)
  user_prompt=get_chat_message_user(prompt)

  result = chat_agent.run(query,data,user_prompt)
  response = result["response"]

  chat_history.append(get_chat_message_user(query))
  chat_history.append(get_chat_message_assistant(response))

  return response

def response_generator(category: str, query: str, data: str):

  prompt = get_prompt_by_category(category=category)
  agent = Agent(prompt)

  result = agent.run(query,data)
  response = result["response"]

  return response


## Example use : 
data={
  "balance":"21,040"
}
# response = chat_response_generator("bank","account","how can i use my account balance usefully ?", data)
# response = response_generator("recommendations_budget","how can i use my account balance usefully ?", data)
# print(response)


