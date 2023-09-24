%global _hardened_build 1

# This file is encoded in UTF-8.  -*- coding: utf-8 -*-
Summary:       GNU Emacs text editor
Name:          emacs
Epoch:         1
Version:       29.1
Release:       %autorelease
License:       GPL-3.0-or-later AND CC0-1.0
URL:           http://www.gnu.org/software/emacs/
Source0:       https://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz
Source1:       https://ftp.gnu.org/gnu/emacs/emacs-%{version}.tar.xz.sig
# Emacs 29+ sign key
Source2:       https://keys.openpgp.org/vks/v1/by-fingerprint/17E90D521672C04631B1183EE78DAE0F3115E06B
Source4:       dotemacs.el
Source5:       site-start.el
Source6:       default.el
# Emacs Terminal Mode, #551949, #617355
Source7:       emacs-terminal.desktop
Source8:       emacs-terminal.sh
# rhbz#713600
Patch1:        emacs-spellchecker.patch
Patch2:        emacs-system-crypto-policies.patch
# causes a dependency on pkgconfig(systemd)
# => remove it if we stop using this patch
Patch3:        emacs-libdir-vs-systemd.patch
Patch5:        0001-configure-Remove-obsolete-check-for-b-i486-linuxaout.patch

BuildRequires: gcc
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: dbus-devel
BuildRequires: giflib-devel
BuildRequires: glibc-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libjpeg-turbo
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXpm-devel
BuildRequires: ncurses-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: zlib-devel
BuildRequires: gnutls-devel
BuildRequires: librsvg2-devel
BuildRequires: m17n-lib-devel
BuildRequires: libotf-devel
BuildRequires: libselinux-devel
BuildRequires: alsa-lib-devel
BuildRequires: gpm-devel
BuildRequires: liblockfile-devel
BuildRequires: libxml2-devel
BuildRequires: autoconf
BuildRequires: bzip2
BuildRequires: cairo
BuildRequires: texinfo
BuildRequires: gzip
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libacl-devel
BuildRequires: harfbuzz-devel
BuildRequires: jansson-devel
BuildRequires: systemd-devel
BuildRequires: libgccjit-devel
BuildRequires: libtree-sitter-devel
BuildRequires: libsqlite3x-devel
BuildRequires: libwebp-devel

BuildRequires: gtk3-devel
BuildRequires: webkit2gtk4.1-devel

BuildRequires: gnupg2

# For lucid
BuildRequires: Xaw3d-devel

# for Patch3
BuildRequires: pkgconfig(systemd)

%ifarch %{ix86}
BuildRequires: util-linux
%endif
BuildRequires: make

# Emacs doesn't run without a font, rhbz#732422
Requires:      google-noto-sans-mono-vf-fonts
Requires(preun): %{_sbindir}/alternatives
Requires(posttrans): %{_sbindir}/alternatives
Requires:      emacs-common = %{epoch}:%{version}-%{release}
Provides:      emacs(bin) = %{epoch}:%{version}-%{release}
Supplements:   ((libwayland-server or xorg-x11-server-Xorg) and emacs-common)

%define site_lisp %{_datadir}/emacs/site-lisp
%define site_start_d %{site_lisp}/site-start.d
%define bytecompargs -batch --no-init-file --no-site-file -f batch-byte-compile
%define pkgconfig %{_datadir}/pkgconfig
%define emacs_libexecdir %{_libexecdir}/emacs/%{version}/%{_host}
%define native_lisp %{_libdir}/emacs/%{version}/native-lisp

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with support for X windows.

%package lucid
Summary:       GNU Emacs text editor with LUCID toolkit X support
Requires:      google-noto-sans-mono-vf-fonts
Requires(preun): %{_sbindir}/alternatives
Requires(posttrans): %{_sbindir}/alternatives
Requires:      emacs-common = %{epoch}:%{version}-%{release}
Provides:      emacs(bin) = %{epoch}:%{version}-%{release}

%description lucid
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with support for X windows
using LUCID toolkit.

%package nox
Summary:       GNU Emacs text editor without X support
Requires(preun): %{_sbindir}/alternatives
Requires(posttrans): %{_sbindir}/alternatives
Requires:      emacs-common = %{epoch}:%{version}-%{release}
Provides:      emacs(bin) = %{epoch}:%{version}-%{release}

%description nox
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package provides an emacs binary with no X windows support for running
on a terminal.

