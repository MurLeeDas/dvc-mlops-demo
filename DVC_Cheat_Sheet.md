# DVC CHEAT SHEET - Quick Reference Guide

## INSTALLATION
```bash
# Install DVC with S3 support
pip install dvc[s3]

# Verify installation
dvc version
```

---

## INITIALIZATION

```bash
# Initialize DVC in existing Git repo
dvc init

# Initialize Git + DVC (new project)
git init
dvc init
```

---

## REMOTE STORAGE CONFIGURATION

```bash
# Add S3 remote (default)
dvc remote add -d myremote s3://bucket-name/path

# Add other remotes
dvc remote add gdrive gdrive://folder-id              # Google Drive
dvc remote add azure azure://container/path           # Azure
dvc remote add gs gs://bucket-name/path               # Google Cloud

# List remotes
dvc remote list

# Modify remote URL
dvc remote modify myremote url s3://new-bucket/path

# Remove remote
dvc remote remove myremote
```

---

## TRACKING DATA

```bash
# Track single file
dvc add data/dataset.csv

# Track entire directory
dvc add data/raw/

# Track multiple files
dvc add data/*.csv

# What happens:
# 1. Creates .dvc file (metadata)
# 2. Adds actual file to .gitignore
# 3. Stores file in .dvc/cache/
```

---

## GIT + DVC WORKFLOW

```bash
# Standard workflow
dvc add data/dataset.csv          # Track with DVC
git add data/dataset.csv.dvc      # Track metadata with Git
git add .gitignore                # Update gitignore
git commit -m "Add dataset v1"    # Commit to Git
dvc push                          # Upload to remote storage

# Update workflow (when data changes)
dvc add data/dataset.csv          # Re-track updated file
git add data/dataset.csv.dvc      # Commit new metadata
git commit -m "Update dataset v2"
dvc push                          # Upload new version
```

---

## PULLING & PUSHING DATA

```bash
# Upload data to remote storage
dvc push

# Download data from remote storage
dvc pull

# Download specific file
dvc pull data/dataset.csv.dvc

# Force re-download (ignore cache)
dvc pull --force

# Push/pull with specific remote
dvc push -r myremote
dvc pull -r myremote
```

---

## TIME TRAVEL (VERSION SWITCHING)

```bash
# List commits
git log --oneline

# Switch to specific version
git checkout <commit-hash>        # Switch Git version
dvc checkout                      # Download matching data

# Return to latest
git checkout main
dvc checkout

# Switch to specific tag
git checkout v1.0
dvc checkout
```

---

## STATUS & INFORMATION

```bash
# Check DVC status
dvc status                        # Show tracked files status

# Check what's changed
dvc diff                          # Compare with last commit

# Show file info
dvc list . data/                  # List DVC-tracked files

# Validate tracked files
dvc status --cloud                # Check cloud vs local
```

---

## CACHE MANAGEMENT

```bash
# Clear local cache
dvc cache clear

# Show cache directory
dvc cache dir

# Move cache to different location
dvc cache dir --local /path/to/new/cache

# Remove unused cache files
dvc gc --workspace
```

---

## UNTRACKING FILES

```bash
# Stop tracking file (keeps data)
dvc remove data/dataset.csv.dvc

# Remove from DVC and delete data
dvc remove data/dataset.csv.dvc
rm data/dataset.csv
```

---

## PIPELINES

```bash
# Create pipeline stage
dvc stage add -n preprocess \
  -d data/raw.csv \
  -o data/processed.csv \
  python preprocess.py

# Run pipeline
dvc repro

# Show pipeline DAG
dvc dag
```

---

## USEFUL COMMANDS

```bash
# Get help
dvc --help
dvc add --help

# Check configuration
cat .dvc/config

# Verify remote connection
dvc remote list
aws s3 ls s3://bucket-name/       # For S3

# Update DVC
pip install --upgrade dvc[s3]
```

---

## COMMON WORKFLOWS

### 📌 New Project Setup
```bash
mkdir my-ml-project
cd my-ml-project
git init
dvc init
dvc remote add -d storage s3://my-bucket/dvc-store
git add .dvc/
git commit -m "Initialize DVC"
```

