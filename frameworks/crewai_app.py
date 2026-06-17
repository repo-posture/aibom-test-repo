from crewai import Agent, Task, Crew, Process
from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

# Framework: crewai
# Libraries: langchain-anthropic, langchain-google-genai
# Models: gpt-4o, claude-3-5-sonnet-20241022, gemini-1.5-flash

researcher = Agent(
    role="Senior Researcher",
    goal="Find accurate and up-to-date information on {topic}",
    backstory="Expert researcher with deep analytical skills.",
    llm=ChatOpenAI(model="gpt-4o"),
    verbose=False,
)

analyst = Agent(
    role="Data Analyst",
    goal="Analyze research findings and extract key insights",
    backstory="Skilled at turning raw data into actionable insights.",
    llm=ChatAnthropic(model="claude-3-5-sonnet-20241022"),
    verbose=False,
)

writer = Agent(
    role="Technical Writer",
    goal="Write clear and concise reports",
    backstory="Expert at communicating complex ideas simply.",
    llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash"),
    verbose=False,
)

research_task = Task(description="Research the topic: {topic}", agent=researcher)
analysis_task = Task(description="Analyze the research output.", agent=analyst)
write_task = Task(description="Write a final report based on analysis.", agent=writer)

crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, write_task],
    process=Process.sequential,
)