%package common
Summary:       Emacs common files
# The entire source code is GPLv3+ except lib-src/etags.c which is
# also BSD.  Manual (info) is GFDL.
License:       GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later AND BSD-3-Clause
Requires(preun): %{_sbindir}/alternatives
Requires(posttrans): %{_sbindir}/alternatives
Requires:      %{name}-filesystem = %{epoch}:%{version}-%{release}
Requires:      libgccjit
Recommends:    (emacs or emacs-lucid or emacs-nox)
Recommends:    enchant2
Recommends:    info
Provides:      %{name}-el = %{epoch}:%{version}-%{release}
Obsoletes:     emacs-el < 1:24.3-29
# transient.el is provided by emacs in lisp/transient.el
Provides:      emacs-transient = 0.3.7
# the existing emacs-transient package is obsoleted by emacs 28+, last package
# version as of the release of emacs 28.1 is obsoleted
Obsoletes:     emacs-transient < 0.3.0-4

# Ideally, we'd package all tree-sitter parsers as RPMs, but, in the
# meantime, we need the following packages for
# treesit-install-language-grammar to be able to build the parsers for
# us at runtime:
Recommends:    ((gcc and gcc-c++) or clang)
Recommends:    git


%description common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor.

This package contains all the common files needed by emacs, emacs-lucid
or emacs-nox.

%package terminal
Summary:       A desktop menu item for GNU Emacs terminal.
Requires:      emacs = %{epoch}:%{version}-%{release}
BuildArch:     noarch

%description terminal
Contains a desktop menu item running GNU Emacs terminal. Install
emacs-terminal if you need a terminal with Malayalam support.

Please note that emacs-terminal is a temporary package and it will be
removed when another terminal becomes capable of handling Malayalam.

%package filesystem
Summary:       Emacs filesystem layout
BuildArch:     noarch

%description filesystem
This package provides some directories which are required by other
packages that add functionality to Emacs.

%package devel
Summary: Development header files for Emacs

%description devel
Development header files for Emacs.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

autoconf

grep -v "tetris.elc" lisp/Makefile.in > lisp/Makefile.in.new \
   && mv lisp/Makefile.in.new lisp/Makefile.in
grep -v "pong.elc" lisp/Makefile.in > lisp/Makefile.in.new \
   && mv lisp/Makefile.in.new lisp/Makefile.in

# Avoid trademark issues
rm -f lisp/play/tetris.el lisp/play/tetris.elc
rm -f lisp/play/pong.el lisp/play/pong.elc

%ifarch %{ix86}
%define setarch setarch %{_arch} -R
%else
%define setarch %{nil}
%endif

# Avoid duplicating doc files in the common subpackage
ln -s ../../%{name}/%{version}/etc/COPYING doc
ln -s ../../%{name}/%{version}/etc/NEWS doc


%build
export CFLAGS="-DMAIL_USE_LOCKF %{build_cflags}"
%set_build_flags

# Build Lucid binary
mkdir build-lucid && cd build-lucid
ln -s ../configure .

LDFLAGS=-Wl,-z,relro;  export LDFLAGS;

%configure --with-dbus --with-gif --with-jpeg --with-png --with-rsvg \
           --with-tiff --with-xft --with-xpm --with-x-toolkit=lucid --with-gpm=no \
           --with-modules --with-harfbuzz --with-cairo --with-json \
           --with-native-compilation=aot --with-tree-sitter --with-sqlite3 \
           --with-webp --with-xinput2
%{setarch} %make_build bootstrap
%{setarch} %make_build
cd ..

# Build binary without X support
mkdir build-nox && cd build-nox
ln -s ../configure .
%configure --with-x=no --with-modules --with-json \
           --with-native-compilation=aot --with-tree-sitter --with-sqlite3
%{setarch} %make_build bootstrap
%{setarch} %make_build
cd ..

# Build GTK+ binary
mkdir build-gtk && cd build-gtk
ln -s ../configure .

LDFLAGS=-Wl,-z,relro;  export LDFLAGS;

%configure --with-dbus --with-gif --with-jpeg --with-png --with-rsvg \
           --with-tiff --with-xpm --with-x-toolkit=gtk3 --with-gpm=no \
           --with-xwidgets --with-modules --with-harfbuzz --with-cairo --with-json \
           --with-native-compilation=aot --with-tree-sitter --with-sqlite3 \
           --with-webp --with-xinput2
%{setarch} %make_build bootstrap
%{setarch} %make_build
cd ..

