#
# conditional build
# _without_dist_kernel		without distribution kernel
#
Summary:	Library for full screen [S]VGA graphics
Summary(de):	Library fЭr Vollbildschirm-[S]VGA-Grafiken
Summary(es):	Biblioteca para grАficos en pantalla llena [S]VGA
Summary(fr):	Une librairie graphique SVGA plein ecran de bas niveau
Summary(pl):	Biblioteki dla peЁnoekranowej grafiki [S]VGA
Summary(pt_BR):	Biblioteca para grАficos em tela cheia [S]VGA
Summary(ru):	Низкоуровневая библиотека полноэкранной SVGA графики
Summary(tr):	Tam-ekran [S]VGA Гizimleri kitaplЩПЩ
Summary(uk):	Низькор╕внева б╕бл╕отека повноекранно╖ SVGA граф╕ки
Name:		svgalib
Version:	1.9.14
Release:	%{_rel}
%define _rel	4
License:	distributable
Group:		Libraries
Source0:	http://www.cs.bgu.ac.il/~zivav/svgalib/%{name}-%{version}.tar.gz
Patch0:		%{name}-pld.patch
Patch1:		%{name}-tmp2TMPDIR.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-smp.patch
Patch4:		%{name}-threeDKit-make.patch
Patch5:		%{name}-nolrmi.patch
Patch6:		%{name}-alpha.patch
URL:		http://www.cs.bgu.ac.il/~zivav/svgalib/
ExclusiveArch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/vga

%description
The svgalib package provides the SVGAlib low-level graphics library
for Linux. SVGAlib is a library which allows applications to use full
screen graphics on a variety of hardware platforms. Many games and
utilities use SVGAlib for their graphics.

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken zu benutzen. Viele Games und
Utilities nutzen diese Library fЭr den Grafikzugriff, da sie fЭr
Maschinen mit wenig Speicher besser geeignet ist als X-Windows.

%description -l es
SVGAlib es una biblioteca que permite a las aplicaciones usar grАficos
de pantalla llena en una variedad de plataformas de hardware. Muchos
juegos y utilitarios son puestos a disposiciСn para usar la SVGAlib
para acceso a grАficos, pues es mАs indicado en mАquinas con poca
memoria para ejecutar un sistema X Window.

%description -l fr
Le package svgalib apporte la librairie graphique SVGAlib de bas
niveau pour Linux. SVGAlib est une librairie qui permet aux
applications d'utiliser des graphismes en plein Иcran sur diverses
plateformes matИrielles. De nombreux jeux et utilitaires utilisent
SVGAlib pour leurs graphismes.

%description -l pl
Biblioteki dla peЁnoekranowej grafiki [S]VGA. Wiele gier i programСw
u©ytkowych korzysta z tych bibliotek, gdy© wymagaj╠ mniej pamiЙci ni©
X Window System.

%description -l pt_BR
SVGAlib И uma biblioteca que permite a aplicaГУes usar grАficos de
tela cheia em uma variedade de plataformas de hardware. Muitos jogos e
utilitАrios sЦo disponibilizados para usar a SVGAlib para acesso a
grАficos, pois ele И mais indicado em mАquinas com pouca memСria para
rodar um sistema X Window.

%description -l ru
Низкоуровневая графическая библиотека SVGAlib обеспечивает работу с
графическими режимами VGA и SVGA с консоли. SVGAlib позволяет
приложениям использовать полноэкранную графику на разнообразных
аппаратных платформах.

Существует множество игр и утилит, использующих SVGAlib для вывода
графики. Вам необходимо будет установить svgalib, если вы используете
такие программы.

%description -l tr
SVGAlib, deПiЧik donanЩm platformlarЩ Эzerinde, uygulamalarЩn tam
ekran Гizim kullanmalarЩnЩ saПlayan bir kitaplЩktЩr. Az bellekli
makinalar iГin X Windows'tan daha uygun olmasЩnЩn yanЩsЩra, pek Гok
oyun ve yardЩmcЩ programlar Гizim eriЧimi iГin bu kitaplЩПЩ kullanЩr.

%description -l uk
Низькор╕внева граф╕чна б╕бл╕отека SVGAlib забезпечу╓ роботу з
граф╕чними режимами VGA та SVGA з консол╕. SVGAlib п╕дтриму╓
повноекранну граф╕ку на р╕зноман╕тних апаратних платформах.

