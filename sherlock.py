"""
Version 1.0
Sherlock is an investigation tool build to automate investigation of something.
Sherlock organizes evidences, assumption, validations, references etc solve an investigation.
Sherlock 1.0 is designed for small scale investigation with small number of hypothesis and evidences.
"""
import os
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


def create_a_new_case():
    print(f"Creating a new case")

    questions_4 = [
        {
            'type': 'input',
            'name': 'directory_name',
            'message': 'Project name: ',
        }
    ]
    answers_4 = prompt(questions_4)

    questions_3 = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Title: ',
        }
    ]
    answers_3 = prompt(questions_3)

    new_case_dir = f"case_{answers_4['directory_name']}"

    if not os.path.exists(os.path.join(root_path, new_case_dir)):
        os.mkdir(os.path.join(root_path, new_case_dir))
        os.mkdir(os.path.join(root_path, new_case_dir, 'media'))
        os.mkdir(os.path.join(root_path, new_case_dir, 'evidences'))

    with open(os.path.join(root_path, new_case_dir, 'notes.md'), "w") as fp:
        fp.write(f"# Notes\n")
        fp.write("---\n")

    with open(os.path.join(root_path, new_case_dir, 'main.md'), "w") as fp:
        fp.write(f"# {answers_3['title']}\n")
        fp.write("---\n")
        fp.write("[[references]] [[evidences]]\n")

        fp.write("## Description\n")
        fp.write("Case description goes here. A short paragraph summarizing what has happend? "
                 "This a living document until the investigation closes.\n")

        fp.write("## Chain of events\n")
        fp.write("A list of events indexed by time. \n")
        fp.write("| Time      | Event |\n")
        fp.write("| ----------- | ----------- |\n")
        fp.write("| Jan 1      | Event 1 Occurs       |\n")
        fp.write("* Additional details for chain of events\n")

        fp.write("## Hypothesis\n")
        fp.write("A list of hypothesis that explains the observation. \n")
        fp.write("| Hypothesis      | Description |\n")
        fp.write("| ----------- | ----------- |\n")
        fp.write("| Hypothesis 1| A is causing B       |\n")
        fp.write("* Additional details for chain of events\n")

        fp.write("## Hypothesis Testing\n")
        fp.write("A Hypothesis can be tested. It can be backed by theoritical or experimental evidence. \n")

        fp.write("| Hypothesis  | Status | Evidence | \n")
        fp.write("| ----------- | ----------- |----------- |\n")
        fp.write("| Hypothesis 1| Not tested(T/F) | links |\n")

        fp.write("## Conclusion\n")
        fp.write("Your conclusion goes here.\n")

    with open(os.path.join(root_path, new_case_dir, 'references.md'), "w") as fp:
        fp.write(f"# References \n")
        fp.write("---\n")

    with open(os.path.join(root_path, new_case_dir, 'evidences', 'evidence_1.md'), "w") as fp:
        fp.write(f"# Evidence name\n")
        fp.write("---\n")
        fp.write("A is correlated with B\n")
        fp.write("Here is a plot\n")

    os.mkdir(os.path.join(root_path, new_case_dir, 'code'))

    print(f"case {answers_3['title']} created.")


def main():
    setup_directory_structure()
    create_a_new_case()


if __name__ == "__main__":
    main()
