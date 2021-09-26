export PYTHON_POST_PROCESS_FILE=`which black`
openapi-generator generate \
    -i swagger.yml \
    -g python-flask \
    -o . \
    --package-name botticelli \
    --enable-post-process-file \
    --language-specific-primitives=Entity,Fact,Tag,User \
    --import-mappings=Entity=botticelli.database.Entity,Fact=botticelli.database.Fact,Tag=botticelli.database.Tag,User=botticelli.database.User
