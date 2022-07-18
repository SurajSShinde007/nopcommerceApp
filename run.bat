
pytest -s -v -m "regression" --html=./Reports/report_chrome.html testCases/ --browser chrome
rem chrome
rem pytest -s -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome rem pytest -s -v -m "sanity or regressoin" --html-./Reports/report_chrome.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report_chrome.html testCases/ --browser chrome


rem firefox
rem pytest -s -v -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity or regressoin" --html=./Reports/ report_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/ report_firefox.html testCases/ --browser firefox
rem pytest -s -v -m "regression" --html=./Reports/ report_firefox.html testCases/ --browser firefox
