# 🚀 Data Version Control (DVC) Project  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Git](https://img.shields.io/badge/Git-Enabled-orange)  
![DVC](https://img.shields.io/badge/DVC-Integrated-green)  

> This repository demonstrates how to integrate **DVC (Data Version Control)** with GitHub for efficient dataset tracking and versioning.  

---


## 🎯 Why This Project?

- 🔄 Keep **datasets in sync** with code commits  
- 📂 Enable **data versioning** without bloating Git history  
- ☁️ Store large files remotely (e.g., S3, GCS, Azure)  
- 🤝 Collaborate seamlessly across teams  
- 🧪 Ensure experiments are **fully reproducible**  

## 📂 Project Flow  

```mermaid
flowchart TD
    A[Create Git Repo] --> B[Clone Locally]
    B --> C[Add mycode.py & Generate Data]
    C --> D[git add/commit/push]
    D --> E[dvc init]
    E --> F[Create S3 Directory]
    F --> G[dvc remote add myremote S3]
    G --> H[dvc add data/]
    H --> I[git rm cached data/]
    I --> J[dvc commit & push]
    J --> K[git commit & push]
    K --> L[Modify Data → New Version]
    L --> M[dvc commit & push again]