# Remove versioned file so that we end up with .1 suffix and only one DOC file
rm build-{gtk,lucid,nox}/src/emacs-%{version}.*

# Create pkgconfig file
cat > emacs.pc << EOF
sitepkglispdir=%{site_lisp}
sitestartdir=%{site_start_d}

Name: emacs
Description: GNU Emacs text editor
Version: %{epoch}:%{version}
EOF

# Create macros.emacs RPM macro file
cat > macros.emacs << EOF
%%_emacs_version %{version}
%%_emacs_ev %{?epoch:%{epoch}:}%{version}
%%_emacs_evr %{?epoch:%{epoch}:}%{version}-%{release}
%%_emacs_sitelispdir %{site_lisp}
%%_emacs_sitestartdir %{site_start_d}
%%_emacs_bytecompile /usr/bin/emacs -batch --no-init-file --no-site-file --eval '(progn (setq load-path (cons "." load-path)))' -f batch-byte-compile
EOF

%install
cd build-gtk
%make_install
cd ..

# Let alternatives manage the symlink
rm %{buildroot}%{_bindir}/emacs
touch %{buildroot}%{_bindir}/emacs

# Do not compress the files which implement compression itself (#484830)
gunzip %{buildroot}%{_datadir}/emacs/%{version}/lisp/jka-compr.el.gz
gunzip %{buildroot}%{_datadir}/emacs/%{version}/lisp/jka-cmpr-hook.el.gz

# Install the emacs with LUCID toolkit
install -p -m 0755 build-lucid/src/emacs %{buildroot}%{_bindir}/emacs-%{version}-lucid

# Install the emacs without X
install -p -m 0755 build-nox/src/emacs %{buildroot}%{_bindir}/emacs-%{version}-nox

# Make sure movemail isn't setgid
chmod 755 %{buildroot}%{emacs_libexecdir}/movemail

mkdir -p %{buildroot}%{site_lisp}
install -p -m 0644 %SOURCE5 %{buildroot}%{site_lisp}/site-start.el
install -p -m 0644 %SOURCE6 %{buildroot}%{site_lisp}

# This solves bz#474958, "update-directory-autoloads" now finally
# works the path is different each version, so we'll generate it here
echo "(setq source-directory \"%{_datadir}/emacs/%{version}/\")" \
 >> %{buildroot}%{site_lisp}/site-start.el

mv %{buildroot}%{_bindir}/{etags,etags.emacs}
mv %{buildroot}%{_mandir}/man1/{ctags.1.gz,gctags.1.gz}
mv %{buildroot}%{_mandir}/man1/{etags.1.gz,etags.emacs.1.gz}
mv %{buildroot}%{_bindir}/{ctags,gctags}
# BZ 927996
mv %{buildroot}%{_infodir}/{info.info.gz,info.gz}

mkdir -p %{buildroot}%{site_lisp}/site-start.d

# Default initialization file
mkdir -p %{buildroot}%{_sysconfdir}/skel
install -p -m 0644 %SOURCE4 %{buildroot}%{_sysconfdir}/skel/.emacs

# Install pkgconfig file
mkdir -p %{buildroot}/%{pkgconfig}
install -p -m 0644 emacs.pc %{buildroot}/%{pkgconfig}

# Install rpm macro definition file
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 0644 macros.emacs %{buildroot}%{_rpmconfigdir}/macros.d/

# Installing emacs-terminal binary
install -p -m 755 %SOURCE8 %{buildroot}%{_bindir}/emacs-terminal

# After everything is installed, remove info dir
rm -f %{buildroot}%{_infodir}/dir

# Install desktop files
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %SOURCE7

# Remove duplicate desktop-related files
rm %{buildroot}%{_datadir}/%{name}/%{version}/etc/%{name}.{desktop,service}

# We don't ship the client variants yet
# https://src.fedoraproject.org/rpms/emacs/pull-request/12
rm %{buildroot}%{_datadir}/applications/emacsclient.desktop
rm %{buildroot}%{_datadir}/applications/emacsclient-mail.desktop

#
# Create file lists
#
rm -f *-filelist {common,el}-*-files

( TOPDIR=${PWD}
  cd %{buildroot}

  find .%{_datadir}/emacs/%{version}/lisp .%{site_lisp} \
    \( -type f -name '*.elc' -fprint $TOPDIR/common-lisp-none-elc-files \) -o \( -type d -fprintf $TOPDIR/common-lisp-dir-files "%%%%dir %%p\n" \) -o \( -name '*.el.gz' -fprint $TOPDIR/el-bytecomped-files -o -fprint $TOPDIR/common-not-comped-files \)

)

