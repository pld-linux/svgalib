#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_with	kernel24	# force using kernel24 headers
%bcond_without	smp		# don't build smp module
%bcond_without	userspace	# don't build userspace packages
#
%if %{with kernel24}
%define		_kernelsrcdir	/usr/src/linux-2.4
%endif
%define kernel26 %(echo %{_kernel_ver} | grep -q '2\.[0-4]\.' ; echo $?)
%if %{kernel26}
%define	k24	%{nil}
%else
%define	k24	24
%endif
Summary:	Library for full screen [S]VGA graphics
Summary(de):	Library f�r Vollbildschirm-[S]VGA-Grafiken
Summary(es):	Biblioteca para gr�ficos en pantalla llena [S]VGA
Summary(fr):	Une librairie graphique SVGA plein ecran de bas niveau
Summary(pl):	Biblioteki dla pe�noekranowej grafiki [S]VGA
Summary(pt_BR):	Biblioteca para gr�ficos em tela cheia [S]VGA
Summary(ru):	�������������� ���������� ������������� SVGA �������
Summary(tr):	Tam-ekran [S]VGA �izimleri kitapl���
Summary(uk):	������Ҧ����� ¦�̦����� �����������ϧ SVGA ���Ʀ��
Name:		svgalib
Version:	1.9.21
%define _rel	1
Release:	%{_rel}
License:	distributable
Group:		Libraries
Source0:	http://www.arava.co.il/matan/svgalib/%{name}-%{version}.tar.gz
# Source0-md5:	1bd8892ee38481051e4b4d85008c86be
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
Patch10:	%{name}-linux26.patch
URL:		http://www.arava.co.il/matan/svgalib/
%if %{with kernel} && %{with dist_kernel}
BuildRequires:	kernel-headers >= 2.4.0
%if %{kernel26}
BuildRequires:	kernel-module-build >= 2.6.0
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.118
# no sparc64 yet acc. to changelog
ExclusiveArch:	%{ix86} alpha amd64 arm hppa ia64 m68k mips ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/vga
%define		specflags	-fomit-frame-pointer

%if %{kernel26}
%define	kmodext	ko
%else
%define kmodext	o
%endif

%description
The svgalib package provides the SVGAlib low-level graphics library
for Linux. SVGAlib is a library which allows applications to use full
screen graphics on a variety of hardware platforms. Many games and
utilities use SVGAlib for their graphics.

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken zu benutzen. Viele Games und
Utilities nutzen diese Library f�r den Grafikzugriff, da sie f�r
Maschinen mit wenig Speicher besser geeignet ist als X-Window.

%description -l es
SVGAlib es una biblioteca que permite a las aplicaciones usar gr�ficos
de pantalla llena en una variedad de plataformas de hardware. Muchos
juegos y utilitarios son puestos a disposici�n para usar la SVGAlib
para acceso a gr�ficos, pues es m�s indicado en m�quinas con poca
memoria para ejecutar un sistema X Window.

%description -l fr
Le package svgalib apporte la librairie graphique SVGAlib de bas
niveau pour Linux. SVGAlib est une librairie qui permet aux
applications d'utiliser des graphismes en plein �cran sur diverses
plateformes mat�rielles. De nombreux jeux et utilitaires utilisent
SVGAlib pour leurs graphismes.

%description -l pl
Biblioteki dla pe�noekranowej grafiki [S]VGA. Wiele gier i program�w
u�ytkowych korzysta z tych bibliotek, gdy� wymagaj� mniej pami�ci ni�
X Window System.

%description -l pt_BR
SVGAlib � uma biblioteca que permite a aplica��es usar gr�ficos de
tela cheia em uma variedade de plataformas de hardware. Muitos jogos e
utilit�rios s�o disponibilizados para usar a SVGAlib para acesso a
gr�ficos, pois ele � mais indicado em m�quinas com pouca mem�ria para
rodar um sistema X Window.

%description -l ru
�������������� ����������� ���������� SVGAlib ������������ ������ �
������������ �������� VGA � SVGA � �������. SVGAlib ���������
����������� ������������ ������������� ������� �� �������������
���������� ����������.

���������� ��������� ��� � ������, ������������ SVGAlib ��� ������
�������. ��� ���������� ����� ���������� svgalib, ���� �� �����������
����� ���������.

%description -l tr
SVGAlib, de�i�ik donan�m platformlar� �zerinde, uygulamalar�n tam
ekran �izim kullanmalar�n� sa�layan bir kitapl�kt�r. Az bellekli
makinalar i�in X-Window'tan daha uygun olmas�n�n yan�s�ra, pek �ok
oyun ve yard�mc� programlar �izim eri�imi i�in bu kitapl��� kullan�r.

