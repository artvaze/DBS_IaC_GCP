# GCP Resource Deployment Scripts

This repository contains Python scripts for deploying infrastructure on Google Cloud Platform (GCP) using the Google Cloud Python client libraries. Each script demonstrates different GCP setup scenarios, helping students understand how to create, configure, and troubleshoot resources on GCP.

## Files in the Repository

1. **deploy_gcp_compute_instances.py**
   - This is the base script that sets up three VM instances within the default network on GCP. It serves as a starting point for deploying basic compute instances in a default network setup.

2. **deploy_gcp_compute_instances_extended.py**
   - This extended version deploys a more complex infrastructure, including:
     - Three VM instances with increased machine types.
     - A firewall rule that allows SSH and HTTP traffic.
   - This script is useful for understanding network security configurations and more advanced instance setups.

3. **deploy_gcp_compute_instances_incomplete.py**
   - This script is intentionally incomplete and contains errors. Key configurations are missing, such as credentials and disk setup. The purpose is for students to review and correct the code to ensure successful deployment.

## Running the Scripts

1. Clone this repository and navigate to the folder:
   ```bash
   git clone https://github.com/artvaze/DBS_IaC_GCP.git
   cd DBS_IaC_GCP
   ```

2. Install the necessary dependencies:
   ```bash
   pip install google-cloud-compute google-auth
   ```

3. Run each script with:
   ```bash
   python script_name.py
   ```

## Educational Objective

These scripts provide practical examples of infrastructure as code on GCP, allowing students to learn by setting up resources and fixing deployment issues.
