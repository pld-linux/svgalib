#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# don't build userspace packages
%bcond_with	grsec_kernel	# build for kernel-grsecurity
#
%if %{with kernel} && %{with dist_kernel} && %{with grsec_kernel}
%define	alt_kernel	grsecurity
%endif
#
%define	_rel	13
Summary:	Library for full screen [S]VGA graphics
Summary(de.UTF-8):	Library für Vollbildschirm-[S]VGA-Grafiken
Summary(es.UTF-8):	Biblioteca para gráficos en pantalla llena [S]VGA
Summary(fr.UTF-8):	Une librairie graphique SVGA plein ecran de bas niveau
Summary(pl.UTF-8):	Biblioteki dla pełnoekranowej grafiki [S]VGA
Summary(pt_BR.UTF-8):	Biblioteca para gráficos em tela cheia [S]VGA
Summary(ru.UTF-8):	Низкоуровневая библиотека полноэкранной SVGA графики
Summary(tr.UTF-8):	Tam-ekran [S]VGA çizimleri kitaplığı
Summary(uk.UTF-8):	Низькорівнева бібліотека повноекранної SVGA графіки
Name:		svgalib
Version:	1.9.25
Release:	%{_rel}
Epoch:		1
License:	distributable
Group:		Libraries
Source0:	http://www.arava.co.il/matan/svgalib/%{name}-%{version}.tar.gz
# Source0-md5:	4dda7e779e550b7404cfe118f1d74222
Patch0:		%{name}-pld.patch
Patch1:		%{name}-tmp2TMPDIR.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-smp.patch
Patch4:		%{name}-threeDKit-make.patch
Patch5:		%{name}-svgalib_helper_Makefile.patch
Patch6:		%{name}-link.patch
Patch7:		%{name}-module-alias.patch
Patch8:		%{name}-sparc.patch
Patch9:		%{name}-depend.patch
Patch10:	%{name}-ppc_memset.patch
Patch11:	%{name}-no-sys-io.patch
Patch12:	%{name}-linux-2.4.patch
Patch13:	%{name}-no-asm-segment.patch
Patch14:	%{name}-no-devfs.patch
URL:		http://www.arava.co.il/matan/svgalib/
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2
%endif
BuildRequires:	rpmbuild(macros) >= 1.379
# no sparc64 yet acc. to changelog
# kernel module requires at least sys32_ioctl translation function
# (isn't required for 32-bit userland on x86_64 too?)
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ia64 m68k mips ppc sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/vga
%define		specflags	-fomit-frame-pointer

%description
The svgalib package provides the SVGAlib low-level graphics library
for Linux. SVGAlib is a library which allows applications to use full
screen graphics on a variety of hardware platforms. Many games and
utilities use SVGAlib for their graphics.

%description -l de.UTF-8
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken zu benutzen. Viele Games und
Utilities nutzen diese Library für den Grafikzugriff, da sie für
Maschinen mit wenig Speicher besser geeignet ist als X-Window.

%description -l es.UTF-8
SVGAlib es una biblioteca que permite a las aplicaciones usar gráficos
de pantalla llena en una variedad de plataformas de hardware. Muchos
juegos y utilitarios son puestos a disposición para usar la SVGAlib
para acceso a gráficos, pues es más indicado en máquinas con poca
memoria para ejecutar un sistema X Window.

%description -l fr.UTF-8
Le package svgalib apporte la librairie graphique SVGAlib de bas
niveau pour Linux. SVGAlib est une librairie qui permet aux
applications d'utiliser des graphismes en plein écran sur diverses
plateformes matérielles. De nombreux jeux et utilitaires utilisent
SVGAlib pour leurs graphismes.

%description -l pl.UTF-8
Biblioteki dla pełnoekranowej grafiki [S]VGA. Wiele gier i programów
użytkowych korzysta z tych bibliotek, gdyż wymagają mniej pamięci niż
X Window System.

%description -l pt_BR.UTF-8
SVGAlib é uma biblioteca que permite a aplicações usar gráficos de
tela cheia em uma variedade de plataformas de hardware. Muitos jogos e
utilitários são disponibilizados para usar a SVGAlib para acesso a
gráficos, pois ele é mais indicado em máquinas com pouca memória para
rodar um sistema X Window.

