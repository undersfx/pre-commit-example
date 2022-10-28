# Instalation

[official website](https://pre-commit.com/#install)

Install pre-commit in you python environment
```
pip install pre-commit
```

Activate the hook in you git repository
```
pre-commit install
```

Copy the config file to the root folder of the project.
```
cp .pre-commit-config.yaml ~/path/to/my/project
```



# Side Notes

To run pre-commit against all files
```
pre-commit run --all-files
```


To ignore checks if needed `(do not abuse of this!)`
```
git commit --no-verify
```
