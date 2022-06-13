export LC_ALL="en_US.UTF-8"
export PATH=$HOME/.local/bin:$PATH
export PATH="$HOME/.npm-global/bin:$PATH"  # ← put this line in .bashrc
export PATH="/home/rohanj/.cargo/bin:$PATH"  # ← put this line in .bashrc
export PATH="/home/rohanj/.scripts/:$PATH"  # ← put this line in .bashrc
# Dependancies You Need for this Config
# zsh-syntax-highlighting - syntax highlighting for ZSH in standard repos
# autojump - jump to directories with j or jc for child or jo to open in file manager
# zsh-autosuggestions - Suggestions based on your history

# Initial Setup
# touch "$HOME/.cache/zshhistory
# Setup Alias in $HOME/zsh/aliasrc
# git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
# echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>! ~/.zshrc

#add keybinds correctly
# case "${TERM}" in
#   cons25*|linux) # plain BSD/Linux console
#     bindkey '\e[H'    beginning-of-line   # home 
#     bindkey '\e[F'    end-of-line         # end  
#     bindkey '\e[5~'   delete-char         # delete
#     bindkey '[D'      emacs-backward-word # esc left
#     bindkey '[C'      emacs-forward-word  # esc right
#     ;;
#   *rxvt*) # rxvt derivatives
#     bindkey '\e[3~'   delete-char         # delete
#     bindkey '\eOc'    forward-word        # ctrl right
#     bindkey '\eOd'    backward-word       # ctrl left
#     # workaround for screen + urxvt
#     bindkey '\e[7~'   beginning-of-line   # home
#     bindkey '\e[8~'   end-of-line         # end
#     bindkey '^[[1~'   beginning-of-line   # home
#     bindkey '^[[4~'   end-of-line         # end
#     ;;
#   *xterm*) # xterm derivatives
#     bindkey '\e[H'    beginning-of-line   # home
#     bindkey '\e[F'    end-of-line         # end
#     bindkey '\e[3~'   delete-char         # delete
#     bindkey '\e[1;5C' forward-word        # ctrl right
#     bindkey '\e[1;5D' backward-word       # ctrl left
#     # workaround for screen + xterm
#     bindkey '\e[1~'   beginning-of-line   # home
#     bindkey '\e[4~'   end-of-line         # end
#     ;;
#   screen)
#     bindkey '^[[1~'   beginning-of-line   # home
#     bindkey '^[[4~'   end-of-line         # end
#     bindkey '\e[3~'   delete-char         # delete
#     bindkey '\eOc'    forward-word        # ctrl right
#     bindkey '\eOd'    backward-word       # ctrl left
#     bindkey '^[[1;5C' forward-word        # ctrl right
#     bindkey '^[[1;5D' backward-word       # ctrl left
#     ;;
# esac


# Custom Variables
# EDITOR=~/.local/bin/lvim
EDITOR=nano
export PF_INFO="ascii title os kernel wm editor shell uptime memory pallete pkgs"
# History in cache directory:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zshhistory
setopt share_history
# Basic auto/tab complete:
autoload -U compinit
autoload -U promptinit; promptinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)               # Include hidden files.
setopt histignorealldups
setopt inc_append_history
# Custom ZSH Binds
bindkey '^ ' autosuggest-accept
bindkey '^R' history-incremental-search-backward
bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char
bindkey '^H' backward-kill-word
bindkey '^[[3;5~' kill-word
bindkey "^[[1;3C" forward-word
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
bindkey "^[[1;3D" backward-word
bindkey "^[OA" history-search-backward
bindkey "^[OB" history-search-forward
# Load aliases and shortcuts if existent.
[ -f "$HOME/.zsh/aliasrc" ] && source "$HOME/.zsh/aliasrc"

#vim stuff

function x11-clip-wrap-widgets() {
    # NB: Assume we are the first wrapper and that we only wrap native widgets
    # See zsh-autosuggestions.zsh for a more generic and more robust wrapper
    local copy_or_paste=$1
    shift

    for widget in $@; do
        # Ugh, zsh doesn't have closures
        if [[ $copy_or_paste == "copy" ]]; then
            eval "
            function _x11-clip-wrapped-$widget() {
                zle .$widget
                xclip -in -selection clipboard <<<\$CUTBUFFER
            }
            "
        else
            eval "
            function _x11-clip-wrapped-$widget() {
                CUTBUFFER=\$(xclip -out -selection clipboard)
                zle .$widget
            }
            "
        fi

        zle -N $widget _x11-clip-wrapped-$widget
    done
}
print_center(){
    local x
    local y
    text="$*"
    x=$(( ($(tput cols) - ${#text}) / 2))
    echo -ne "\E[6n";read -sdR y; y=$(echo -ne "${y#*[}" | cut -d';' -f1)
    echo -ne "\033[${y};${x}f$*"
}
# Fzf folder cder
fzf-dir() {
    local dir ret=$?
    dir=$(fd . $HOME -a --type directory | fzf --height=40%)
    if [ -z "$dir" ]; then
        zle redisplay
        return 0
    fi 
    cd $dir
    local precmd
    for precmd in $precmd_functions; do
      $precmd
    done
    zle reset-prompt
    return $ret
}

fzf-dir-lvim() {
    local cmd ret=$?
    cmd=$(fd . -a |  fzf --preview="cat {}" --bind ctrl-u:preview-page-up,ctrl-d:preview-page-down)
    if [ -z "$cmd" ]; then
        zle redisplay
        return 0
    fi 
    lvim $cmd
    local precmd
    for precmd in $precmd_functions; do
      $precmd
    done
    zle reset-prompt
    return $ret
}
zle -N fzf-dir
# zle -N fzf-dir-lvim
bindkey "^F" fzf-dir
bindkey "^G" fzf-dir-lvim
bindkey -s "^[n" "lvim .^M"
bindkey -s "^[e" "nautilus . &; disown %1; ^M"
# main()

# clear the screen, put the cursor at line 10, and set the text color
# to light blue.

local copy_widgets=(
    vi-yank vi-yank-eol vi-delete vi-backward-kill-word vi-change-whole-line
)
local paste_widgets=(
    vi-put-{before,after}
)

# NB: can atm. only wrap native widgets
x11-clip-wrap-widgets copy $copy_widgets
x11-clip-wrap-widgets paste  $paste_widgets

#Conda stuff
#colorscript -e 28
figlet -f Speed SugoN | lolcat 
# figlet -f Speed Archbtw | lolcat -b
# figlet   -f Speed -c  Archbtw | sed 's/^/            /' | lolcat -b
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
#prompt spaceship
eval "$(starship init zsh)"

# !! Contents within this block are managed by 'conda init' !!
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null
source /usr/share/zsh/plugins/zsh-autocomplete/zsh-autocomplete.zsh 2>/dev/null
source /usr/share/autojump/autojump.zsh 2>/dev/null
export PATH=$HOME/.config/nvcode/utils/bin:$PATH
#	source /usr/share/zsh/plugins/zsh-vi-mode/zsh-vi-mode.plugin.zsh
source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh
