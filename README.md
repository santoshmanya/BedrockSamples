# BedrockSamples
Mini repo to evaluate AWS Bedrock services based on AWS sample code. As a java programmer, I organized code into packages
![image](https://github.com/santoshmanya/BedrockSamples/assets/4672235/2e2af213-8251-4f0d-851d-579f12901fd9)

**Prerequisites**
%pip install --no-build-isolation --force-reinstall \
    "boto3>=1.28.57" \
    "awscli>=1.29.57" \
    "botocore>=1.31.57"
    
**text**
%pip install  \
    "langchain>=0.0.350" \
    "transformers>=4.24,<5" \
    sqlalchemy -U \
    "faiss-cpu>=1.7,<2" \
    "pypdf>=3.8,<4" \
    pinecone-client==2.2.4 \
    apache-beam==2.52. \
    tiktoken==0.5.2 \
    "ipywidgets>=7,<8" \
    matplotlib==3.8.2 \
    anthropic==0.9.0
    
%pip install datasets==2.15.0

%pip install numexpr==2.8.8

**agents**
%pip install --quiet \
    xmltodict==0.13.0  \
    duckduckgo-search  \
    yfinance  \
    pandas_datareader  \
    langchain_experimental \
    pysqlite3 \
    google-search-results
    
****entity extraction**

**%pip install --quiet beautifulsoup4==4.12.2
**image**

%pip install --quiet "pillow>=9.5,<10"

**guardrails**

%%bash
apt-get update && apt-get install g++ -y
%pip install -qU --no-cache-dir nemoguardrails==0.5.0

%pip install -qU "faiss-cpu>=1.7,<2" \
                      "langchain>=0.0.350" \
                      "pypdf>=3.8,<4" \
                      "ipywidgets>=7,<8"
