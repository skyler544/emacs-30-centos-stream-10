#!/bin/sh

# The pure GTK build of emacs is not supported on X11, so try to avoid
# using if there is an alternative.

if [ "$XDG_SESSION_TYPE" = 'x11' ]; then
    case "$(readlink -f /usr/bin/emacs)" in
    */emacs-*.*-pgtk)
        if type emacs-gtk+x11 >/dev/null; then
            exec emacs-gtk+x11 "$@"
        elif type emacs-lucid >/dev/null; then
            exec emacs-lucid "$@"
        fi
        ;;
    esac
fi

exec emacs "$@"
