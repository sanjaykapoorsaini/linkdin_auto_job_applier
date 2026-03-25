'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

Support me: https://github.com/sponsors/GodsScion

version:    26.01.20.5.08
'''

from modules.helpers import (
    critical_error_log,
    find_default_profile_directory,
    get_chrome_binary_and_version,
    get_default_temp_profile,
    make_directories,
    print_lg,
)
from config.settings import run_in_background, stealth_mode, disable_extensions, safe_mode, file_name, failed_file_name, logs_folder_path, generated_resume_path
from config.questions import default_resume_path
if stealth_mode:
    try:
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass
    import undetected_chromedriver as uc
else: 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import SessionNotCreatedException

def createChromeSession(isRetry: bool = False):
    make_directories([file_name,failed_file_name,logs_folder_path+"/screenshots",default_resume_path,generated_resume_path+"/temp"])
    # Set up WebDriver with Chrome Profile
    options = uc.ChromeOptions() if stealth_mode else Options()
    if run_in_background:   options.add_argument("--headless")
    if disable_extensions:  options.add_argument("--disable-extensions")

    print_lg("IF YOU HAVE MORE THAN 10 TABS OPENED, PLEASE CLOSE OR BOOKMARK THEM! Or it's highly likely that application will just open browser and not do anything!")
    profile_dir = find_default_profile_directory()
    if isRetry:
        print_lg("Will login with a guest profile, browsing history will not be saved in the browser!")
    elif profile_dir and not safe_mode:
        options.add_argument(f"--user-data-dir={profile_dir}")
    else:
        print_lg("Logging in with a guest profile, Web history will not be saved!")
        options.add_argument(f"--user-data-dir={get_default_temp_profile()}")
    if stealth_mode:
        print_lg("Downloading Chrome Driver... This may take some time. Undetected mode requires download every run!")
        chrome_bin, version_main = get_chrome_binary_and_version()
        uc_kw: dict = {}
        if chrome_bin:
            uc_kw["browser_executable_path"] = chrome_bin
        if version_main is not None:
            uc_kw["version_main"] = version_main
        # Do not set use_subprocess=False on macOS: undetected-chromedriver then uses multiprocessing
        # in a way that fails when this module runs createChromeSession() at import time (before
        # __main__ finishes), triggering "bootstrapping phase" errors with the 'spawn' start method.
        if chrome_bin:
            print_lg(f"Chrome binary: {chrome_bin}  (detected major version: {version_main or 'unknown'})")
        driver = uc.Chrome(options=options, **uc_kw)
    else: driver = webdriver.Chrome(options=options) #, service=Service(executable_path="C:\\Program Files\\Google\\Chrome\\chromedriver-win64\\chromedriver.exe"))
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)
    actions = ActionChains(driver)
    return options, driver, actions, wait

try:
    options, driver, actions, wait = None, None, None, None
    options, driver, actions, wait = createChromeSession()
except SessionNotCreatedException as e:
    critical_error_log("Failed to create Chrome Session, retrying with guest profile", e)
    options, driver, actions, wait = createChromeSession(True)
except Exception as e:
    err_s = str(e).lower()
    msg = 'Seems like Google Chrome is out dated. Update browser and try again! \n\n\nIf issue persists, try Safe Mode. Set, safe_mode = True in config.py \n\nPlease check GitHub discussions/support for solutions https://github.com/GodsScion/Auto_job_applier_linkedIn \n                                   OR \nReach out in discord ( https://discord.gg/fFp7uUzWCY )'
    if isinstance(e, TimeoutError):
        msg = "Couldn't download Chrome-driver. Set stealth_mode = False in config!"
    elif "certificate_verify_failed" in err_s or "ssl" in err_s and "cert" in err_s:
        msg = (
            "HTTPS certificate verification failed while downloading ChromeDriver (Chrome itself is usually fine).\n\n"
            "Fix: pip install truststore  (then run again; the bot injects it when available)\n"
            "Or: macOS python.org Python — run Install Certificates.command from the Python folder in Applications.\n"
            "Or: set stealth_mode = False in config/settings.py to use Selenium's driver manager.\n\n"
            "See: https://github.com/GodsScion/Auto_job_applier_linkedIn"
        )
    elif "cannot connect to chrome" in err_s or "chrome not reachable" in err_s:
        msg = (
            "Chrome started but WebDriver could not attach (often after a Chrome update).\n\n"
            "Try: pip install -U undetected-chromedriver selenium\n"
            "Or: set stealth_mode = False in config/settings.py\n"
            "Also: quit all Chrome windows and retry; avoid running multiple bot instances."
        )
    print_lg(msg)
    critical_error_log("In Opening Chrome", e)
    from pyautogui import alert
    alert(msg, "Error in opening chrome")
    try: driver.quit()
    except NameError: exit()
    
