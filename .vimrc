syntax on
"Add the following lines
set smartindent  "sometimes while pasting use :set paste
set history=1000
set number                     " enable line numbers
set ruler
set tabstop=2 shiftwidth=2 expandtab softtabstop=2 "elminate tab headaches
set showmatch                  " show matching parenthesis
set nobackup
set noswapfile
set undolevels=1000      " use many muchos levels of undo
set title                " change the terminal's title

if exists('+colorcolumn')
  set colorcolumn=80
else
  au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>80v.\+', -1)
endif

set encoding=utf-8  " The encoding displayed.
set fileencoding=utf-8  " The encoding written to file.
"set autoindent "  copy the indentation from the previous line
set showmode "show you the mode you are in
set showcmd "will show you information about the current command going on
set hidden "you can have unwritten changes to a file and open a new file
set visualbell
set cursorline "sets a cursor line where you are on
set ttyfast
set backspace=indent,eol,start " make backspace work like most other apps
set laststatus=2

"work together to highlight search results (as you type)
set incsearch
set showmatch
set hlsearch

"If you search for an all-lowercase string your search will be case-insensitive,
"but if one or more characters is uppercase the search will be case-sensitive
set ignorecase
set smartcase

"makes Vim handle long lines correctly lines manage my line wrapping settings
"and also show a colored column at 85 characters
set wrap
set textwidth=80
set formatoptions=qrn1
set colorcolumn=80
