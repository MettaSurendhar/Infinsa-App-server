from typing import Any, Union
from haystack.core.component import component
from haystack.components.builders import PromptBuilder,ChatPromptBuilder
from haystack_integrations.components.generators.google_ai import GoogleAIGeminiGenerator,GoogleAIGeminiChatGenerator
from haystack import Pipeline
from dotenv import load_dotenv
import os

os.environ["GOOGLE_API_KEY"]="AIzaSyDI4oqkPgsZIqlhnM2ra-VhuOSRWBs1nMM"

@component
class Agent:

  def __init__ (self,prompt):
    self.prompt_builder = PromptBuilder(template=prompt)
    self.generator = GoogleAIGeminiGenerator(model="gemini-1.5-flash")
    self.pipeline = Pipeline()
    self.pipeline.add_component("prompt_builder", self.prompt_builder)
    self.pipeline.add_component("generator", self.generator)
    self.pipeline.connect("prompt_builder", "generator")

  @component.output_types(response=dict[str, Any])
  def run(self, query: str, data: dict[str:Any]):
    result = self.pipeline.run(
      data={
        "prompt_builder": {{"query": query}, {"data":data}}
      })
    response = result["generator"]["replies"][0]

    return response

@component
class ChatAgent:

  def __init__ (self,chat_history):
    self.chat_history = chat_history  
    self.prompt_builder = ChatPromptBuilder()
    self.generator = GoogleAIGeminiChatGenerator(model="gemini-1.5-flash")
    self.pipeline = Pipeline()
    self.pipeline.add_component("prompt_builder", self.prompt_builder)
    self.pipeline.add_component("generator", self.generator)
    self.pipeline.connect("prompt_builder", "generator")

  @component.output_types(response=dict[str, Any])
  def run(self, query: str, data: dict[str:Any], prompt: str):

    messages= self.chat_history + prompt
    result = self.pipeline.run(
      data={
        "prompt_builder": {
          "template_variables":{"query": query, "data":data},
          "template": messages
          }
      })
    response = result["generator"]["replies"][0].content

    return {"response":response}