# Sorted list of info files
%define info_files auth autotype bovine calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eglot eieio eintr elisp emacs-gnutls emacs-mime emacs epa erc ert eshell eudc eww flymake forms gnus htmlfontify idlwave ido mairix-el message mh-e modus-themes newsticker nxml-mode octave-mode org pcl-cvs pgg rcirc reftex remember sasl sc semantic ses sieve smtpmail speedbar srecode todo-mode tramp transient url use-package vhdl-mode vip viper vtable widget wisent woman

for info_f in %info_files; do
    echo "%{_infodir}/${info_f}.info*" >> info-filelist
done
# info.gz is a rename of info.info.gz and thus needs special handling
echo "%{_infodir}/info*" >> info-filelist

# Put the lists together after filtering  ./usr to /usr
sed -i -e "s|\.%{_prefix}|%{_prefix}|" *-files
grep -vhE '%{site_lisp}(|/(default\.el|site-start\.d|site-start\.el))$' {common,el}-*-files > common-filelist

# Remove old icon
rm %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document23.svg

# Install all the pdmp with fingerprints
gtk_pdmp="emacs-$(./build-gtk/src/emacs --fingerprint 2>&1 | sed 's/.* //').pdmp"
install -p -m 0644 build-gtk/src/emacs.pdmp %{buildroot}%{emacs_libexecdir}/${gtk_pdmp}

lucid_pdmp="emacs-$(./build-lucid/src/emacs --fingerprint 2>&1 | sed 's/.* //').pdmp"
install -p -m 0644 build-lucid/src/emacs.pdmp %{buildroot}%{emacs_libexecdir}/${lucid_pdmp}

nox_pdmp="emacs-$(./build-nox/src/emacs --fingerprint 2>&1 | sed 's/.* //').pdmp"
install -p -m 0644 build-nox/src/emacs.pdmp %{buildroot}%{emacs_libexecdir}/${nox_pdmp}

# Install native compiled Lisp of all builds
gtk_comp_native_ver=$(ls -1 build-gtk/native-lisp)
lucid_comp_native_ver=$(ls -1 build-lucid/native-lisp)
nox_comp_native_ver=$(ls -1 build-nox/native-lisp)
cp -ar build-gtk/native-lisp/${gtk_comp_native_ver} %{buildroot}%{native_lisp}
cp -ar build-lucid/native-lisp/${lucid_comp_native_ver} %{buildroot}%{native_lisp}
cp -ar build-nox/native-lisp/${nox_comp_native_ver} %{buildroot}%{native_lisp}

(TOPDIR=${PWD}
 cd %{buildroot}
 find .%{native_lisp}/${gtk_comp_native_ver} \( -type f -name '*eln' -fprintf $TOPDIR/gtk-eln-filelist "%%%%attr(755,-,-) %%p\n" \) -o \( -type d -fprintf $TOPDIR/gtk-dirs "%%%%dir %%p\n" \)
)
(TOPDIR=${PWD}
 cd %{buildroot}
 find .%{native_lisp}/${lucid_comp_native_ver} \( -type f -name '*eln' -fprintf $TOPDIR/lucid-eln-filelist "%%%%attr(755,-,-) %%p\n" \) -o \( -type d -fprintf $TOPDIR/lucid-dirs "%%%%dir %%p\n" \)
)
(TOPDIR=${PWD}
 cd %{buildroot}
 find .%{native_lisp}/${nox_comp_native_ver} \( -type f -name '*eln' -fprintf $TOPDIR/nox-eln-filelist "%%%%attr(755,-,-) %%p\n" \) -o \( -type d -fprintf $TOPDIR/nox-dirs "%%%%dir %%p\n" \)
)
echo %{emacs_libexecdir}/${gtk_pdmp} >> gtk-eln-filelist
echo %{emacs_libexecdir}/${lucid_pdmp} >> lucid-eln-filelist
echo %{emacs_libexecdir}/${nox_pdmp} >> nox-eln-filelist

# remove leading . from filelists
sed -i -e "s|\.%{native_lisp}|%{native_lisp}|" *-eln-filelist *-dirs

# remove exec permissions from eln files to prevent the debuginfo extractor from
# trying to extract debuginfo from them
find %{buildroot}%{_libdir}/ -name '*eln' -type f | xargs chmod -x

