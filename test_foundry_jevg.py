# Before running the sample:
#    pip install --pre azure-ai-projects>=2.0.0b1
#    pip install azure-identity

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

myEndpoint = "https://gpt4-workshop-jevg-resource.services.ai.azure.com/api/projects/gpt4-workshop-jevg"

project_client = AIProjectClient(
    endpoint=myEndpoint,
    credential=DefaultAzureCredential(),
)

myAgent = "Test-gpt4-agent-jevg"
# Get an existing agent
agent = project_client.agents.get(agent_name=myAgent)
print(f"Retrieved agent: {agent.name}")

openai_client = project_client.get_openai_client()

# Use the AIProjectClient high-level chat API to call the agent directly.
# This avoids constructing an OpenAI-compatible payload manually and
# prevents issues decoding project/AML connections.
resp = project_client.chat.create(
    agent_reference=agent.name,
    messages=[{"role": "user", "content": "Tell me what you can help with."}],
)

try:
    # `resp` may have different shapes; prefer `output_text` when available.
    out = getattr(resp, "output_text", None) or getattr(resp, "content", None) or resp
    print(f"Response output: {out}")
except Exception:
    print("Received response object:", resp)



