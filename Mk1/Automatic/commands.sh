function create() {
    cd "Automatic"
    source .env
    python create.py "$1"
    cd $FILEPATH$1
    git init
    git remote add origin git@github.com:"$USERNAME"/"$1".git
    touch README.md
	touch .gitignore
    git add .
    git commit -m "Initial commit"
    git push -u origin master
}