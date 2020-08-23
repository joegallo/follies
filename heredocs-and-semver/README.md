# Heredocs and Semver

I was writing a bash script and needed to process version numbers in a
semver-aware manner. This is easy enough to do in python, and I didn't
want to figure out how to do it in bash proper.

So I embedded all the python code in a heredoc in the bash script, and
then invoked it via `python -c`. Definitely not something you'd want
to do if the embedded subprogram gets big enough, but it solved the
problem I had.

```
$ ./heredocs-and-semver.sh <(echo -n "1.1.2 foobar")
1.1.2 foobar
$ ./heredocs-and-semver.sh <(echo -n "1.2.1 baxquux")
1.2.1 baxquux
$ ./heredocs-and-semver.sh <(echo -n "2.1.1 hameggs")
$
```

And thanks to Ernesto on stackoverflow for the [`read` trickery](https://stackoverflow.com/a/44828706/11062962).
