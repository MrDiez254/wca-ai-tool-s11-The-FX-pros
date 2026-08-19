# 🛒 AI Supermarket Sales Optimizer

> **Repository:** `wca-ai-tool-s11-The-FX-pros`  
> **Course:** WeCan Academy AI Course — Season 11 Group Project  

---

## 👥 Group Members & Roles

* **[Isaac Macharia]** — System Integrator (`main.py`)
* **[Duncan Mugo]** — Stage 1 Guardrail Developer (`stage_1_guardrail.py`)
* **[Benson Kimani]** — Stage 2 Strategist Developer (`stage_2_strategist.py`)
* **[Tidal Okoth]** — Database Manager & RAG Context (`database_manager.py`)
* **[Michael Bethe]** — Report Generator (`report_generator.py`)

---

## 📖 What the Tool Does

This tool is a CLI application that helps retail managers handle supermarket inventory issues through a two-stage AI workflow:

1. **Stage 1 (Guardrail & Input Analysis):** Evaluates user inputs for relevance to retail operations and extracts key inventory issues.
2. **Stage 2 (Action Plan Generation):** Combines database inventory context with Gemini API analysis to generate actionable sales and stock strategies.
3. **Report Saving:** Automatically exports the final recommendations to a local file for record-keeping.

---

## ⚙️ Project Architecture

* **`main.py`**: Interactive CLI menu and two-stage pipeline controller.
* **`stage_1_guardrail.py`**: Prompt logic for validating retail inputs.
* **`stage_2_strategist.py`**: Prompt logic for generating retail strategies.
* **`database_manager.py`**: Queries stock levels and product catalog.
* **`report_generator.py`**: Saves generated strategies to text/markdown format.

---

## 🚀 Quickstart & Setup

### 1. Prerequisites
* Python 3.10 or higher

### 2. Install Dependencies
```bash
pip install -r requirements.txt