%description -l ru.UTF-8
Низкоуровневая графическая библиотека SVGAlib обеспечивает работу с
графическими режимами VGA и SVGA с консоли. SVGAlib позволяет
приложениям использовать полноэкранную графику на разнообразных
аппаратных платформах.

Существует множество игр и утилит, использующих SVGAlib для вывода
графики. Вам необходимо будет установить svgalib, если вы используете
такие программы.

%description -l tr.UTF-8
SVGAlib, değişik donanım platformları üzerinde, uygulamaların tam
ekran çizim kullanmalarını sağlayan bir kitaplıktır. Az bellekli
makinalar için X-Window'tan daha uygun olmasının yanısıra, pek çok
oyun ve yardımcı programlar çizim erişimi için bu kitaplığı kullanır.

%description -l uk.UTF-8
Низькорівнева графічна бібліотека SVGAlib забезпечує роботу з
графічними режимами VGA та SVGA з консолі. SVGAlib підтримує
повноекранну графіку на різноманітних апаратних платформах.

Існує чимало ігор та утиліт, які використовують SVGAlib для виводу
графіки. Вам необхідно буде встановити svgalib, якщо ви користуєтесь
такими програмами.

%package devel
Summary:	Development libraries and include files for [S]VGA graphics
Summary(de.UTF-8):	Entwicklungs-Libraries und INCLUDE-Dateien für (S)VGA-Grafik
Summary(es.UTF-8):	Bibliotecas de desarrollo y archivos de inclusión para gráficos [S]VGA
Summary(fr.UTF-8):	Outils pour développer des programmes utilisant SVGAlib
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla [S]VGA
Summary(pt_BR.UTF-8):	Bibliotecas de desenvolvimento e arquivos de inclusão para gráficos [S]VGA
Summary(ru.UTF-8):	Файлы для построения программ, использующих SVGAlib
Summary(tr.UTF-8):	[S]VGA grafikleri için geliştirme kitaplıkları ve başlık dosyaları
Summary(uk.UTF-8):	Файли для побудови програм, що використовують SVGAlib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The svgalib-devel package contains the libraries and header files
needed to build programs which will use the SVGAlib low-level graphics
library.

%description devel -l de.UTF-8
Dies sind die Libraries und Header-Dateien, die zum Erstellen von
Programmen erforderlich sind, die SVGAlib verwenden. Mit SVGAlib
können Programme Vollbildgrafiken auf einer Reihe von Plattformen
verwenden, ohne den von X erforderlichen Overhead.

%description devel -l es.UTF-8
Estas son las bibliotecas y archivos de inclusión que son necesarios
para construir programas que usan SVGAlib. Permite que los programas
usen gráficos de pantalla llena en una variedad de plataformas de
hardware sin el overhead del X.

%description devel -l fr.UTF-8
Le package svgalib-devel contient les librairies et les fichiers
d'entêtes nécessaires pour construire des programmes qui utiliseront
la librairie graphique plein écran de bas-niveau SVGAlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla [S]VGA.

%description devel -l pt_BR.UTF-8
Estas são as bibliotecas e arquivos de inclusão que são necessários
para construir programas que usam SVGAlib. SVGAlib permite que
programas usem gráficos de tela cheia em uma variedade de plataformas
de hardware sem o overhead do X.

%description devel -l ru.UTF-8
Это файлы, необходимые для компиляции программ, использующих
библиотеку SVGAlib. SVGAlib позволяет программам использовать
полноэкранную графику на разнообразных аппаратных платформах и без
необходимости запускать для этого X Window.

%description devel -l tr.UTF-8
Bu paket, SVGAlib kitaplığını kullanan programlar geliştirmek için
gereken başlık dosyalarını ve statik kitaplıkları içerir.

%description devel -l uk.UTF-8
Це файли, необхідні для компіляції програм, що використовують
бібліотеку SVGAlib. SVGAlib дає програмам можливість працювати з
повноекранною графікою на різноманітних апаратних платформах та без
необхідності запускати для цього X Window.

%package static
Summary:	Static [S]VGA graphics librarires
Summary(pl.UTF-8):	Biblioteki statyczne [S]VGA
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com SVGAlib
Summary(ru.UTF-8):	Статические библиотеки для построения программ, использующих SVGAlib
Summary(uk.UTF-8):	Статичні бібліотеки для побудови програм, що використовують SVGAlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static [S]VGA graphics librarires.

