%define date 19981020
Summary:     Library for full screen [S]VGA graphics
Summary(de): Library für Vollbildschirm-[S]VGA-Grafiken
Summary(fr): Bibliothèque pour les graphiques plein écran [S]VGA
Summary(pl): Biblioteki do pe³noekranowej grafiki [S]VGA
Summary(tr): Tam-ekran [S]VGA çizimleri kitaplýðý
Name:        svgalib
Version:     1.3.1
Release:     %{date}.1
Copyright:   distributable
Group:       Libraries
Source:      http://www.cs.bgu.ac.il/~zivav/svgalib/%{name}-%{version}.%{date}.tar.gz
Patch0:      svgalib-config.patch
Patch1:      svgalib-buildroot.patch
Patch2:      svgalib-secu.patch
Patch3:      svgalib-non-root.patch
URL:         http://www.cs.bgu.ac.il/~zivav/svgalib/
Buildroot:   /tmp/%{name}-%{version}-root
Exclusivearch: i386 alpha
Exclusiveos: Linux

%description
SVGAlib is a library which allows applications to use full screen
graphics on a variety of hardware platforms. Many games and utilities
are avaiable which take advantage of SVGAlib for graphics access, as
it is more suitable for machines with little memory then X Windows is.

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken  zu benutzen. Viele Games
und Utilities nutzen diese Library für den Grafikzugriff, da sie 
für Maschinen mit wenig Speicher besser geeignet ist als X-Windows.

%description -l pl
Biblioteki do robienia aplikacji korzystaj±cych z pe³noekranowej grafiki
[S]VGA. Wiele gier i programów u¿ytkowych korzysta z tej biblioteki, gdy¿
wymagaj± mniej pamiêci ni¿ X Window System.

%description -l tr
SVGAlib, deðiþik donaným platformlarý üzerinde, uygulamalarýn tam ekran
çizim kullanmalarýný saðlayan bir kitaplýktýr. Az bellekli makinalar için
X Windows'tan daha uygun olmasýnýn yanýsýra, pek çok oyun ve yardýmcý
programlar çizim eriþimi için bu kitaplýðý kullanýr.

%package devel
Summary:     development libraries and include files for [S]VGA graphics
Summary(de): Entwicklungs-Libraries und INCLUDE-Dateien für (S)VGA-Grafik. 
Summary(fr): Bibliothèques et en-têtes de développement pour graphiques [S]VGA.
Summary(pl): Pliki nag³ówkowe i dokumentacja dla [S]VGA
Summary(tr): [S]VGA grafikleri için geliþtirme kitaplýklarý ve baþlýk dosyalarý
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
These are the libraries and header files that are needed to build programs
which use SVGAlib. SVGAlib allows programs to use full screen graphics
on a variety of hardware platforms and without the overhead X requires.

%description -l de devel
Dies sind die Libraries und Header-Dateien, die zum Erstellen von Programmen
erforderlich sind, die SVGAlib verwenden. Mit SVGAlib können Programme
Vollbildgrafiken auf einer Reihe von Plattformen verwenden, ohne den von X
erforderlichen Overhead.

%description -l fr devel
Bibliothèques et en-têtes pour construire des programmes utilisant SVGAlib.
SVGAlib permet au programmes d'utiliser des graphiques plein écran sur une
grande variété de plates-formes matérielles et sans le surcoût qu'entraîne X.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja dla [S]VGA.

%description -l tr devel
Bu paket, SVGAlib kitaplýðýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarýný ve statik kitaplýklarý içerir.

%package static
Summary:     Static [S]VGA graphics librarires
Summary(pl): Biblioteki statyczne [S]VGA
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static [S]VGA graphics librarires.

%prep
%setup -q
%patch0 -p1 -b .config
%patch1 -p1 -b .buildroot
%patch2 -p1 -b .secu
%patch3 -p1

%description -l pl static
Biblioteki statyczne [S]VGA.

%build
make static shared OPTIMIZE="$RPM_OPT_FLAGS -fomit-frame-pointer -pipe"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/vga,usr/{bin,include,lib,man/man{1,3,5,6,7}}}

export PATH=/sbin:$PATH
make install \
	INSTALL_PREFIX="$RPM_BUILD_ROOT" \
	includedir="$RPM_BUILD_ROOT/usr/include" \
	sharedlibdir="$RPM_BUILD_ROOT/usr/lib" \
	exec_prefix="$RPM_BUILD_ROOT/usr" \
	datadir="$RPM_BUILD_ROOT/etc/vga" \
	mandir="$RPM_BUILD_ROOT/usr/man" \
	INSTALL_PROGRAM="install -s" \
	INSTALL_SHLIB="install -s" \
	INSTALL_DATA="install -c"

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so.*.*} || :

%clean
rm -fr $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%config /etc/vga/*
%doc doc/{CHANGES*,DESIGN,FILES,Makefile,README*,SECURITY*,TODO} 0-README 0-RELEASE
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) /usr/lib/lib*.so.*.*
%attr(644, root,  man) /usr/man/man[1567]/*

%files devel
%defattr(644, root, root, 755)
/usr/include/*
%attr(755, root, root) /usr/lib/*.so
%attr(644, root,  man) /usr/man/man3/*

%files static
%attr(644, root, root)/usr/lib/*.a

%changelog
* Tue Dec  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.1-19981020.1]
- added gzipping man pages,
- added missing %attr in static %files.

* Thu Sep 24  1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3.0-3]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added alpha to Exclusivearch list,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files.
- added modification which allow build package from non-root account
  (svgalib-non-root.patch),
- added striping shared libraries.

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- verify dumpreg is not setuid (problem #760)
- specfile fiddles

* Thu Jul 30 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.3.0
- security patch

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Mon Apr 06 1998 Erik Troan <ewt@redhat.com>
- updated to svgalib 1.2.13
- uses a build root

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- removed Mach64 from configuration, as the driver does not work

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups
