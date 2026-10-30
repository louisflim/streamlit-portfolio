# Louis Francis Lim | Streamlit Autobiography & Portfolio

A five-section Streamlit project for **CSIT 349 Applied AI**. This version features the GitHub projects **DormScout**, **GymTrack**, and **Hotel System**. Review every sentence, section, project description, and skill score to ensure it matches your own experience before turning it in.

## Requirements
- Python 3.11 or newer
- Windows 11 (or another supported OS)
- VS Code (recommended)

## Windows PowerShell setup

Open the project folder in VS Code and run in its **Terminal > New Terminal**:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If PowerShell refuses activation, **instead** run without activation:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Visit http://localhost:8501 (if the browser did not open automatically). Use Ctrl+C to stop.

## Customize BEFORE submitting
1. Change `SECTION = "G7"` in `app.py` if your current section is different.
2. Edit the autobiographical text to reflect your own life and words.
3. Review the three featured projects in `PROJECTS` in `app.py`:
   - DormScout — https://github.com/louisflim/dormscout (public README reviewed)
   - GymTrack — https://github.com/louisflim/gymtrack (public README reviewed)
   - Hotel System — https://github.com/louisflim/hotel-system (**returned 404 on October 30, 2026**; update to the correct public URL, and fill in role, tech stack, features, and outcome)
   Make sure all project claims and your individual contributions are accurate. The GymTrack README includes planned functionality, not necessarily verified finished features.
4. Adjust `SKILLS` self-ratings to honestly reflect your confidence.
5. To use your own portrait, put an image named **profile.jpg** alongside `app.py`. The built-in `avatar_placeholder.png` will otherwise display.
6. Test each sidebar page, the filters, charts, buttons, and the feedback form.

The feedback form **only stores messages in Streamlit session state**; it does not send email or persist user submissions.

## Option A: code submission
Zip `app.py`, `requirements.txt`, `avatar_placeholder.png`, and `.streamlit/config.toml` (and `profile.jpg` if you added one). You can include `README.md` too. Do **not** include `.venv`, passwords, or API keys.

Example submission comment: `Louis Francis Lim — BSIT 4 — Section G7` (verify section).

## Option B: Community Cloud (+10 bonus according to the activity handout)
1. Create a new **public** GitHub repository (example: `streamlit-autobiography-portfolio`).
2. Upload `app.py`, `requirements.txt`, `avatar_placeholder.png`, and `.streamlit/config.toml` (plus optional portrait) into the repo, preserving the `.streamlit` folder.
3. Open https://share.streamlit.io and sign in with GitHub.
4. Choose **Create app**, select your repository, branch `main`, entrypoint `app.py`, and deploy.
5. Open the public `https://...streamlit.app` URL in an incognito tab to ensure it works, then submit **that URL** and your name and section.

Privacy: If you put a personal photo, email, phone number, or other data in a public GitHub repository, those assets and your portfolio may become public. Only publish what you are comfortable sharing.
