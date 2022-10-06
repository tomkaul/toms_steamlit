#!bash
echo "Pushing to gitlab with comment:" \"$@\"
MSG="Update"
if [ $# -gt 0 ]
then
    MSG="$@"
fi
git commit -a -m "$MSG"
git push
