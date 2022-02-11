import os
import shutil
import subprocess
from PyInquirer import prompt

question_1 = [
        {
            'type': 'input',
            'name': 'rootpath',
            'message': 'Set your root path.\n',
            'default': '/Users/naveenmysore/Dropbox/obsidian/sherlock'
        }
    ]
answers_1 = prompt(question_1)
root_path = answers_1['rootpath']


def setup_directory_structure():
    if not os.path.exists(os.path.join(root_path, 'archive')):
        os.mkdir(os.path.join(root_path, 'archive'))

def open_a_case():
    print("Opening a case")

    questions_5 = [
        {
            'type': 'list',
            'name': 'case_type',
            'message': 'What cases you are looking for?',
            'choices': ['active', 'archived'],
            'filter': lambda val: val.lower()
        }
    ]
    answers_5 = prompt(questions_5)

    cases = os.listdir(os.path.join(root_path))
    if '.DS_Store' in cases:
        cases.remove('.DS_Store')
    if 'archive' in cases:
        cases.remove('archive')

    if answers_5 == 'archived':
        cases = os.listdir(os.path.join(root_path, 'archived'))

    questions_6 = [
        {
            'type': 'list',
            'name': 'case_name',
            'message': 'Pick a case',
            'choices': cases,
            'filter': lambda val: val.lower()
        }
    ]
    answers_6 = prompt(questions_6)

    path = os.path.join(root_path, answers_6['case_name'])
    if answers_5 == 'archived':
        path = os.path.join(root_path, 'archived', answers_6['case_name'])

    subprocess.run(["/Applications/Obsidian.app/Contents/MacOS/Obsidian", path])


def close_a_case():
    print(f"Closing a case")
    active_cases = os.listdir(os.path.join(root_path))
    if '.DS_Store' in active_cases:
        active_cases.remove('.DS_Store')
    if 'archive' in active_cases:
        active_cases.remove('archive')
    questions_4 = [
        {
            'type': 'list',
            'name': 'case_name',
            'message': 'What is the aim of research?',
            'choices': active_cases,
            'filter': lambda val: val.lower()
        }
    ]
    answers_4 = prompt(questions_4)
    shutil.move(src=os.path.join(root_path, answers_4['case_name']), dst=os.path.join(root_path, 'archive'))
    print(f"Case {answers_4['case_name']} archived.")


def create_a_new_case():
    print(f"Creating a new case")
    questions_3 = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Title: ',
        }
    ]
    answers_3 = prompt(questions_3)
    archived_cases = os.listdir(os.path.join(root_path, 'archive'))
    active_cases = os.listdir(os.path.join(root_path))
    if '.DS_Store' in archived_cases:
        archived_cases.remove('.DS_Store')
    if '.DS_Store' in active_cases:
        active_cases.remove('.DS_Store')
    if 'archive' in active_cases:
        active_cases.remove('archive')

    case_cnt = len(archived_cases) + len(active_cases)
    new_case_name = f"case_{case_cnt+1}"

    if not os.path.exists(os.path.join(root_path, new_case_name)):
        os.mkdir(os.path.join(root_path, new_case_name))
        os.mkdir(os.path.join(root_path, new_case_name, 'media'))

    with open(os.path.join(root_path, new_case_name, 'main.md'), "w") as fp:
        fp.write(f"# {answers_3['title']}\n")
        fp.write("---\n")
        fp.write("[[references]] [[evidences]]\n")

        fp.write("## Description\n")
        fp.write("Case description goes here.\n")

        fp.write("## Hypothesis\n")
        fp.write("Hypothesis 1\n")
        fp.write("Link to evidences in favour: \n")
        fp.write("Link to evidences not in favour: \n")
        fp.write("Hypothesis 2\n")
        fp.write("Link to evidences in favour: \n")
        fp.write("Link to evidences not in favour: \n")

        fp.write("## Conclusion\n")
        fp.write("Your conclusion goes here.\n")

    with open(os.path.join(root_path, new_case_name, 'references.md'), "w") as fp:
        fp.write(f"# References \n")
        fp.write("---\n")

    os.mkdir(os.path.join(root_path, new_case_name, 'evidences'))
    with open(os.path.join(root_path, new_case_name, 'evidences', 'evidence_copy.md'), "w") as fp:
        fp.write(f"# Evidence Copy\n")
        fp.write("---\n")
        fp.write("A is correlated with B\n")
        fp.write("Here is a plot\n")

    os.mkdir(os.path.join(root_path, new_case_name, 'code'))

    print(f"case {new_case_name} created.")


def main():
    setup_directory_structure()

    question_2 = [
        {
            'type': 'list',
            'name': 'options',
            'message': 'Please select the tool you wish to use.\n',
            'choices': ['open a case', 'create new case', 'close a case'],
        }
    ]
    answers_2 = prompt(question_2)
    opts = answers_2['options']

    if opts == "create new case":
        create_a_new_case()

    if opts == "close a case":
        close_a_case()

    if opts == "open a case":
        open_a_case()


if __name__ == "__main__":
    main()
