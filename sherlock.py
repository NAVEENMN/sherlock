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


def setup_directory_structure(new_case_dir):
    if not os.path.exists(os.path.join(new_case_dir)):
        os.mkdir(os.path.join(root_path, new_case_dir))
        os.mkdir(os.path.join(root_path, new_case_dir, 'media'))
        os.mkdir(os.path.join(root_path, new_case_dir, 'evidences'))
        os.mkdir(os.path.join(root_path, new_case_dir, 'code'))


def add_notes(new_case_dir):
    with open(os.path.join(root_path, new_case_dir, 'notes.md'), "w") as fp:
        fp.write(f"# Notes\n")
        fp.write("---\n")


def add_evidence(new_case_dir):
    """
    For version 2.0 when dealing with complex investigations which many evidences.
    we need to support different types of evidences
    TODO: sherlock --addevidence, it will ask for type expreiment, stats, others and generated name.md file
    """
    with open(os.path.join(root_path, new_case_dir, 'evidences', 'evidence_1_template.md'), "w") as fp:
        fp.write(f"# Template Statistical Evidence\n")
        fp.write("---\n")

        fp.write("## Reproduction or Simulation\n")
        fp.write("Where did you get the data, how are you plotting it, What does variable means.\n")

        fp.write("## Observations\n")
        fp.write("A is correlated with B\n")
        fp.write("Here is a plot\n")

        fp.write("## Conclusion\n")
        fp.write("Your conclusion based on the observation goes here\n")

    with open(os.path.join(root_path, new_case_dir, 'evidences', 'evidence_2_template.md'), "w") as fp:
        fp.write(f"# Template Empirical Evidence\n")
        fp.write("---\n")
        fp.write("## Reproduction or Simulation\n")
        fp.write("Your reproduction steps goes here\n")

        fp.write("## Experiment\n")
        fp.write("Your Experimental details on how goes here\n")

        fp.write("## Observations\n")
        fp.write("What are the observations you are seeing from reproduction, simulation or experiment\n")
        fp.write("Here is a plot\n")
        fp.write("Here are the error logs\n")
        fp.write("Here are the images\n")

        fp.write("## Conclusion\n")
        fp.write("Your conclusion based on the observation goes here\n")


def add_stake_holders(new_case_dir):
    """
    For version 2.0 when dealing with complex investigations which many people we need to improve this section.
    TODO: sherlock --addperson <name>, it will ask relevant question and create dedicated name.md file
    """
    with open(os.path.join(root_path, new_case_dir, 'stakeholders.md'), "w") as fp:
        fp.write(f"# Stake holders\n")
        fp.write("---\n")
        fp.write("This document contains key people names, their roles, "
                 "why are they interested and what information can they provide.\n")


def add_main(new_case_dir, title):
    with open(os.path.join(root_path, new_case_dir, 'main.md'), "w") as fp:
        fp.write(f"# {title}\n")
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


def add_reference(new_case_dir):
    """
    For version 2.0 when dealing large scale you might need to use bib for reference management.
    """
    with open(os.path.join(root_path, new_case_dir, 'references.md'), "w") as fp:
        fp.write(f"# References \n")
        fp.write("---\n")


def create_a_new_case():
    print(f"Creating a new case")

    questions_4 = [
        {
            'type': 'input',
            'name': 'directory_name',
            'message': 'Directory name: ',
        }
    ]
    answers_4 = prompt(questions_4)

    questions_3 = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'Case title: ',
        }
    ]
    answers_3 = prompt(questions_3)

    new_case_dir = f"case_{answers_4['directory_name']}"
    setup_directory_structure(new_case_dir)
    add_notes(new_case_dir)
    add_stake_holders(new_case_dir)
    add_main(new_case_dir, answers_3['title'])
    add_evidence(new_case_dir)
    add_reference(new_case_dir)

    print(f"case {answers_3['title']} created.")


def main():
    create_a_new_case()


if __name__ == "__main__":
    main()