# ensure native files are newer than byte-code files
# see: https://bugzilla.redhat.com/show_bug.cgi?id=2157979#c11
find %{buildroot}%{_libdir}/ -name '*eln' -type f | xargs touch

%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%preun
%{_sbindir}/alternatives --remove emacs %{_bindir}/emacs-%{version} || :

%posttrans
%{_sbindir}/alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version} 80 || :

%preun lucid
%{_sbindir}/alternatives --remove emacs %{_bindir}/emacs-%{version}-lucid || :
%{_sbindir}/alternatives --remove emacs-lucid %{_bindir}/emacs-%{version}-lucid || :

%posttrans lucid
%{_sbindir}/alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version}-lucid 70 || :
%{_sbindir}/alternatives --install %{_bindir}/emacs-lucid emacs-lucid %{_bindir}/emacs-%{version}-lucid 60 || :

%preun nox
%{_sbindir}/alternatives --remove emacs %{_bindir}/emacs-%{version}-nox || :
%{_sbindir}/alternatives --remove emacs-nox %{_bindir}/emacs-%{version}-nox || :

%posttrans nox
%{_sbindir}/alternatives --install %{_bindir}/emacs emacs %{_bindir}/emacs-%{version}-nox 70 || :
%{_sbindir}/alternatives --install %{_bindir}/emacs-nox emacs-nox %{_bindir}/emacs-%{version}-nox 60 || :

%preun common
%{_sbindir}/alternatives --remove emacs.etags %{_bindir}/etags.emacs || :

%posttrans common
%{_sbindir}/alternatives --install %{_bindir}/etags emacs.etags %{_bindir}/etags.emacs 80 \
       --slave %{_mandir}/man1/etags.1.gz emacs.etags.man %{_mandir}/man1/etags.emacs.1.gz || :

%files -f gtk-eln-filelist -f gtk-dirs
%{_bindir}/emacs-%{version}
%attr(0755,-,-) %ghost %{_bindir}/emacs

%files lucid -f lucid-eln-filelist -f lucid-dirs
%{_bindir}/emacs-%{version}-lucid
%attr(0755,-,-) %ghost %{_bindir}/emacs
%attr(0755,-,-) %ghost %{_bindir}/emacs-lucid

%files nox -f nox-eln-filelist -f nox-dirs
%{_bindir}/emacs-%{version}-nox
%attr(0755,-,-) %ghost %{_bindir}/emacs
%attr(0755,-,-) %ghost %{_bindir}/emacs-nox

%files common -f common-filelist -f info-filelist
%config(noreplace) %{_sysconfdir}/skel/.emacs
%{_rpmconfigdir}/macros.d/macros.emacs
%license etc/COPYING
%doc doc/NEWS BUGS README
%{_bindir}/ebrowse
%{_bindir}/emacsclient
%{_bindir}/etags.emacs
%{_bindir}/gctags
%{_datadir}/applications/emacs.desktop
%{_datadir}/applications/emacs-mail.desktop
%{_metainfodir}/%{name}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/emacs.png
%{_datadir}/icons/hicolor/scalable/apps/emacs.svg
%{_datadir}/icons/hicolor/scalable/apps/emacs.ico
%{_datadir}/icons/hicolor/scalable/mimetypes/emacs-document.svg
%{_mandir}/man1/ebrowse.1*
%{_mandir}/man1/emacs.1*
%{_mandir}/man1/emacsclient.1*
%{_mandir}/man1/etags.emacs.1*
%{_mandir}/man1/gctags.1*
%dir %{_datadir}/emacs/%{version}
%{_datadir}/emacs/%{version}/etc
%{_datadir}/emacs/%{version}/site-lisp
%dir %{emacs_libexecdir}/
%{emacs_libexecdir}/movemail
%{emacs_libexecdir}/hexl
%{emacs_libexecdir}/rcs2log
%{_userunitdir}/emacs.service
%attr(0644,root,root) %config(noreplace) %{site_lisp}/default.el
%attr(0644,root,root) %config %{site_lisp}/site-start.el
%{pkgconfig}/emacs.pc

%files terminal
%{_bindir}/emacs-terminal
%{_datadir}/applications/emacs-terminal.desktop

%files filesystem
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%dir %{_datadir}/emacs/site-lisp/site-start.d

%files devel
%{_includedir}/emacs-module.h

%changelog
%autochangelog
