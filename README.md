# ⚖️ VakeelSaab.ai : The Legal Lens  
*An AI-powered Chrome Extension to Demystify Legal Documents*  

![Hackathon](https://img.shields.io/badge/Hackathon-Google%20Cloud's%20Gen%20AI%20Exchange%20Hackathon-blue?logo=googlecloud)  
<!-- ![MadeWith](https://img.shields.io/badge/made%20with-Python%20%26%20JS-1f425f.svg) -->  
<!--![Build](https://img.shields.io/badge/build-passing-brightgreen) -->


<img width="5912" height="1588" alt="banner-desktop" src="https://github.com/user-attachments/assets/2137f3df-e89d-4f23-9f29-07d816c88e8d" />
<!--![Project Banner](./assets/banner.png) <!-- Add hackathon/project banner -->

---

## 🚀 Team Details
- **Team Name:** Codestrome  
- **Problem Statement:** Generative AI for Demystifying Legal Documents  
---

## 📌 Problem Statement
Legal documents (rental agreements, loan contracts, terms & conditions) are written in **dense legalese**, making them inaccessible to non-lawyers and others.  

- Users often **sign risky clauses unknowingly**, leading to financial or legal consequences.  
- Existing summarizers require uploading entire confidential documents, raising **privacy concerns**.  

---

## 💡 Our Solution – *VakeelSaab.ai*
**VakeelSaab.ai: The Legal Lens** is a **privacy-first, AI-powered Chrome Extension** that:  
- Simplifies **legal clauses in real-time** (on webpages & PDFs).  
- Provides **summary, risks, and plain English rewrite**.  
- Ensures **privacy** by processing only selected text.  
- Empowers users with **clarity & confidence** in legal decisions.  

👉 *Highlight → Simplify → Understand → Act*  

---

## ✨ Core Features (MVP)
- 📑 **Clause Highlight & Simplify** – Select any clause and simplify with AI.  
- 🔒 **Privacy-first Processing** – Only highlighted text sent to backend, not entire docs.  
- 🖼 **Interactive UI** – Chrome popup showing *Summary, Risks, Plain English Rewrite*.  
- ⚠️ **Risk Identification** – Highlights potential obligations & penalties.  
- 🗣 **Plain-English Simplification** – Converts legalese to easy-to-read language.  

---

## 🌟 Future Enhancements
- 🟢 **Risk Scoring** – Auto high/medium/low flags with color codes.  
- 📤 **Save/Export** – Share simplified clauses via PDF/email.  
- 🤖 **Follow-up Q&A** – Context-aware “what if” queries.  
- 🏥 **Domain Expansion** – Beyond contracts to rental, healthcare, consent forms.  
- 🛡 **Google Cloud DLP API** – Mask sensitive data for trust & compliance.  

---

## 🔧 Tech Stack
**Frontend (Chrome Extension)**  
- `content.js` → Capture highlighted text  
- `popup.html / popup.js` → Interactive UI (Summary, Risks, Rewrite)  
- `background.js` → Secure backend bridge  

**Backend (FastAPI)**  
- REST API with **FastAPI + Uvicorn**  
- Modular AI agents: `summarization_agent`, `risk_agent`, `rewrite_agent`, `critic_agent`  
- Data validation with **Pydantic**  
- Deployed on **Google Cloud Run / Firebase**  

**AI / NLP Layer**  
- **Google Cloud Gen AI (Gemini-1.5-flash)** → Simplification, Risk Analysis, Explanations  
- (Optional) Critic Agent for cross-verification  

**Security & Privacy**  
- HTTPS + Auth  
- Only highlighted text processed  
- Future: DLP masking  

---

## 🏗 Architecture
```plaintext
USER (Chrome Extension)
 ├── content.js → Capture highlighted text
 ├── popup.js/html → Display results
 └── background.js → Secure API calls

BACKEND (FastAPI)
 ├── Summarization Module
 ├── Risk Identification Module
 ├── Plain-English Rewrite Module
 └── Follow-up Q&A (future)

AI LAYER (Google Cloud Gen AI)
 └── Gemini-1.5-flash for legal clause simplification
```

## 🔄 Process Flow

1. **User Interaction**
   - User opens contract **PDF / webpage**.  
   - Highlights a clause → Clicks **“Simplify with AI”**.  

2. **Chrome Extension**
   - Captures highlighted text.  
   - Sends securely to backend.  

3. **Backend (FastAPI + GenAI)**
   - Processes the text.  
   - Returns structured output:  
     - ✅ **Summary**  
     - ⚠️ **Risks & Obligations**  
     - 📝 **Plain-English Rewrite**  

4. **UI Display**
   - Results are shown in a **clean popup** for easy reading.  


## 📊 Market Impact

- 🎯 **Target Users**  
  Freelancers, startups, students, and small businesses.  
- 💰 **Affordable Clarity**  
  Saves time and helps prevent costly legal mistakes.  
- 🔑 **Trust & Control**  
  Privacy-first design that empowers users.  


## ✅ Hackathon Alignment

- 🛠 **Problem Solving** → Demystifies complex legal docs.  
- 💡 **Innovation** → Privacy-first, context-aware AI legal assistant.  
- ⚙️ **Feasibility** → Lightweight Chrome Extension + FastAPI backend.  
- ☁️ **Scalability** → Cloud-native (Cloud Run, Firebase, DLP).  
- 🌍 **Impact** → Improves access to legal understanding for non-lawyers.  



## 🚀 Setup Instructions

### 1. Backend
The backend is already deployed at:  
[https://demystifyinglegaldocuments.onrender.com/]((https://demystifyinglegaldocuments.onrender.com/)

### 2. Chrome Extension
1. Download the extension ZIP file from:  
   [Extension Download](https://drive.google.com/file/d/1gJXt9x-ETlQP14aZ_R9ByhyGPogCamxc/view?usp=sharing)
2. Unzip the downloaded file.
3. Open Chrome and navigate to:  
   `chrome://extensions/`
4. Enable **Developer mode** (toggle at top-right corner).
5. Click **Load unpacked** → Select the unzipped extension folder.
6. The extension is now ready to use! It will call your deployed backend API automatically.

## 📌 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.
