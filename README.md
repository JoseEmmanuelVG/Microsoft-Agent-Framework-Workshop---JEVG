# Microsoft-Agent-Framework-Workshop---JEVG

Microsoft Agent Framework Workshop: 
Pre-Work Requirements
Preparation Steps to Maximize Your Workshop Experience
To ensure we make the most out of our Microsoft Agent Framework workshop, please 
review and complete the following pre-work requirements before the day of the event. The 
goal is for everyone to arrive with their environment set up, so we can focus directly on 
building agents.
��Prerequisite Access
1. Azure OpenAI Access
2. The user account you will use for the workshop must have one of the following roles 
assigned for the Azure OpenAI resource:
o Cognitive Services OpenAI User
o Cognitive Services OpenAI Contributor
3. If you don’t have this access, please request it in advance.
��Visual Studio Code
1. Please install Visual Studio Code and make sure to sign in using the same Azure 
account that will have access to the Azure OpenAI resource.
2. Download: https://code.visualstudio.com/
3. Recommended Extensions:
o Python
o Azure Account
o Azure Resources
��Azure CLI (Required)
1. Install the Azure CLI, as we will run commands during the workshop to validate, list, 
or configure resources.
2. Download and installation: https://learn.microsoft.com/cli/azure/install-azure-cli
After installing, verify with:
az version
Then sign in with the correct user:
az login
��Python Environment Setup
1. Install Python 3.10 or higher.
2. We will use a single virtual environment (.venv) at the root of the workshop 
repository, which will be reused for all modules (01-xxx, 02-yyy, etc.).
3. Executable Note: Depending on your operating system, the Python command may 
differ:
4. Windows: py or python
5. macOS/Linux: python3
Examples use py, but you may substitute the appropriate command for your system.
Steps:
1. Create the virtual environment:
py -m venv .venv
2. Activate it:
macOS / Linux: source .venv/bin/activate
Windows: .venv\Scripts\activate
3. Upgrade pip:
py -m pip install --upgrade pip
4. Install the Agent Framework:
pip install agent-framework
��Workshop Repository
You will receive the repository in advance. The virtual environment should be created once 
at the root and reused for every lab session in the workshop.
Optional: Free Azure Trial Subscription
If needed, you can obtain a free Azure trial subscription here: 
https://azure.microsoft.com/free
