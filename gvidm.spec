Summary:	Application to quickly and easily change video resolutions in X
Summary(pl.UTF-8):	Aplikacja do szybkiej i łatwej zmiany rozdzielczości pod X
Name:		gvidm
Version:	0.8
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.dakotacom.net/~donut/programs/gvidm/%{name}-%{version}.tar.gz
# Source0-md5:	fa9bbf18561c7830e0f9b2d3995e3720
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://www.dakotacom.net/~donut/programs/gvidm.html
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
gvidm is a GTK+ app to quickly and easily change video resolutions in
X. Running it will pop up a list of available modes, upon choosing a
mode or cancelling, it exits. This makes it perfect for running from
an application menu or a hotkey, so you don't have to use ram for an
applet constantly running. If you are running dual or multi-head
displays, it will give you a list of screens so you can select the
appropriate one. gvidm is based on gvid (similar GNOME application).

%description -l pl.UTF-8
gvidm to aplikacja GTK+ do szybkiej i łatwej zmiany rozdzielczości pod
X. Po uruchomieniu wyświetla listę dostępnych trybów, a po wybraniu
któregoś lub rezygnacji kończy pracę. Dzięki temu może być łatwo
uruchamiana z menu aplikacji lub klawiszem skrótu i nie zajmuje przy
tym pamięci. W przypadku pracy z wieloma monitorami pozwala wybrać
ten, którego ma dotyczyć zmiana. gvidm bazuje na programie gvid
(służącym do tego samego celu, ale będącym aplikacją GNOME).

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_pixmapsdir},%{_desktopdir}}

install gvidm $RPM_BUILD_ROOT%{_bindir}
install gvidm.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
