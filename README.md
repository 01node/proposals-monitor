# Proposal Checker

This is a functional alpha version!

`proposals.py` is a Python script that scrapes some data from a RPC node to check if a validator has voted or not. It works on most tendermint based chains

## How can I set it up?

First of all, you need to download the latest release from [the project page](https://github.com/01node/proposals-checker/). After that, you should unzip it and complete the `config.toml` file with your info:

```sh
cp proposals.toml.sample proposals.toml
```

After filling in the info in  `config.toml` just run the script
```sh
python3 proposals.py
```

The script will send a message for each proposal in the voting period that the monitored address did not vote

Also, if you select debug in the `logLevel` section of `proposals.toml` the script will output the proposals to the terminal

Since this an alpha version more features will come :D. Please fill free to drop a Feature Request.

## How can I contribute?

Bug reports and feature requests are always welcome! If you want to contribute, feel free to open issues or PRs.
