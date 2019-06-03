# udemy-python-beginner
Learn python in Udemy class.

I decided to learn from this class.  
[Python 3 入門 + 応用 +アメリカのシリコンバレー流コードスタイルを学び、実践的なアプリ開発の準備をする](https://www.udemy.com/course/python-beginner/)

# Environment for python
I use [pyenv](https://github.com/pyenv/pyenv).

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

```bash
# python by pyenv {{{
export PYENV_ROOT="$HOME/.pyenv"
if [ -d $PYENV_ROOT ]; then
	export PATH="$PATH:$PYENV_ROOT/bin"
	eval "$(pyenv init -)"
fi
# }}}
```

# Install python

```bash
$ pyenv install 3.7.3
$ pyenv global 3.7.3
```

# Install Anaconda

```bash
$ pyenv install anaconda3-2019.03
```

# IDE for python

Install [PyCharm-Professional](https://www.jetbrains.com/pycharm/) on Ubuntu 18.04 LTS.  
Set the interpreter as "$HOME/.pyenv/versions/anaconda3-2019.03/bin/python"

referred to the following.  
https://linuxize.com/post/how-to-install-pycharm-on-ubuntu-18-04/


---
