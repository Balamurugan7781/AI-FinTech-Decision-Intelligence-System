# AI Fintech Decision Intelligence System

A production-style AI system that evaluates loan applications using probability of default (PD) modelling and financial decision logic.

---

## 🚧 Status

Work in Progress — Enhancing system with API integration, improved modelling, and deployment capabilities.

---

## 🏗️ System Architecture

User Input → Feature Processing → PD Model → Financial Engine → Decision Engine → Explanation

---

## ⚙️ Core Logic

### 1. Probability of Default (PD)
- Estimated using borrower features such as credit score and income
- Higher credit score → lower PD  
- Higher income → lower PD  

---

### 2. Financial Evaluation

- Expected Loss = PD × Loan Amount × LGD  
- Expected Profit = Interest Rate × Loan Amount × (1 - PD)  

Where:
- LGD = Loss Given Default (assumed recovery-adjusted loss)

---

### 3. Decision Engine

- APPROVED → Low risk and profitable  
- REVIEW → Moderate risk  
- REJECTED → High risk  

---

## 🚀 Features

- Probability of Default (PD) modelling  
- Risk vs profit evaluation  
- Explainable decision outputs  
- Modular system design  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- SQLite  
- (Upcoming) FastAPI  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
