Summary:	Library for full screen [S]VGA graphics
Summary(de):	Library für Vollbildschirm-[S]VGA-Grafiken
Summary(fr):	Une librairie graphique SVGA plein ecran de bas niveau
Summary(pl):	Biblioteki dla pe³noekranowej grafiki [S]VGA
Summary(tr):	Tam-ekran [S]VGA çizimleri kitaplýðý
Name:		svgalib
Version:	1.9.2
Release:	2
License:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://metalab.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Patch0:		svgalib-pld.patch
Patch1:		svgalib-tmp2TMPDIR.patch
Patch2:		svgalib-DESTDIR.patch
Patch3:		svgalib-stderr.patch
URL:		http://www.cs.bgu.ac.il/~zivav/svgalib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Exclusivearch:	%{ix86} alpha

%define		_sysconfdir	/etc/vga
%define		_kernel_ver	%(grep UTS_RELEASE /usr/src/linux/include/linux/version.h 2>/dev/null | cut -d'"' -f2)

%description
The svgalib package provides the SVGAlib low-level graphics library for
Linux.  SVGAlib is a library which allows applications to use full screen
graphics on a variety of hardware platforms.  Many games and utilities use
SVGAlib for their graphics.

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer Reihe
von Plattformen Vollbild-Grafiken zu benutzen. Viele Games und Utilities
nutzen diese Library für den Grafikzugriff, da sie für Maschinen mit wenig
Speicher besser geeignet ist als X-Windows.

%description -l fr
Le package svgalib apporte la librairie graphique SVGAlib de bas niveau pour
Linux. SVGAlib est une librairie qui permet aux applications d'utiliser des
graphismes en plein écran sur diverses plateformes matérielles. De nombreux
jeux et utilitaires utilisent SVGAlib pour leurs graphismes.

%description -l pl
Biblioteki dla pe³noekranowej grafiki [S]VGA. Wiele gier i programów
u¿ytkowych korzysta z tych bibliotek, gdy¿ wymagaj± mniej pamiêci ni¿ X
Window System.

%description -l tr
SVGAlib, deðiþik donaným platformlarý üzerinde, uygulamalarýn tam ekran
çizim kullanmalarýný saðlayan bir kitaplýktýr. Az bellekli makinalar için X
Windows'tan daha uygun olmasýnýn yanýsýra, pek çok oyun ve yardýmcý
programlar çizim eriþimi için bu kitaplýðý kullanýr.

%package devel
Summary:	development libraries and include files for [S]VGA graphics
Summary(de):	Entwicklungs-Libraries und INCLUDE-Dateien für (S)VGA-Grafik
Summary(fr):	Outils pour développer des programmes utilisant SVGAlib
Summary(pl):	Pliki nag³ówkowe i dokumentacja dla [S]VGA
Summary(tr):	[S]VGA grafikleri için geliþtirme kitaplýklarý ve baþlýk dosyalarý
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The svgalib-devel package contains the libraries and header files needed to
build programs which will use the SVGAlib low-level graphics library.

%description -l de devel
Dies sind die Libraries und Header-Dateien, die zum Erstellen von
Programmen erforderlich sind, die SVGAlib verwenden. Mit SVGAlib können
Programme Vollbildgrafiken auf einer Reihe von Plattformen verwenden, ohne
den von X erforderlichen Overhead.

%description devel -l fr
Le package svgalib-devel contient les librairies et les fichiers d'entêtes
nécessaires pour construire des programmes qui utiliseront la librairie
graphique plein écran de bas-niveau SVGAlib.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja dla [S]VGA.

%description -l tr devel
Bu paket, SVGAlib kitaplýðýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarýný ve statik kitaplýklarý içerir.

%package static
Summary:	Static [S]VGA graphics librarires
Summary(pl):	Biblioteki statyczne [S]VGA
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static [S]VGA graphics librarires.

%description -l pl static
Biblioteki statyczne [S]VGA.

%prep
%setup -q
gzip -d doc/man?/*gz
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%{__make} OPTIMIZE="$RPM_OPT_FLAGS -pipe" shared
ln -sf libvga.so.%{version} sharedlib/libvga.so
(cd utils; make LDFLAGS="-L../sharedlib")
%{__make} OPTIMIZE="$RPM_OPT_FLAGS -pipe" static

%{__make} -C kernel/svgalib_helper

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT install
%{__make} install -C kernel/svgalib_helper DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/lib/svgalib

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*
gzip -9nf doc/{CHANGES*,DESIGN,READ*,TODO} 0-README \
	$RPM_BUILD_ROOT%{_mandir}/man?/*

%post
/sbin/ldconfig
/sbin/depmod -a

%postun
/sbin/ldconfig
/sbin/depmod -a

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES*,DESIGN.gz,READ*,TODO.gz} 0-README.gz

%dir /etc/vga
%dir /var/lib/svgalib
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(600,root,root) /lib/modules/*/misc/*.o
%{_mandir}/man[1567]/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