%description -l uk
������Ҧ����� ���Ʀ��� ¦�̦����� SVGAlib ��������դ ������ �
���Ʀ����� �������� VGA �� SVGA � �����̦. SVGAlib Ц�����դ
������������ ���Ʀ�� �� Ҧ�����Φ���� ��������� ����������.

���դ ������ ���� �� ���̦�, �˦ �������������� SVGAlib ��� ������
���Ʀ��. ��� ����Ȧ��� ���� ���������� svgalib, ���� �� ������դ����
������ ����������.

%package devel
Summary:	Development libraries and include files for [S]VGA graphics
Summary(de):	Entwicklungs-Libraries und INCLUDE-Dateien f�r (S)VGA-Grafik
Summary(es):	Bibliotecas de desarrollo y archivos de inclusi�n para gr�ficos [S]VGA
Summary(fr):	Outils pour d�velopper des programmes utilisant SVGAlib
Summary(pl):	Pliki nag��wkowe i dokumentacja dla [S]VGA
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclus�o para gr�ficos [S]VGA
Summary(ru):	����� ��� ���������� ��������, ������������ SVGAlib
Summary(tr):	[S]VGA grafikleri i�in geli�tirme kitapl�klar� ve ba�l�k dosyalar�
Summary(uk):	����� ��� �������� �������, �� �������������� SVGAlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The svgalib-devel package contains the libraries and header files
needed to build programs which will use the SVGAlib low-level graphics
library.

%description devel -l de
Dies sind die Libraries und Header-Dateien, die zum Erstellen von
Programmen erforderlich sind, die SVGAlib verwenden. Mit SVGAlib
k�nnen Programme Vollbildgrafiken auf einer Reihe von Plattformen
verwenden, ohne den von X erforderlichen Overhead.

%description devel -l es
Estas son las bibliotecas y archivos de inclusi�n que son necesarios
para construir programas que usan SVGAlib. Permite que los programas
usen gr�ficos de pantalla llena en una variedad de plataformas de
hardware sin el overhead del X.

%description devel -l fr
Le package svgalib-devel contient les librairies et les fichiers
d'ent�tes n�cessaires pour construire des programmes qui utiliseront
la librairie graphique plein �cran de bas-niveau SVGAlib.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla [S]VGA.

%description devel -l pt_BR
Estas s�o as bibliotecas e arquivos de inclus�o que s�o necess�rios
para construir programas que usam SVGAlib. SVGAlib permite que
programas usem gr�ficos de tela cheia em uma variedade de plataformas
de hardware sem o overhead do X.

%description devel -l ru
��� �����, ����������� ��� ���������� ��������, ������������
���������� SVGAlib. SVGAlib ��������� ���������� ������������
������������� ������� �� ������������� ���������� ���������� � ���
������������� ��������� ��� ����� X Window.

%description devel -l tr
Bu paket, SVGAlib kitapl���n� kullanan programlar geli�tirmek i�in
gereken ba�l�k dosyalar�n� ve statik kitapl�klar� i�erir.

%description devel -l uk
�� �����, ����Ȧ�Φ ��� ���Ц��æ� �������, �� ��������������
¦�̦����� SVGAlib. SVGAlib ��� ��������� �����צ��� ��������� �
������������� ���Ʀ��� �� Ҧ�����Φ���� ��������� ���������� �� ���
����Ȧ����Ԧ ��������� ��� ����� X Window.

%package static
Summary:	Static [S]VGA graphics librarires
Summary(pl):	Biblioteki statyczne [S]VGA
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com SVGAlib
Summary(ru):	����������� ���������� ��� ���������� ��������, ������������ SVGAlib
Summary(uk):	������Φ ¦�̦����� ��� �������� �������, �� �������������� SVGAlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static [S]VGA graphics librarires.

%description static -l pl
Biblioteki statyczne [S]VGA.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com SVGAlib.

%description static -l ru
��� �����, ����������� ��� ���������� ��������, ������������
���������� SVGAlib. SVGAlib ��������� ���������� ������������
������������� ������� �� ������������� ���������� ���������� � ���
������������� ��������� ��� ����� X Window.

%description static -l uk
�� �����, ����Ȧ�Φ ��� ���Ц��æ� �������, �� ��������������
¦�̦����� SVGAlib. SVGAlib ��� ��������� �����צ��� ��������� �
������������� ���Ʀ��� �� Ҧ�����Φ���� ��������� ���������� �� ���
����Ȧ����Ԧ ��������� ��� ����� X Window.

