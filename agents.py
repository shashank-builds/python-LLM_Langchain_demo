import os
from autogen import AssistantAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ResearchAgents:
    def __init__(self,api_key,base_url):
        self.openai_api_key = api_key
        self.openai_base_url = base_url
        self.llm_config = {'config_list': [{'model': 'gpt4otest',"base_url":self.openai_base_url,'api_key':self.openai_api_key,"api_type": "azure","api_version":"2025-01-01-preview"}]}

        # Summarizer Agent - Summarizes research papers
        self.summarizer_agent = AssistantAgent(
            name="summarizer_agent",
            system_message="Summarize the retrieved research papers and present concise summaries to the user, JUST GIVE THE RELEVANT SUMMARIES OF THE RESEARCH PAPER AND NOT YOUR THOUGHT PROCESS.",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config=False
        )

        # Advantages and Disadvantages Agent - Analyzes pros and cons
        self.advantages_disadvantages_agent = AssistantAgent(
            name="advantages_disadvantages_agent",
            system_message="Analyze the summaries of the research papers and provide a list of advantages and disadvantages for each paper in a pointwise format. JUST GIVE THE ADVANTAGES AND DISADVANTAGES, NOT YOUR THOUGHT PROCESS",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config=False
        )

    def summarize_paper(self, paper_summary):
        """Generates a summary of the research paper."""
        summary_response = self.summarizer_agent.generate_reply(
            messages=[{"role": "user", "content": f"Summarize this paper: {paper_summary}"}]
        )
        return summary_response.get("content", "Summarization failed!") if isinstance(summary_response, dict) else str(summary_response)

    def analyze_advantages_disadvantages(self, summary):
        """Generates advantages and disadvantages of the research paper."""
        adv_dis_response = self.advantages_disadvantages_agent.generate_reply(
            messages=[{"role": "user", "content": f"Provide advantages and disadvantages for this paper: {summary}"}]
        )
        return adv_dis_response.get("content", "Advantages and disadvantages analysis failed!")  if isinstance(adv_dis_response, dict) else str(adv_dis_response)