Summary:	Library for full screen [S]VGA graphics
Summary(de):    Library für Vollbildschirm-[S]VGA-Grafiken
Summary(fr):    Bibliothèque pour les graphiques plein écran [S]VGA
Summary(pl):    Biblioteki dla pe³noekranowej grafiki [S]VGA
Summary(tr):    Tam-ekran [S]VGA çizimleri kitaplýðý
Name:		svgalib
Version:	1.3.1
Release:	4
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
URL:		http://www.cs.bgu.ac.il/~zivav/svgalib
Source:		%{name}-%{version}.tar.gz
Patch0:		svgalib-pld.patch
Patch1:		svgalib-glibc.patch
Patch2:		svgalib-buildroot.patch
Patch3:		svgalib-secu.patch
Patch4:		svgalib-tmp2var.patch
Prereq:		/sbin/ldconfig
Buildroot:	/tmp/%{name}-%{version}-root

Exclusivearch: i386 alpha

%description
SVGAlib is a library which allows applications to use full screen
graphics on a variety of hardware platforms. Many games and utilities
are avaiable which take advantage of SVGAlib for graphics access, as
it is more suitable for machines with little memory then X Windows is.

%description -l pl
Biblioteki dla pe³noekranowej grafiki [S]VGA. Wiele gier i programów 
u¿ytkowych korzysta z tych bibliotek, gdy¿ wymagaj± mniej pamiêci ni¿
X Window System. Biblioteki te s± w trakcie wycofywania poniewa¿ 
programy pisane z ich u¿yciem wymagaj± SUID'a. 

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken  zu benutzen. Viele Games
und Utilities nutzen diese Library für den Grafikzugriff, da sie 
für Maschinen mit wenig Speicher besser geeignet ist als X-Windows.

%description -l tr
SVGAlib, deðiþik donaným platformlarý üzerinde, uygulamalarýn tam ekran
çizim kullanmalarýný saðlayan bir kitaplýktýr. Az bellekli makinalar için
X Windows'tan daha uygun olmasýnýn yanýsýra, pek çok oyun ve yardýmcý
programlar çizim eriþimi için bu kitaplýðý kullanýr.

%package devel
Summary:     development libraries and include files for [S]VGA graphics
Group:       Development/Libraries
Group(pl):   Programowanie/Biblioteki
Requires:    %{name} = %{version}
Summary(de): Entwicklungs-Libraries und INCLUDE-Dateien für (S)VGA-Grafik. 
Summary(fr): Bibliothèques et en-têtes de développement pour graphiques [S]VGA.
Summary(pl): Pliki nag³ówkowe i dokumentacja dla [S]VGA 
Summary(tr): [S]VGA grafikleri için geliþtirme kitaplýklarý ve baþlýk dosyalarý

%description devel
These are the libraries and header files that are needed to build programs
which use SVGAlib. SVGAlib allows programs to use full screen graphics
on a variety of hardware platforms and without the overhead X requires.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja dla [S]VGA.

%description -l de devel
Dies sind die Libraries und Header-Dateien, die zum Erstellen von Programmen
erforderlich sind, die SVGAlib verwenden. Mit SVGAlib können Programme
Vollbildgrafiken auf einer Reihe von Plattformen verwenden, ohne den von X
erforderlichen Overhead.

%description -l fr devel
Bibliothèques et en-têtes pour construire des programmes utilisant SVGAlib.
SVGAlib permet au programmes d'utiliser des graphiques plein écran sur une
grande variété de plates-formes matérielles et sans le surcoût qu'entraîne X.

%description -l tr devel
Bu paket, SVGAlib kitaplýðýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarýný ve statik kitaplýklarý içerir.

%package static
Summary:	Static [S]VGA graphics librarires
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Summary(pl):	Biblioteki statyczne [S]VGA

%description static
Static [S]VGA graphics librarires.

%description -l pl static
Biblioteki statyczne [S]VGA.

%prep
%setup -q
gzip -d doc/man?/*gz
%patch0 -p1 
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

gzip doc/man*/*

%build
make OPTIMIZE="$RPM_OPT_FLAGS -pipe" static shared 
(cd utils; make)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{lib,etc/vga,usr/{bin,lib,include}} \
	$RPM_BUILD_ROOT/usr/share/man/man{1,3,5,6,7} \
	$RPM_BUILD_ROOT/var/state/svgalib

install utils/{convfont,dumpreg,restore*,fix132*,setmclk} \
	$RPM_BUILD_ROOT/usr/bin

rm -f $RPM_BUILD_ROOT/usr/bin/{*.c,*.o}

strip $RPM_BUILD_ROOT/usr/bin/*

install utils/{runx,savetextmode,textmode} $RPM_BUILD_ROOT/usr/bin

cp -a doc/man* $RPM_BUILD_ROOT/usr/share/man

install sharedlib/lib*.so.* $RPM_BUILD_ROOT/lib

ln -sf libvga.so.1.3.1 $RPM_BUILD_ROOT/lib/libvga.so
ln -sf libvga.so.1.3.1 $RPM_BUILD_ROOT/lib/libvga.so.1
ln -sf libvgagl.so.1.3.1 $RPM_BUILD_ROOT/lib/libvgagl.so
ln -sf libvgagl.so.1.3.1 $RPM_BUILD_ROOT/lib/libvgagl.so.1

install include/*.h $RPM_BUILD_ROOT/usr/include
install gl/vgagl.h $RPM_BUILD_ROOT/usr/include

install staticlib/*.a $RPM_BUILD_ROOT/lib

install libvga.config $RPM_BUILD_ROOT/etc/vga
install et4000.regs $RPM_BUILD_ROOT/etc/vga/libvga.et4000
install et6000.regs $RPM_BUILD_ROOT/etc/vga/libvga.et6000

gzip -9nf doc/{CHANGES*,DESIGN,READ*,SECURITY*,TODO} 0-README 0-RELEASE

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
  rm -f /var/lib/svgalib/fontdata
  rm -f /var/lib/svgalib/textregs
fi

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES*,DESIGN.gz,READ*,SECURITY*,TODO.gz} 0-README.gz 0-RELEASE.gz

%dir /etc/vga
%attr(1777,root,root) %dir /var/state/svgalib

%config(noreplace) %verify(not size mtime md5) /etc/vga/*

%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /lib/*.so.*

/usr/share/man/man[1567]/*

%files devel
%defattr(644,root,root,755)

/usr/include/*.h

%attr(755,root,root) /lib/*.so
/usr/share/man/man3/*

%files static
%attr(644,root,root) /lib/*.a

%changelog
* Wed Jan 20 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.3.1-4d]
- updated to stable version, 
- compressed man pages && documentation,
- added Prereq: /sbin/ldconfig,
- added Group(pl),

  by Micha³ Zalewski <lcamtuf@dione.ids.pl>

- fixed group of shared libraries & ELF binaries.  

* Mon Nov 02 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
[1.3.1-1d]
- updated to latest snapshoot - 1.3.1.19981020,
- added fiew missing ELF Binaries,
- shared libraries moved to /lib
- minor changes.

* Fri Oct 15 1998 Wojtek ¦lusarczyk <wojtek@SHADOW.EU.ORG>
[1.3.0-3d]
- build against Tornado,
- translation modified for pl,
- added missing %defattr support in %files static,
- minor changes.

* Thu Sep 24  1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
[1.3.0-3]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added alpha to Exclusivearch list,
- added using $RPM_OPT_FLAGS during compile,
- added full %attr description in %files.
- added modification witch allow build package from non-root account
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
