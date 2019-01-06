# VIM Setup

This is my config file for Python development in VIM.

Make sure you have VIM 7.3 or higher:

`vim --version`

After checking, installing, and/or upgrading (if necessary), copy the contents of this file into a `.vimrc` file in your home directory.

`cd ~ && touch .vimrc && vim .vimrc`

To save and exit:

`:wq`

Open vim by typing `vim` in your terminal/console. Then type this to install the plugins: 

`:PluginInstall`

This will install the `vimrc` packages into a `.vim/bundle/` directory that you can exam later.

I did have a few issues with installing `YouCompleteMe` from Vundle. If you run into a server restart issue, type this to reinstall the YouCompleteMe packages:

`cd ~/.vim/bundle/YouCompleteMe && install.sh`

This should fix your autocomplete server issue. If not, refer to the documentation for [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) and [Vundle](https://github.com/VundleVim/Vundle.vim). 

Thanks to [Real Python](https://realpython.com/vim-and-python-a-match-made-in-heaven/) for the info which led to this setup! For additional information and tools, check out the link.

