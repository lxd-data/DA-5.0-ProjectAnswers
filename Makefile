clean:
	find . -name '*.pyc' -exec rm -rf {} \;
	find . -name '*.DS_Store' -exec rm {} \;
	find . -type dir -name '__pycache__' -delete;