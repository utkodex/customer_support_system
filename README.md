# **CUSTOMER SUPPORT SYSTEM**

This scrapes the data from Flipkart
Creates the **RAG** out of database and provide insightful response with the help of **LLM**
---

## Table of Contents

* [Installation](#installation)

  * [Exporting PATH](#exporting-path)
  * [Checking Conda Version](#checking-conda-version)
  * [Creating a Conda Environment](#creating-a-conda-environment)
  * [Activating the Conda Environment](#activating-the-conda-environment)
  * [Alternative Activation (Source Command)](#alternative-activation-source-command)

## Installation

### 1. **Exporting PATH**

```bash
export PATH="/c/ProgramData/anaconda3/bin:/c/ProgramData/anaconda3/Scripts:$PATH"
```

* **What it does:**
  Updates the system's `PATH` environment variable to include the paths for Anaconda's `bin` and `Scripts` directories. This ensures that Anaconda's commands (like `conda`) can be executed from the terminal.
* **Why it’s needed:**
  If `conda` commands are not recognized in your terminal, it could mean that Anaconda's executables are not in your system's `PATH`. This command fixes that issue.

---

### 2. **Checking Conda Version**

```bash
conda --version
```

* **What it does:**
  Displays the currently installed version of Conda on your system.
* **Why it’s needed:**
  Verifies that Conda is properly installed and accessible before proceeding with environment setup.

---

### 3. **Creating a Conda Environment**

```bash
conda create -p venv python=3.10 -y
```

* **What it does:**

  * Creates a new Conda environment in a directory named `venv`.
  * The `-p` flag specifies the path for the environment.
  * Installs Python version 3.10 in the environment.
  * The `-y` flag automatically confirms the environment creation without prompting for user input.
* **Why it’s needed:**
  Isolates your project dependencies by creating a virtual environment, ensuring they don't interfere with global Python or other projects.

---

### 4. **Activating the Conda Environment**

```bash
conda activate "<path to venv>"
```

* **What it does:**
  Activates the Conda environment located at the specified path (`<path to venv>`), making the environment's Python and installed libraries accessible.
* **Why it’s needed:**
  You must activate the environment to run Python scripts or install libraries in the specific environment.

---

### 5. **Alternative Activation (Source Command)**

```bash
source activate ./venv
```

* **What it does:**
  Activates the Conda environment using the `source` command, typically used in Unix/Linux-based systems or Windows PowerShell.
* **Why it’s needed:**
  An alternative to `conda activate`, particularly useful on systems where `conda activate` might not work or requires additional configuration.

---

## If it shows the SSL certificate error use these cammands
```bash
unset SSL_CERT_FILE
set SSL_CERT_FILE=
```

## For running Fast API

```cmd
uvicorn main:app --reload --port 8001
```

![Alt Text](images/chatbot.jpeg)