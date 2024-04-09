#!/bin/sh

# The pure GTK build of emacs is not supported on X11, so try to avoid
# using if there is an alternative.

if [ "$XDG_SESSION_TYPE" = 'x11' ]; then
    emacs="$(readlink -f /usr/bin/emacs)"
    emacs="${emacs##*/}"
    emacs="${emacs%-*.*}"
    if [ "$emacs" = 'emacs' ]; then
        if type emacs-gtk+x11 >/dev/null; then
            exec emacs-gtk+x11 "$@"
        elif type emacs-lucid >/dev/null; then
            exec emacs-lucid "$@"
        fi
    fi
fi

exec emacs "$@"
