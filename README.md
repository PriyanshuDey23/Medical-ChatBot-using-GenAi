# Medical-ChatBot-using-GenAi

# End-to-End Medical Chatbot - Generative AI

An advanced, end-to-end generative AI chatbot designed for the medical domain, leveraging Pinecone for vector indexing, OpenAI's GPT for generative responses, and LangChain for seamless language model integration. This project includes cloud deployment via AWS with CI/CD setup using GitHub Actions.

## Getting Started

### Prerequisites

To run this project, you will need:

- [Python 3.10](https://www.python.org/)
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for environment management
- AWS account with EC2 and ECR access
- OpenAI and Pinecone API credentials

### Installation and Setup

Follow these steps to set up and run the chatbot locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PriyanshuDey23/Medical-ChatBot-using-GenAi
   
   ```

2. **Create a Conda Environment**
   ```bash
   conda create -n medibot python=3.10 -y
   conda activate medibot
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   
   Create a `.env` file in the project root directory and add your Pinecone and OpenAI credentials:
   ```ini
   PINECONE_API_KEY="your-pinecone-api-key"
   GOOGLE_API_KEY="your-google-api-key"
   ```

5. **Store Embeddings to Pinecone**
   ```bash
   python store_index.py
   ```

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Chatbot**
   
   Open `localhost` in your browser to interact with the chatbot.

---

## Tech Stack

- **Python**
- **LangChain** - Language model orchestration
- **Flask** - Web framework for hosting the chatbot
- **GOOGLE GEMINI** - Generative AI for chatbot responses
- **Pinecone** - Vector database for indexing and retrieval

---

## AWS CI/CD Deployment with GitHub Actions

### Step 1: AWS Setup

1. **Login to AWS**: Access your AWS Management Console.
2. **Create IAM User**: Configure a deployment-specific IAM user with the following policies:
   - `AmazonEC2ContainerRegistryFullAccess` for ECR access
   - `AmazonEC2FullAccess` for EC2 management

3. **Create ECR Repository**
   - Navigate to ECR and create a new repository.
   - Note the repository URI, e.g., `970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot`.

4. **Launch an EC2 Instance** (Ubuntu recommended):
   - Open EC2 and configure a new Ubuntu instance.
   - Install Docker on EC2 with the following commands:
     ```bash
     sudo apt-get update -y
     sudo apt-get install -y docker.io
     sudo usermod -aG docker $USER
     ```

### Step 2: Configure EC2 as a Self-Hosted Runner

Navigate to **Settings > Actions > Runners** in your GitHub repository, select **New self-hosted runner**, and follow the setup instructions.

### Step 3: Set Up GitHub Secrets

In your repository settings, under **Secrets and variables > Actions**, add the following secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO` (your ECR repository URI)
- `PINECONE_API_KEY`
- `GOOGLE_API_KEY`

---

## Deployment Overview

1. **Build Docker Image**: A Docker image of the source code is built and pushed to ECR.
2. **Deploy on EC2**: The image is pulled from ECR to the EC2 instance, where it is run as a containerized application.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues, please open an issue in this repository. For further questions, reach out to [priyanshudey.ds@example.com].