%description static -l pl.UTF-8
Biblioteki statyczne [S]VGA.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com SVGAlib.

%description static -l ru.UTF-8
Это файлы, необходимые для компиляции программ, использующих
библиотеку SVGAlib. SVGAlib позволяет программам использовать
полноэкранную графику на разнообразных аппаратных платформах и без
необходимости запускать для этого X Window.

%description static -l uk.UTF-8
Це файли, необхідні для компіляції програм, що використовують
бібліотеку SVGAlib. SVGAlib дає програмам можливість працювати з
повноекранною графікою на різноманітних апаратних платформах та без
необхідності запускати для цього X Window.

%package -n kernel%{_alt_kernel}-video-svgalib_helper
Summary:	svgalib's helper kernel module
Summary(de.UTF-8):	Svgalibs Helferkernmodul
Summary(es.UTF-8):	Bibliotecas de desarrollo y archivos de inclusión para gráficos [S]VGA
Summary(pl.UTF-8):	Pomocniczy moduł jądra svgaliba
Summary(pt_BR.UTF-8):	Bibliotecas de desenvolvimento e arquivos de inclusão para gráficos [S]VGA
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel}
Requires(post,postun):	/sbin/depmod
Provides:	svgalib-helper = %{epoch}:%{version}-%{release}
Obsoletes:	svgalib-helper

%description -n kernel%{_alt_kernel}-video-svgalib_helper
This package contains the kernel module necessary to run svgalib-based
programs.

%description -n kernel%{_alt_kernel}-video-svgalib_helper -l pl.UTF-8
Ten pakiet zawiera moduł jądra potrzebny do uruchamiania programów
opartych na svgalib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
#%patch12 -p1
%patch13 -p1
%patch14 -p1

# remove backup of svgalib.7 - we don't want it in package
rm -f doc/man7/svgalib.7?*

%build
%if %{with kernel}
%build_kernel_modules -C kernel/svgalib_helper -m svgalib_helper
%endif

%if %{with userspace}
%ifarch %{ix86}
NOASM=n
%else
NOASM=y
%endif
MOPT="%{rpmcflags} -pipe"
LDFLAGS="%{rpmldflags}"; export LDFLAGS

%{__make} shared \
	CC="%{__cc}" \
	OPTIMIZE="$MOPT" \
	NO_ASM="$NOASM"

%{__make} -C utils \
	CC="%{__cc}" \
	LDFLAGS="-L../sharedlib $LDFLAGS" \
	OPTIMIZE="$MOPT"

%ifarch %{ix86}
%{__make} -C lrmi-0.6m \
	CC="%{__cc}" \
	CFLAGS="$LDFLAGS $MOPT"
%endif
%{__make} -C threeDKit \
	CC="%{__cc} -L../sharedlib $LDFLAGS $MOPT"
rm -f src/svgalib_helper.h

%{__make} static \
	CC="%{__cc}" \
	OPTIMIZE="$MOPT" \
	NO_ASM="$NOASM"

%{__make} -C threeDKit lib3dkit.a \
	CC="%{__cc} $MOPT" \
	ALLOBJS="\$(OBJECTS)"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT/var/lib/svgalib
%{__make} installheaders installsharedlib installconfig installstaticlib \
	installutils installman lib3dkit-install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	sharedlibdir=%{_libdir}

install threeDKit/lib3dkit.a $RPM_BUILD_ROOT%{_libdir}

%ifarch %{ix86}
# omitted by main Makefile
install lrmi-0.6m/vga_reset $RPM_BUILD_ROOT%{_bindir}
%endif
%endif

%if %{with kernel}
%install_kernel_modules -m kernel/svgalib_helper/svgalib_helper -d misc
%endif

# hack to kill wrong symlink to README.lrmi
mv -f lrmi-0.6m/README doc/README.lrmi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-svgalib_helper
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-video-svgalib_helper
%depmod %{_kernel_ver}

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc doc/{CHANGES*,DESIGN,READ*,TODO} 0-README

%dir %{_sysconfdir}
%dir /var/lib/svgalib
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man[1567]/*
%ifarch %{ix86}
%{_mandir}/man8/mode3.8*
%{_mandir}/man8/vga_reset.8*
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-video-svgalib_helper
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/svgalib_helper.ko*
%endif
