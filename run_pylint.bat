@echo off
cd /d "d:\0_Python\study_recommendation_system.worktrees\agents-linting-errors-fix-branch"
python -m pylint test_environment.py setup.py docs\conf.py src\data\make_dataset.py