╤сну╓ чимало ╕гор та утил╕т, як╕ використовують SVGAlib для виводу
граф╕ки. Вам необх╕дно буде встановити svgalib, якщо ви користу╓тесь
такими програмами.

%package -n kernel-video-svgalib_helper
Summary:	svgalib's helper kernel module
Summary(de):	Svgalibs Helferkernmodul
Summary(es):	Bibliotecas de desarrollo y archivos de inclusiСn para grАficos [S]VGA
Summary(pl):	Pomocniczy moduЁ j╠dra svgaliba
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclusЦo para grАficos [S]VGA
Group:		Base/Kernel
Release:	%{_rel}@%{_kernel_ver_str}
Prereq:		/sbin/depmod
%{!?_without_dist_kernel:%requires_releq_kernel_up}
Provides:	svgalib-helper = %{version}
Obsoletes:	svgalib-helper

%description -n kernel-video-svgalib_helper
This package contains the kernel module necessary to run svgalib-based
programs.

%description -n kernel-video-svgalib_helper -l pl
Ten pakiet zawiera moduЁ j╠dra potrzebny do uruchamiania programСw
opartych na svgalib.

%package -n kernel-smp-video-svgalib_helper
Summary:	svgalib's helper kernel module for SMP
Summary(pl):	Pomoczniczy moduЁ j╠dra svgalib dla SMP
Group:		Base/Kernel
Release:	%{_rel}@%{_kernel_ver_str}
Prereq:		/sbin/depmod
%{!?_without_dist_kernel:%requires_releq_kernel_smp}
Provides:	svgalib-helper = %{version}
Obsoletes:	svgalib-helper

%description -n kernel-smp-video-svgalib_helper
This package contains the kernel module necessary to run svgalib-based
programs.

%description -n kernel-smp-video-svgalib_helper -l pl
Ten pakiet zawiera moduЁ j╠dra potrzebny do uruchamiania programСw
opartych na svgalib.

%package devel
Summary:	Development libraries and include files for [S]VGA graphics
Summary(de):	Entwicklungs-Libraries und INCLUDE-Dateien fЭr (S)VGA-Grafik
Summary(es):	Bibliotecas de desarrollo y archivos de inclusiСn para grАficos [S]VGA
Summary(fr):	Outils pour dИvelopper des programmes utilisant SVGAlib
Summary(pl):	Pliki nagЁСwkowe i dokumentacja dla [S]VGA
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclusЦo para grАficos [S]VGA
Summary(ru):	Файлы для построения программ, использующих SVGAlib
Summary(tr):	[S]VGA grafikleri iГin geliЧtirme kitaplЩklarЩ ve baЧlЩk dosyalarЩ
Summary(uk):	Файли для побудови програм, що використовують SVGAlib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The svgalib-devel package contains the libraries and header files
needed to build programs which will use the SVGAlib low-level graphics
library.

%description devel -l de
Dies sind die Libraries und Header-Dateien, die zum Erstellen von
Programmen erforderlich sind, die SVGAlib verwenden. Mit SVGAlib
kЖnnen Programme Vollbildgrafiken auf einer Reihe von Plattformen
verwenden, ohne den von X erforderlichen Overhead.

%description devel -l es
Estas son las bibliotecas y archivos de inclusiСn que son necesarios
para construir programas que usan SVGAlib. Permite que los programas
usen grАficos de pantalla llena en una variedad de plataformas de
hardware sin el overhead del X.

%description devel -l fr
Le package svgalib-devel contient les librairies et les fichiers
d'entЙtes nИcessaires pour construire des programmes qui utiliseront
la librairie graphique plein Иcran de bas-niveau SVGAlib.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja dla [S]VGA.

%description devel -l pt_BR
Estas sЦo as bibliotecas e arquivos de inclusЦo que sЦo necessАrios
para construir programas que usam SVGAlib. SVGAlib permite que
programas usem grАficos de tela cheia em uma variedade de plataformas
de hardware sem o overhead do X.

%description devel -l ru
Это файлы, необходимые для компиляции программ, использующих
библиотеку SVGAlib. SVGAlib позволяет программам использовать
полноэкранную графику на разнообразных аппаратных платформах и без
необходимости запускать для этого X Window.

%description devel -l tr
Bu paket, SVGAlib kitaplЩПЩnЩ kullanan programlar geliЧtirmek iГin
gereken baЧlЩk dosyalarЩnЩ ve statik kitaplЩklarЩ iГerir.

