default:
    @just --summary

clean:
    rm -rf dist

lock:
    poetry lock

build: clean lock
    poetry build

publish:
    #!/usr/bin/env fish
    set passes (op item get 'pypi token' --fields label=username,label=credential --format json | jq '.[] | .id, .value')
    set username (string replace -a '"' '' $passes[2])
    set credential (string replace -a '"' '' $passes[4])

    set _cmd poetry publish -u $username -p $credential
    #    echo $_cmd
    $_cmd
#    poetry publish -u "$username" -p "$credential"

#    poetry publish -u -p