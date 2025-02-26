import json
import logging

import requests
from dotenv import load_dotenv
from duckduckgo_search.exceptions import DuckDuckGoSearchException
from langchain.chains.base import Chain
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from requests import RequestException, Response

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define Pydantic model for GitHub user info
class GithubInfo(BaseModel):
    name: str = Field(description="Name of the user in github repo")
    github_username: str = Field(description="Person github username")
    followers: int = Field(description="User number of followers")
    following: int = Field(description="User number of following")
    repo_count: int = Field(description="User number of repository")
    description: str = Field(description="Create a small summary about the user")
    image_url: str = Field(description="Github profile pic url of the user")


# Function to store results into a JSON file for debugging
def store_results(results: dict, result_type: str, username: str) -> None:
    store_data = {result_type: results, "username": username}
    try:
        with open("debug.json", "w") as file:
            json.dump(store_data, file, indent=4)
    except Exception as ex:
        logger.error(f"Error storing results to file: {ex}")


# Github api call function
def github_user_details(username: str) -> dict:
    response: dict = {}
    try:
        api_response: Response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        response = api_response.json()
    except RequestException as ex:
        print(f"Exception during github api call: {str(ex)}")
    return response


# DuckDuckGo search function
def duckduckgo_search(username: str) -> str:
    try:
        duckduckgo_search_tool = DuckDuckGoSearchResults(output_format="list")
        results = duckduckgo_search_tool.invoke(username)
        store_results(results, "duckduckgo_search", username)
        return str(results)
    except DuckDuckGoSearchException as ex:
        logger.error(f"Error during DuckDuckGo search: {ex}")
        return "No results found"


# Create the Langchain chain for processing GitHub user info
def create_langchain_chain() -> Chain:
    # Create the prompt templates to be in the chains
    github_prompt = """
        User github profile data: {data}
    """

    user_prompt = """
        Using the info, create an innovative information in markdown format of the user with {name} and {username}.

        User github info: {user_info}
        DuckDuckGo Search Results: {duckduckgo_results}
    """

    github_prompt_template = PromptTemplate.from_template(github_prompt)
    user_prompt_template = PromptTemplate.from_template(user_prompt)

    # Create the instance of the LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm_structured = llm.with_structured_output(GithubInfo)

    # Setup the chain
    chain = (
        github_prompt_template
        | llm_structured
        | {
            "user_info": RunnablePassthrough() | str,
            "name": RunnableLambda(lambda input: input.name),
            "username": RunnableLambda(lambda input: input.github_username),
            "duckduckgo_results": RunnableLambda(lambda input: duckduckgo_search(input.github_username)),
        }
        | user_prompt_template
        | llm
        | StrOutputParser()
    )

    return chain


# Entry point
if __name__ == "__main__":
    # Take the username that you want to use to create the markdown text
    username = "yash0307jain"

    # Call the github api to get the user data using username
    github_user_data = github_user_details(username=username)

    # Create the langchain chain
    chain = create_langchain_chain()

    # Invoke the langchain chain
    output = chain.invoke({"data": str(github_user_data)})

    # Print the output
    logger.info(f"Output for {username}: {output}")
