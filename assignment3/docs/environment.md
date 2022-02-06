# Python環境構築

## pyenvのインストール

[参考](https://zenn.dev/kenghaya/articles/9f07914156fab5)

1. Homebrewでpyenvをインストール
```zsh
brew install pyenv
```

2. pathを通す

zshなので

```zsh
export PYENV_ROOT="$HOME/.pyenv" >> ~/.zshrc
export PATH="$PYENV_ROOT/bin:$PATH" >> ~/.zshrc
eval "$(pyenv init --path)" >> ~/.zshrc
eval "$(pyenv init -)" >> ~/.zshrc
```

上記のようにする。
その後、shellの設定を読み込ませる

```zsh
source ~/.zshrc
```

このようにした。

## Pylance

Pylance周りでエラーが出たりしたので、ドキュメントを読みました。   
[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

pylanceにおいて、import周りでwarningがでるときに追加するべきextraPathsがあるとのことでみた記事

[microsoft公式](https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#unresolved-import-warnings)

[Pylanceの使い方まわり](https://bluebirdofoz.hatenablog.com/entry/2020/07/12/030238)

## Formatter , Linter

[参考記事](https://qiita.com/sin9270/items/85e2dab4c0144c79987d)

この記事を参考にvscodeのsetting.jsonをいじった
