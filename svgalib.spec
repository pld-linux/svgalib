Summary:	Library for full screen [S]VGA graphics
Summary(de):    Library für Vollbildschirm-[S]VGA-Grafiken
Summary(fr):    Bibliothèque pour les graphiques plein écran [S]VGA
Summary(pl):    Biblioteki dla pe³noekranowej grafiki [S]VGA
Summary(tr):    Tam-ekran [S]VGA çizimleri kitaplýðý
Name:		svgalib
Version:	1.4.0
Release:	1
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://metalab.unc.edu/pub/Linux/libs/graphics/%{name}-%{version}.tar.gz
Patch0:		svgalib-pld.patch
Patch1:		svgalib-inc.patch
Patch2:		svgalib-tmp2var.patch
URL:		http://www.cs.bgu.ac.il/~zivav/svgalib
Buildroot:	/tmp/%{name}-%{version}-root
Exclusivearch: %{ix86} alpha

%define	_sysconfdir	/etc/vga
%define	_localstatedir	/var/state/%{name}

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
Summary:	development libraries and include files for [S]VGA graphics
Summary(de):	Entwicklungs-Libraries und INCLUDE-Dateien für (S)VGA-Grafik. 
Summary(fr):	Bibliothèques et en-têtes de développement pour graphiques [S]VGA.
Summary(pl):	Pliki nag³ówkowe i dokumentacja dla [S]VGA 
Summary(tr):	[S]VGA grafikleri için geliþtirme kitaplýklarý ve baþlýk dosyalarý
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

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
%patch1 -p0
%patch2 -p1
gzip doc/man*/*

%build
make OPTIMIZE="$RPM_OPT_FLAGS -pipe" shared 
ln -sf libvga.so.%{version} sharedlib/libvga.so
(cd utils; make)
make OPTIMIZE="$RPM_OPT_FLAGS -pipe" static 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,3,5,6,7},%{_sysconfdir}} \
	$RPM_BUILD_ROOT%{_localstatedir}

install utils/{convfont,dumpreg,restore*,fix132*,setmclk} \
	$RPM_BUILD_ROOT%{_bindir}

rm -f	$RPM_BUILD_ROOT%{_bindir}/{*.c,*.o}

strip	$RPM_BUILD_ROOT%{_bindir}/*

install utils/{runx,savetextmode,textmode} $RPM_BUILD_ROOT%{_bindir}

cp -a doc/man*				$RPM_BUILD_ROOT%{_mandir}

install sharedlib/lib*.so.*		$RPM_BUILD_ROOT%{_libdir}

ln -sf libvga.so.%{version}		$RPM_BUILD_ROOT%{_libdir}/libvga.so
ln -sf libvgagl.so.%{version}		$RPM_BUILD_ROOT%{_libdir}/libvgagl.so

install include/*.h			$RPM_BUILD_ROOT%{_includedir}
install gl/vgagl.h			$RPM_BUILD_ROOT%{_includedir}

install staticlib/*.a			$RPM_BUILD_ROOT%{_libdir}

install src/config/libvga.config	$RPM_BUILD_ROOT%{_sysconfdir}
install src/config/*.keymap		$RPM_BUILD_ROOT%{_sysconfdir}
install src/config/et4000.regs		$RPM_BUILD_ROOT%{_sysconfdir}/libvga.et4000

gzip -9nf doc/{CHANGES*,DESIGN,READ*,TODO} 0-README 0-RELEASE

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	rm -f %{_localstatedir}/fontdata
	rm -f %{_localstatedir}/textregs
fi

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES*,DESIGN.gz,READ*,TODO.gz} 0-README.gz 0-RELEASE.gz

%dir /etc/vga
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%{_mandir}/man[1567]/*

%attr(1777,root,root) %dir %{_localstatedir}

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/*.so
%{_mandir}/man3/*

%files static
%attr(644,root,root) %{_libdir}/*.a