%description devel -l uk
Це файли, необх╕дн╕ для комп╕ляц╕╖ програм, що використовують
б╕бл╕отеку SVGAlib. SVGAlib да╓ програмам можлив╕сть працювати з
повноекранною граф╕кою на р╕зноман╕тних апаратних платформах та без
необх╕дност╕ запускати для цього X Window.

%package static
Summary:	Static [S]VGA graphics librarires
Summary(pl):	Biblioteki statyczne [S]VGA
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com SVGAlib
Summary(ru):	Статические библиотеки для построения программ, использующих SVGAlib
Summary(uk):	Статичн╕ б╕бл╕отеки для побудови програм, що використовують SVGAlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static [S]VGA graphics librarires.

%description static -l pl
Biblioteki statyczne [S]VGA.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com SVGAlib.

%description static -l ru
Это файлы, необходимые для компиляции программ, использующих
библиотеку SVGAlib. SVGAlib позволяет программам использовать
полноэкранную графику на разнообразных аппаратных платформах и без
необходимости запускать для этого X Window.

%description static -l uk
Це файли, необх╕дн╕ для комп╕ляц╕╖ програм, що використовують
б╕бл╕отеку SVGAlib. SVGAlib да╓ програмам можлив╕сть працювати з
повноекранною граф╕кою на р╕зноман╕тних апаратних платформах та без
необх╕дност╕ запускати для цього X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%ifnarch %{ix86}
# lrmi is x86-only
%patch5 -p1
%endif
%patch6 -p1

# remove backup of svgalib.7 - we don't want it in package
rm -f doc/man7/svgalib.7?*

%build
%ifarch %{ix86}
NOASM=n
%else
NOASM=y
%endif
MOPT="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -pipe"
LDFLAGS="%{rpmldflags}"; export LDFLAGS

%{__make} CC=%{__cc} OPTIMIZE="$MOPT" NO_ASM="$NOASM" shared
ln -sf libvga.so.%{version} sharedlib/libvga.so
ln -sf libvgagl.so.%{version} sharedlib/libvgagl.so

%{__make} CC=%{__cc} LDFLAGS="-L../sharedlib $LDFLAGS" OPTIMIZE="$MOPT" -C utils
%ifarch %{ix86}
%{__make} CC=%{__cc} CFLAGS="$LDFLAGS $MOPT" -C lrmi-0.6m
%endif
%{__make} CC="%{__cc} -L../sharedlib $LDFLAGS $MOPT" -C threeDKit
%{__make} CC=%{__cc} OPTIMIZE="$MOPT" NO_ASM="$NOASM" static
%{__make} CC="%{__cc} $MOPT" -C threeDKit lib3dkit.a

# UP
%{__make} CC=%{__cc} -C kernel/svgalib_helper \
	INCLUDEDIR=%{_kernelsrcdir}/include

mv -f kernel/svgalib_helper/svgalib_helper.o  kernel/svgalib_helper/svgalib_helper-up.o
rm -f kernel/svgalib_helper/main.o

# SMP
%{__make} CC=%{__cc} -C kernel/svgalib_helper \
	SMP=1 \
	INCLUDEDIR=%{_kernelsrcdir}/include

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/svgalib \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install threeDKit/lib3dkit.a $RPM_BUILD_ROOT/%{_libdir}/
install kernel/svgalib_helper/svgalib_helper-up.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/svgalib_helper.o
install kernel/svgalib_helper/svgalib_helper.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/svgalib_helper.o

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n kernel-video-svgalib_helper
/sbin/depmod -a

%postun -n kernel-video-svgalib_helper
/sbin/depmod -a

%post -n kernel-smp-video-svgalib_helper
/sbin/depmod -a

%postun -n kernel-smp-video-svgalib_helper
/sbin/depmod -a

%files
%defattr(644,root,root,755)
%doc doc/{CHANGES*,DESIGN,READ*,TODO} 0-README

%dir %{_sysconfdir}
%dir /var/lib/svgalib
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man[1567]/*
%ifarch %{ix86}
%{_mandir}/man8/mode3.8*
%endif

%files -n kernel-video-svgalib_helper
%defattr(644,root,root,755)
%attr(600,root,root) /lib/modules/%{_kernel_ver}/misc/svgalib_helper.o

%files -n kernel-smp-video-svgalib_helper
%defattr(644,root,root,755)
%attr(600,root,root) /lib/modules/%{_kernel_ver}smp/misc/svgalib_helper.o

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
