# End-to-End-Text-Summarizer-Project

In this project, I built a text summarizer app that will summarize any text, dialogue, conversation or article. I utilized the Pegasus model and fine-tuned it with the SAMSum dataset.

🔗 **Model**: [Pegasus](https://huggingface.co/docs/transformers/en/model_doc/pegasus)  
🔗 **Dataset**: [SAMSum](https://huggingface.co/datasets/Samsung/samsum)

### **Project Highlights**
What makes this project unique is the integration of **MLOps** techniques:
- **Pipelines**: Implemented Data Ingestion, Validation, Transformation, Model Trainer, Evaluation and Prediction.
- **Docker**: Containerized the source code for easy deployment on AWS ECR and EC2.
- **GitHub Actions**: Set up Continuous Integration and Continuous Deployment.
- **Streamlit App**: Developed an beautiful UI for user interaction.

### **Challenges & Solutions**
1. **Model Fine-Tuning**: Finding the right hyperparameters for the SAMSum dataset required extensive experimentation.
2. **Deployment**: Containerizing and deploying the app on AWS was challenging, but leveraging Docker and GitHub Actions streamlined the process.

### **Results**
- Successfully summarized a chat between me and my friend [@dheerajvoore](https://www.linkedin.com/in/dheerajvoore/) into a short and clear summary.
- The app now processes various text inputs with impressive accuracy.

### **Pegasus Model Performance**:

| Model   | ROUGE-1   | ROUGE-2 | ROUGE-L | ROUGE-Lsum |
|---------|-----------|---------|---------|------------|
| Pegasus | 0.02161   | 0.0     | 0.02131 | 0.02125    |


## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the components
6. update the pipeline
7. update the main.py
8. update the app.py

## Pipelines

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Trainer
5. Model Evaluation

## STEPS

Clone the repository

```bash
git clone https://github.com/CodeWithCharan/Text-Summarizer.git
```
### STEP 01: Create a conda environment after opening the repository

```bash
conda create -n envname python=3.8 -y
```

```bash
conda activate envname
```


### STEP 02: install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03: run streamlit app
```bash
streamlit run app.py
```

### STEP 04: After running the app, it will be available at:

- `http://127.0.0.1:8080`
- `http://localhost:8080`

## AWS CI/CD Deployment with Github Actions

Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2
## Steps:

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

### 4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = ap-south-1

    AWS_ECR_LOGIN_URI =

    ECR_REPOSITORY_NAME = mlproj