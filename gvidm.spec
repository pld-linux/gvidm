#
# TODO:
# - add desktop file.
#
Summary:	Application to quickly and easily change video resolutions in X
Summary(pl):	Aplikacja do szybkiej i ³atwej zmiany rozdzielczo¶ci pod X
Name:		gvidm
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.dakotacom.net/~donut/programs/gvidm/%{name}-%{version}.tar.gz
# Source0-md5:	3a810437c21a7f68cb73b0e47c911374
URL:		http://www.dakotacom.net/~donut/programs/gvidm.html
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
gvidm is a gtk app to quickly and easily change video resolutions in
X. Running it will pop up a list of available modes, upon choosing a
mode or cancelling, it exits. This makes it perfect for running from
an application menu or a hotkey, so you don't have to use ram for an
applet constantly running. If you are running dual or multi-head
displays, it will give you a list of screens so you can select the
appropriate one. gvidm is based on gvid (similar GNOME application).

%description -l pl
gvidm to aplikacja gtk do szybkiej i ³atwej zmiany rozdzielczo¶ci pod
X. Po uruchomieniu wy¶wietla listê dostêpnych trybów, a po wybraniu
którego¶ lub rezygnacji koñczy pracê. Dziêki temu mo¿e byæ ³atwo
uruchamiany z menu aplikacji lub klawiszem skrótu i nie zajmuje przy
tym pamiêci. W przypadku pracy z wieloma monitorami pozwala wybraæ
ten, którego ma dotyczyæ zmiana. gvidm bazuje na programie gvid
(s³u¿±cym do tego samego celu, ale bêd±cym aplikacj± GNOME).

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install gvidm $RPM_BUILD_ROOT%{_bindir}
install gvidm.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