### 📌 Track New Dataset
```bash
dvc add data/train.csv
git add data/train.csv.dvc .gitignore
git commit -m "Add training dataset"
dvc push
git push
```

### 📌 Clone Project & Get Data
```bash
git clone <repo-url>
cd <repo>
dvc pull                          # Downloads all data
```

### 📌 Update Dataset
```bash
# Modify data/train.csv
dvc add data/train.csv
git add data/train.csv.dvc
git commit -m "Update training data"
dvc push
git push
```

### 📌 Share Data with Team
```bash
# Team member workflow
git pull                          # Get latest .dvc files
dvc pull                          # Download latest data
```

---

## TROUBLESHOOTING

### ❌ Problem: `dvc push` fails with "Access Denied"
```bash
# Check AWS credentials
aws sts get-caller-identity
aws s3 ls s3://bucket-name/

# Verify IAM permissions (need: PutObject, GetObject, ListBucket)
```

### ❌ Problem: `dvc pull` does nothing
```bash
# Check status
dvc status

# Verify remote configured
dvc remote list
cat .dvc/config

# Force pull
dvc pull --force
```

### ❌ Problem: Hash mismatch errors
```bash
# Clear cache
dvc cache clear

# Re-pull
dvc pull --force
```

### ❌ Problem: Git and DVC out of sync
```bash
# Always follow order:
# 1. dvc add
# 2. git add .dvc
# 3. git commit
# 4. dvc push
# 5. git push
```

---

## BEST PRACTICES

✅ **Always commit .dvc files to Git**
```bash
git add data/dataset.csv.dvc
git commit -m "Track dataset"
```

✅ **Push DVC and Git together**
```bash
dvc push && git push
```

✅ **Use meaningful commit messages**
```bash
git commit -m "Add 500k new customer reviews to training data"
```

✅ **Don't commit large files to Git**
```bash
# Check .gitignore includes:
/data/*.csv
/data/*.parquet
```

✅ **Use DVC for files > 10MB**
```bash
# Smaller files: Git is fine
# Larger files: Use DVC
```

✅ **Enable S3 versioning** (backup for DVC storage)
```bash
aws s3api put-bucket-versioning \
  --bucket my-bucket \
  --versioning-configuration Status=Enabled
```

---

## FILE STRUCTURE REFERENCE

```
my-ml-project/
├── .git/                         # Git repository
├── .dvc/
│   ├── config                    # DVC configuration
│   ├── .gitignore               # Ignore DVC cache
│   └── cache/                   # Local DVC cache
├── data/
│   ├── raw/
│   │   └── dataset.csv          # Actual data (gitignored)
│   └── raw.dvc                  # DVC metadata (in Git)
├── .gitignore                   # Ignore data files
└── README.md
```

---

## QUICK COMPARISON

| Action | Git | DVC |
|--------|-----|-----|
| Track file | `git add file.py` | `dvc add data.csv` |
| Commit | `git commit` | `git commit` (commit .dvc file) |
| Upload | `git push` | `dvc push` |
| Download | `git pull` | `dvc pull` |
| Restore version | `git checkout <hash>` | `git checkout <hash>` + `dvc checkout` |

---

## INTEGRATION WITH MLOps TOOLS

### With MLflow
```bash
# Track training data
dvc add data/train.csv

# MLflow logs model
# DVC tracks data
# Both tracked together in Git
```

### With CI/CD
```yaml
# GitLab CI example
script:
  - dvc pull              # Get latest data
  - python train.py       # Train model
  - dvc add models/model.pkl
  - dvc push              # Upload model
```

---

## USEFUL LINKS

- Official Docs: https://dvc.org/doc
- Tutorial: https://dvc.org/doc/start
- Use Cases: https://dvc.org/doc/use-cases
- Community: https://discord.com/invite/dvwXA2N

---

**Pro Tip:** Treat DVC commands like Git commands. The workflow is intentionally similar!

```
dvc add = git add (for data)
dvc push = git push (to cloud storage)
dvc pull = git pull (from cloud storage)
```

---

**Created for MLOps Training Session**
*Last Updated: [22-Jan-2026]*
