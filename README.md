# LinkedIn AI Auto Job Applier 🤖

This is a web scraping bot that automates applying to jobs on LinkedIn: it searches using your criteria, fills application forms, and can tailor answers from the job description and company info. In practice it can submit many Easy Apply applications in a single session.

**This repository** is a maintained fork. It keeps the upstream AGPLv3 license and original copyright; changes here include **`truststore` integration** so ChromeDriver downloads work on **macOS** and **corporate TLS** environments (where Python’s default CA bundle fails with `CERTIFICATE_VERIFY_FAILED`), **clearer errors** when Chrome/session setup fails, and README install notes for those cases. Upstream project: [GodsScion/Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn).

## 📽️ See it in Action
[![Auto Job Applier demo video](https://github.com/GodsScion/Auto_job_applier_linkedIn/assets/100998531/429f7753-ebb0-499b-bc5e-5b4ee28c4f69)](https://youtu.be/gMbB1fWZDHw)
Click on above image to watch the demo or use this link https://youtu.be/gMbB1fWZDHw


## ✨ Content
- [Introduction](#linkedin-ai-auto-job-applier-)
- [Demo Video](#%EF%B8%8F-see-it-in-action)
- [Index](#-content)
- [Install](#%EF%B8%8F-how-to-install)
- [Configure](#-how-to-configure)
- [Disclaimer](#-disclaimer)
- [Terms and Conditions](#%EF%B8%8F-terms-and-conditions)
- [License](#%EF%B8%8F-license)

<br>

## ⚙️ How to install

[![Auto Job Applier setup tutorial video](https://github.com/user-attachments/assets/9e876187-ed3e-4fbf-bd87-4acc145880a2)](https://youtu.be/f9rdz74e1lM?si=4fRBcte0nuvr6tEH)
Click on above image to watch the tutorial for installation and configuration or use this link https://youtu.be/f9rdz74e1lM (Recommended to watch it in 2x speed)

1. [Python 3.10](https://www.python.org/) or above. Visit https://www.python.org/downloads/ to download and install Python, or for windows you could visit Microsoft Store and search for "Python". **Please make sure Python is added to Path in System Environment Variables**.
2. Install [Undetected Chromedriver](https://pypi.org/project/undetected-chromedriver/), [PyAutoGUI](https://pypi.org/project/PyAutoGUI/), [Setuptools](https://pypi.org/project/setuptools/), and related packages. After Python is installed, open a terminal and run:
  ```
  pip install undetected-chromedriver pyautogui setuptools truststore openai flask-cors flask
  ```
  (`truststore` helps HTTPS certificate verification on macOS and some corporate networks when ChromeDriver is downloaded.)
3. Download and install latest version of [Google Chrome](https://www.google.com/chrome) in it's default location, visit https://www.google.com/chrome to download it's installer.
4. Clone this repo or download it as a zip. Example:
   ```bash
   git clone git@github.com:sanjaykapoorsaini/linkdin_auto_job_applier.git
   ```
   (HTTPS: `https://github.com/sanjaykapoorsaini/linkdin_auto_job_applier.git`)
5. (Not needed if you set `stealth_mode = True` in `config/settings.py` ) Download and install the appropriate [Chrome Driver](https://googlechromelabs.github.io/chrome-for-testing/) for Google Chrome and paste it in the location Chrome was installed, visit https://googlechromelabs.github.io/chrome-for-testing/ to download.
  <br> <br>
  ***OR*** 
  <br> <br>
  If you are using Windows, click on `windows-setup.bat` available in the `/setup` folder, this will install the latest chromedriver automatically.
6. If ChromeDriver download still fails with SSL errors after installing `truststore`, try `stealth_mode = False` in `config/settings.py` or fix certificates for your Python environment (see macOS **Install Certificates.command** for python.org builds).

[back to index](#-content)

<br>

## 🔧 How to configure
1. Open `personals.py` file in `/config` folder and enter your details like name, phone number, address, etc. Whatever you want to fill in your applications.
2. Open `questions.py` file in `/config` folder and enter your answers for application questions, configure wether you want the bot to pause before submission or pause if it can't answer unknown questions.
3. Open `search.py` file in `/config` folder and enter your search preferences, job filters, configure the bot as per your needs (these settings decide which jobs to apply for or skip).
4. Open `secrets.py` file in `/config` folder and enter your LinkedIn username, password to login and OpenAI API Key for generation of job tailored resumes and cover letters (This entire step is optional). If you do not provide username or password or leave them as default, it will login with saved profile in browser, if failed will ask you to login manually.
5. Open `settings.py` file in `/config` folder to configure the bot settings like, keep screen awake, click intervals (click intervals are randomized to seem like human behavior), run in background, stealth mode (to avoid bot detection), etc. as per your needs.
6. (Optional) Don't forget to add you default resume in the location you mentioned in `default_resume_path = "all resumes/default/resume.pdf"` given in `/config/questions.py`. If one is not provided, it will use your previous resume submitted in LinkedIn or (In Development) generate custom resume if OpenAI APT key is provided!
7. Run `runAiBot.py` and see the magic happen.
8. To run the Applied Jobs history UI, run `app.py` and open your browser at `http://localhost:5000`.

[back to index](#-content)

<br>

## 📜 Disclaimer

**This program is for educational purposes only. By downloading, using, copying, replicating, or interacting with this program or its code, you acknowledge and agree to abide by all applicable Terms, Conditions, Policies, and Licenses (including the AGPLv3 in this repo). Stay informed of license and policy changes. Additionally, comply with LinkedIn’s terms of service and policies on automation and data use. Usage is at your own risk; authors and contributors are not liable for misuse, damages, or legal consequences.**


## 🏛️ Terms and Conditions

Please consider the following:

- **LinkedIn Policies**: LinkedIn has specific policies regarding web scraping and data collection. The responsibility to review and comply with these policies before engaging, interacting, or undertaking any actions with this program bears upon yourself. Be aware of the limitations and restrictions imposed by LinkedIn to avoid any potential violation(s).

- **No Warranties or Guarantees**: This program is provided as-is, without any warranties or guarantees of any kind. The accuracy, reliability, and effectiveness of the program cannot be guaranteed. Use it at your own risk.

- **Disclaimer of Liability**: The creators and contributors of this program shall not be held responsible or liable for any damages or consequences arising from the direct or indirect use, interaction, or actions performed with this program. This includes but is not limited to any legal issues, loss of data, or other damages incurred.

- **Use at Your Own Risk**: It is important to exercise caution and ensure that your usage, interactions, and actions with this program comply with the applicable laws and regulations. Understand the potential risks and consequences associated with web scraping and data collection activities.

- **Chrome Driver**: This program utilizes the Chrome Driver for web scraping. Please review and comply with the terms and conditions specified for [Chrome Driver](https://chromedriver.chromium.org/home).


## ⚖️ License

Copyright (C) 2024 Sai Vignesh Golla  <saivigneshgolla@outlook.com>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

See [AGPLv3 LICENSE](LICENSE) for more info.


<br>

[back to index](#-content)

<br>

---

[back to the top](#linkedin-ai-auto-job-applier-)
