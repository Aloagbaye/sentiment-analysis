# ✅ GitHub Actions YAML Cheat Sheet

### 📁 File Location
```bash
.github/workflows/your-workflow-name.yml
```

---

### 🏷️ `name`
Defines the workflow’s name (appears in GitHub UI).

```yaml
name: CI Pipeline
```

---

### ⚡ `on`
Specifies **trigger events** for the workflow.

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: "0 0 * * 0"    # Every Sunday at midnight UTC
  workflow_dispatch:        # Manual trigger
```

---

### 🧱 `jobs`
Defines one or more jobs that can run in parallel or in sequence.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps: ...
```

---

### 🧭 `runs-on`
Specifies the **runner machine** for the job.

```yaml
runs-on: ubuntu-latest    # or macos-latest / windows-latest
```

---

### ⛴️ `services` (Docker containers for testing)
Attach services like PostgreSQL, Redis, etc.

```yaml
services:
  postgres:
    image: postgres:14
    env:
      POSTGRES_DB: app
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    ports:
      - 5432:5432
    options: >-
      --health-cmd="pg_isready"
      --health-interval=10s
      --health-timeout=5s
      --health-retries=5
```

---

### 🌱 `env`
Global environment variables for all steps in the job.

```yaml
env:
  DB_HOST: localhost
  DB_PORT: 5432
```

---

### 🪜 `steps`
Each job runs a series of steps.

#### 🔁 Checkout Code
```yaml
- uses: actions/checkout@v3
```

#### 🐍 Setup Python
```yaml
- uses: actions/setup-python@v4
  with:
    python-version: 3.11
```

#### 🐳 Setup Docker
```yaml
- uses: docker/setup-buildx-action@v3
```

#### 🔐 Login to DockerHub
```yaml
- uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

#### 📦 Build and Push Image
```yaml
- uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: ${{ secrets.DOCKER_USERNAME }}/my-image:latest
```

#### 🧪 Run Shell Commands
```yaml
- name: Run Tests
  run: pytest tests/
```

---

### 🔗 `needs`
Make a job run **after** another job completes successfully.

```yaml
jobs:
  test:
    ...
  deploy:
    needs: test
```

---

### 🔐 `secrets`
Securely reference sensitive values (like tokens or passwords).

```yaml
with:
  token: ${{ secrets.MY_SECRET }}
```

Set via **Repository → Settings → Secrets and Variables → Actions**

---

### 📌 Reusable Workflow Snippets

#### Python Project
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install pytest
```

#### Wait for Database
```yaml
- name: Wait for Postgres
  run: |
    until pg_isready -h localhost -p 5432; do echo "Waiting..."; sleep 2; done
```

---

### 🔁 Common Actions

| Action | Purpose |
|--------|---------|
| `actions/checkout` | Clones repo |
| `actions/setup-node` | Sets up Node.js |
| `actions/setup-python` | Sets up Python |
| `docker/login-action` | Logs into Docker Hub |
| `docker/build-push-action` | Builds & pushes Docker image |
| `github/codeql-action/init` | Code scanning with CodeQL |

---

### 🧪 Test Matrix (Optional)
Run tests in parallel across different OS or Python versions:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    python: [3.9, 3.10]

runs-on: ${{ matrix.os }}
steps:
  - uses: actions/setup-python@v4
    with:
      python-version: ${{ matrix.python }}
```

---

### 📘 More Tips

- Comments start with `#`
- Use `>` or `|-` for multi-line strings:
  ```yaml
  run: >-
    echo "This is a single line string"
  ```

- Workflows fail if **any step returns a non-zero exit code** (unless you use `continue-on-error: true`).