%package -n kernel%{k24}-video-svgalib_helper
Summary:	svgalib's helper kernel module
Summary(de):	Svgalibs Helferkernmodul
Summary(es):	Bibliotecas de desarrollo y archivos de inclusi�n para gr�ficos [S]VGA
Summary(pl):	Pomocniczy modu� j�dra svgaliba
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclus�o para gr�ficos [S]VGA
Group:		Base/Kernel
Release:	%{_rel}@%{_kernel_ver_str}
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod
Provides:	svgalib-helper = %{version}-%{release}
Obsoletes:	svgalib-helper

%description -n kernel%{k24}-video-svgalib_helper
This package contains the kernel module necessary to run svgalib-based
programs.

%description -n kernel%{k24}-video-svgalib_helper -l pl
Ten pakiet zawiera modu� j�dra potrzebny do uruchamiania program�w
opartych na svgalib.

%package -n kernel%{k24}-smp-video-svgalib_helper
Summary:	svgalib's helper kernel module for SMP
Summary(pl):	Pomoczniczy modu� j�dra svgalib dla SMP
Group:		Base/Kernel
Release:	%{_rel}@%{_kernel_ver_str}
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod
Provides:	svgalib-helper = %{version}-%{release}
Obsoletes:	svgalib-helper

%description -n kernel%{k24}-smp-video-svgalib_helper
This package contains the kernel module necessary to run svgalib-based
programs.

%description -n kernel%{k24}-smp-video-svgalib_helper -l pl
Ten pakiet zawiera modu� j�dra potrzebny do uruchamiania program�w
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

# remove backup of svgalib.7 - we don't want it in package
rm -f doc/man7/svgalib.7?*

%build
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

%if %{with kernel}
%if %{kernel26}
cd kernel/svgalib_helper
ln -sf %{_kernelsrcdir}/config-up .config
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf-up.h include/linux/autoconf.h
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
%{__make} -C %{_kernelsrcdir} modules \
	SUBDIRS=`pwd` \
	O=`pwd` \
	V=1
rm -rf .*.cmd include include2 scripts arch
cd -
%else
%{__make} -C kernel/svgalib_helper -f Makefile.alt \
	CC="%{kgcc}" \
	COPT="%{rpmcflags}" \
	INCLUDEDIR=%{_kernelsrcdir}/include
%endif
mv -f kernel/svgalib_helper/svgalib_helper.%{kmodext} \
	 kernel/svgalib_helper-up.%{kmodext}
rm -f kernel/svgalib_helper/*.*o

%if %{with smp}
%if %{kernel26}
cd kernel/svgalib_helper
ln -sf %{_kernelsrcdir}/config-smp .config
install -d include/{linux,config}
ln -sf %{_kernelsrcdir}/include/linux/autoconf-smp.h include/linux/autoconf.h
ln -sf %{_kernelsrcdir}/include/asm-%{_arch} include/asm
touch include/config/MARKER
%{__make} -C %{_kernelsrcdir} modules \
	SUBDIRS=`pwd` \
	O=`pwd` \
	V=1
cd -
%else
%{__make} -C kernel/svgalib_helper -f Makefile.alt \
	CC="%{kgcc}" \
	COPT="%{rpmcflags} -D__KERNEL_SMP" \
	INCLUDEDIR=%{_kernelsrcdir}/include
%endif
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/svgalib \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}{,smp}/misc

%if %{with userspace}
%{__make} installheaders installsharedlib installconfig installstaticlib \
	installutils installman lib3dkit-install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir} \
	sharedlibdir=%{_libdir}

install threeDKit/lib3dkit.a $RPM_BUILD_ROOT%{_libdir}
%endif

%if %{with kernel}
install kernel/svgalib_helper-up.%{kmodext} \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/misc/svgalib_helper.%{kmodext}
%if %{with smp}
install kernel/svgalib_helper/svgalib_helper.%{kmodext} \
	$RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}smp/misc/svgalib_helper.%{kmodext}
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n kernel%{k24}-video-svgalib_helper
%depmod %{_kernel_ver}

%postun -n kernel%{k24}-video-svgalib_helper
%depmod %{_kernel_ver}

%post	-n kernel%{k24}-smp-video-svgalib_helper
%depmod %{_kernel_ver}smp

%postun -n kernel%{k24}-smp-video-svgalib_helper
%depmod %{_kernel_ver}smp

%if %{with userspace}
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
%files -n kernel%{k24}-video-svgalib_helper
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/svgalib_helper.%{kmodext}*

%if %{with smp}
%files -n kernel%{k24}-smp-video-svgalib_helper
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}smp/misc/svgalib_helper.%{kmodext}*
%endif
%endif
