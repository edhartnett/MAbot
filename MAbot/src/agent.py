"""Defining an agent."""
from typing import Literal

from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.chains.base import Chain
from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner,
)
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

from tool_loader import load_tools
#from config import set_environment

#set_environment()

ReasoningStrategies = Literal["zero-shot-react", "plan-and-solve"]


def load_agent(tool_names: list[str], strategy: ReasoningStrategies = "zero-shot-react") -> Chain:
    #llm = ChatAnthropic(model="anthropic:claude-3-5-haiku-latest", temperature=0, streaming=True)
    llm = ChatAnthropic(
    model="claude-3-5-haiku-latest",
    temperature=0,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
    # api_key="...",
    # base_url="...",
    # other params...
    )
    tools = load_tools(tool_names=tool_names, llm=llm)
    if strategy == "plan-and-solve":
        planner = load_chat_planner(llm)
        executor = load_agent_executor(llm, tools, verbose=True)
        return PlanAndExecute(planner=planner, executor=executor, verbose=True)

    prompt = hub.pull("hwchase17/react")
    return AgentExecutor(
        agent=create_react_agent(llm=llm, tools=tools, prompt=prompt), tools=tools
    )
