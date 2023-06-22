import os

if __name__ == "__main__":
    command = "cd TestCases & pytest -n=3 --html=../Reports/report.html --self-contained-html -v"
    os.system(command)